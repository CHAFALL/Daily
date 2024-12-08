package com.qzp.bid.domain.live.service;

import com.qzp.bid.domain.deal.entity.Deal;
import com.qzp.bid.domain.deal.entity.DealStatus;
import com.qzp.bid.domain.deal.entity.Wish;
import com.qzp.bid.domain.deal.purchase.entity.Purchase;
import com.qzp.bid.domain.deal.purchase.repository.PurchaseRepository;
import com.qzp.bid.domain.deal.repository.DealRepository;
import com.qzp.bid.domain.deal.repository.WishRepository;
import com.qzp.bid.domain.deal.sale.entity.Sale;
import com.qzp.bid.domain.deal.sale.repository.SaleRepository;
import com.qzp.bid.domain.live.dto.LiveRecordingRes;
import com.qzp.bid.domain.live.dto.LiveRoomReq;
import com.qzp.bid.domain.live.dto.LiveRoomRes;
import com.qzp.bid.domain.live.entity.Video;
import com.qzp.bid.domain.live.repository.VideoRepository;
import com.qzp.bid.domain.sse.dto.SseDto;
import com.qzp.bid.domain.sse.dto.SseType;
import com.qzp.bid.domain.sse.service.SseService;
import com.qzp.bid.global.result.error.ErrorCode;
import com.qzp.bid.global.result.error.exception.BusinessException;
import com.qzp.bid.global.security.util.AccountUtil;
import io.openvidu.java.client.Connection;
import io.openvidu.java.client.ConnectionProperties;
import io.openvidu.java.client.ConnectionType;
import io.openvidu.java.client.OpenVidu;
import io.openvidu.java.client.OpenViduHttpException;
import io.openvidu.java.client.OpenViduJavaClientException;
import io.openvidu.java.client.OpenViduRole;
import io.openvidu.java.client.Recording;
import io.openvidu.java.client.Recording.OutputMode;
import io.openvidu.java.client.RecordingMode;
import io.openvidu.java.client.RecordingProperties;
import io.openvidu.java.client.Session;
import io.openvidu.java.client.SessionProperties;
import jakarta.annotation.PostConstruct;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.HashMap;
import java.util.List;
import java.util.Optional;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@Slf4j
@RequiredArgsConstructor
@Transactional(readOnly = true)
public class LiveServiceImpl implements LiveService {

    private final RedisTemplate redisTemplate;
    private final DealRepository<Deal> dealRepository;
    private final SaleRepository saleRepository;
    private final PurchaseRepository purchaseRepository;
    private final WishRepository wishRepository;
    private final SseService sseService;
    private final AccountUtil accountUtil;
    private final VideoRepository videoRepository;
    private final STTService sttService;
    private final SummaryService summaryService;
    private OpenVidu openVidu;
    @Value("${openvidu.url}")
    private String OPENVIDU_URL;
    @Value("${openvidu.secret}")
    private String OPENVIDU_SECRET;

    @PostConstruct
    public void init() {
        this.openVidu = new OpenVidu(OPENVIDU_URL, OPENVIDU_SECRET);
    }

    @Transactional
    @Override
    public LiveRoomRes JoinLiveRoom(LiveRoomReq liveRoomReq)
        throws OpenViduJavaClientException, OpenViduHttpException {

        long userId = liveRoomReq.getUserId();
        long dealId = liveRoomReq.getDealId();

        Deal deal = dealRepository.findById(dealId)
            .orElseThrow(() -> new BusinessException(ErrorCode.GET_SALE_FAIL));

        String sessionId = String.valueOf(
            redisTemplate.opsForHash().get("OpenVidu_SessionId", dealId));

        openVidu.fetch();
        Session session = null;
        for (Session s : openVidu.getActiveSessions()) {
            if (sessionId != null && s.getSessionId().equals(sessionId)) {
                session = s;
                break;
            }
        }

        Connection connection = null;
        ConnectionProperties connectionProperties = new ConnectionProperties.Builder().type(
            ConnectionType.WEBRTC).role(OpenViduRole.PUBLISHER).data(deal.toString()).build();

        if (session != null) { // 세션 존재

            connection = session.createConnection(connectionProperties);

            //  REDIS  <DealId : <UserId : ConnectionId>> 넣기
            HashMap<String, String> changehashMap = (HashMap<String, String>) redisTemplate.opsForHash()
                .get("OpenVidu_ConnectionId", dealId);
            changehashMap.put("USERID", connection.getConnectionId());
            redisTemplate.opsForHash().put("OpenVidu_ConnectionId", dealId, changehashMap);

        } else { // 세션 없음 -> 새로 만들기

            if (userId != Long.parseLong(accountUtil.getLoginMemberId())) {
                throw new BusinessException(ErrorCode.NOT_WRITER);
            }

            SessionProperties sessionProperties = new SessionProperties.Builder().customSessionId(
                "LIVECHATROOMID" + dealId).recordingMode(RecordingMode.MANUAL).build();

            session = openVidu.createSession(sessionProperties);
            session.fetch();
            connection = session.createConnection(connectionProperties);

            if (deal.getClass().getSimpleName().equals("Purchase")) {
                Purchase purchase = purchaseRepository.findById(dealId)
                    .orElseThrow(() -> new BusinessException(ErrorCode.GET_PURCHASE_FAIL));
                purchase.setStatus(DealStatus.LIVE);
                purchaseRepository.save(purchase);

            }

            // 세션 만들어지면 알람 보내기
            Optional<List<Wish>> wishes = wishRepository.findByDealId(dealId);
            if (wishes.isPresent()) {
                for (Wish wish : wishes.get()) {
                    sseService.send(SseDto.of(wish.getMember().getId(), wish.getDeal().getId(),
                        wish.getDeal().getClass().getSimpleName(), SseType.START_LIVE,
                        LocalDateTime.now()));
                }
            }

            // Redis  <DealId : SessionId> 넣기
            redisTemplate.opsForHash().put("OpenVidu_SessionId", dealId, session.getSessionId());

            // REDIS  <DealId : <UserId : ConnectionId>> 넣기
            HashMap<Long, String> redisHashValue = new HashMap<>();
            redisHashValue.put(userId, connection.getConnectionId());
            redisTemplate.opsForHash().put("OpenVidu_ConnectionId", dealId, redisHashValue);
        }

        // 응답에 필요한 정보 구성
        LiveRoomRes liveRoom = LiveRoomRes.builder().roomNum(dealId).roomName(deal.getTitle())
            .token(connection.getToken()).build();

        return liveRoom;
    }

    @Override
    @Transactional
    public Recording StartRecording(LiveRoomReq liveRoomReq)
        throws OpenViduJavaClientException, OpenViduHttpException {

        long userId = liveRoomReq.getUserId();
        long dealId = liveRoomReq.getDealId();

        Deal deal = dealRepository.findById(dealId)
            .orElseThrow(() -> new BusinessException(ErrorCode.DEAL_ID_NOT_EXIST));

        if (userId != Long.parseLong(accountUtil.getLoginMemberId())) {
            throw new BusinessException(ErrorCode.NOT_WRITER);
        }

        String sessionId = String.valueOf(
            redisTemplate.opsForHash().get("OpenVidu_SessionId", dealId));

        RecordingProperties properties = new RecordingProperties.Builder().outputMode(
                OutputMode.COMPOSED).hasAudio(true).hasVideo(true).name("LIVE" + dealId).frameRate(30)
            .resolution("600x900").build();

        openVidu.fetch();
        Session session = null;
        for (Session s : openVidu.getActiveSessions()) {
            if (sessionId != null && s.getSessionId().equals(sessionId)) {
                session = s;
                break;
            }
        }

        // 녹화 시작
        Recording recording = openVidu.startRecording(session.getSessionId(), properties);
        // Record Id Redis에 저장
        redisTemplate.opsForHash().put("OpenVidu_recording", dealId, recording.getId());

        // 상태 바꾸기 : LIVE
        if (deal.getClass().getSimpleName().equals("Sale")) {
            Sale sale = saleRepository.findById(dealId)
                .orElseThrow(() -> new BusinessException(ErrorCode.SALE_ID_NOT_EXIST));
            sale.setStatus(DealStatus.LIVE);
            saleRepository.save(sale);
        }

        Video video = Video.builder().dealId(dealId).name("LIVE" + dealId).build();
        videoRepository.save(video);

        return recording;

    }

    @Transactional
    @Override
    public Recording EndRecording(LiveRoomReq liveRoomReq)
        throws OpenViduJavaClientException, OpenViduHttpException {

        long userId = liveRoomReq.getUserId();
        long dealId = liveRoomReq.getDealId();

        Deal deal = dealRepository.findById(dealId)
            .orElseThrow(() -> new BusinessException(ErrorCode.DEAL_ID_NOT_EXIST));

        if (userId != Long.parseLong(accountUtil.getLoginMemberId())) {
            throw new BusinessException(ErrorCode.NOT_WRITER);
        }

        String recordingId = String.valueOf(
            redisTemplate.opsForHash().get("OpenVidu_recording", dealId));

        Recording recording = openVidu.getRecording(recordingId);
        // 상태 바꾸기 : AUCTION
        if (deal.getClass().getSimpleName().equals("Sale")) {
            Sale sale = saleRepository.findById(dealId)
                .orElseThrow(() -> new BusinessException(ErrorCode.SALE_ID_NOT_EXIST));
            sale.setStatus(DealStatus.AUCTION);
            saleRepository.save(sale);
        } else {
            Purchase purchase = purchaseRepository.findById(dealId)
                .orElseThrow(() -> new BusinessException(ErrorCode.GET_PURCHASE_FAIL));
            purchase.setStatus(DealStatus.AUCTION);
            purchaseRepository.save(purchase);
        }
        recording = openVidu.stopRecording(recording.getId());
        Video video = videoRepository.findByDealId(dealId)
            .orElseThrow(() -> new BusinessException(ErrorCode.VIDEO_NOT_EXIST));

        video.setRunTime(String.format("%02d",
            ChronoUnit.HOURS.between(video.getCreateTime(), LocalDateTime.now())) + ":"
            + String.format("%02d",
            (ChronoUnit.MINUTES.between(video.getCreateTime(), LocalDateTime.now()) % 60)) + ":"
            + String.format("%02d",
            (ChronoUnit.SECONDS.between(video.getCreateTime(), LocalDateTime.now()) % 60)));
        video.setPath(recording.getUrl());

        videoRepository.save(video);

        //STT
        try {
            sttService.transcribeFile(video.getId());
            summaryService.getSummary(video.getId());
        } catch (Exception e) {
            log.info("STT ERROR : " + e);
        }

        // 라이브 종료 = 세션 종료
        redisTemplate.opsForHash().delete("OpenVidu_recording", dealId);
        redisTemplate.opsForHash().delete("OpenVidu_SessionId", dealId);
        redisTemplate.opsForHash().delete("OpenVidu_ConnectionId", dealId);

        return recording;

    }

    @Transactional
    @Override
    public void CheckRecording(LiveRecordingRes liveRecordingRes) {
        long dealId = liveRecordingRes.getDealId();

        Video video = videoRepository.findByDealId(dealId)
            .orElseThrow(() -> new BusinessException(ErrorCode.VIDEO_NOT_EXIST));

        List<String> timeLine = video.getTimeLine();
        String time = String.format("%02d",
            ChronoUnit.HOURS.between(video.getCreateTime(), LocalDateTime.now())) + ":"
            + String.format("%02d",
            (ChronoUnit.MINUTES.between(video.getCreateTime(), LocalDateTime.now())) % 60) + ":"
            + String.format("%02d",
            (ChronoUnit.SECONDS.between(video.getCreateTime(), LocalDateTime.now())) % 60);

        switch (liveRecordingRes.getStep()) {
            case 1:
                timeLine.add("1_" + time);
                break;
            case 2:
                timeLine.add("2_" + time);
                break;
            case 3:
                timeLine.add("3_" + time);
                break;
            case 4:
                timeLine.add("4_" + time);
                break;
            case 5:
                timeLine.add("5_" + time);
                break;
            case 6:
                timeLine.add("6_" + time);
                break;
        }

        videoRepository.save(video);

    }

    @Override
    @Transactional
    public void EndLive(long dealId) {
        Purchase purchase = purchaseRepository.findById(dealId)
            .orElseThrow(() -> new BusinessException(ErrorCode.GET_PURCHASE_FAIL));
        purchase.setStatus(DealStatus.END);
        purchaseRepository.save(purchase);
    }

    @Override
    public List<Video> GetLiveRecord(long dealId) {
        List<Video> videos = videoRepository.findAllByDealId(dealId);
        return videos;
    }

}