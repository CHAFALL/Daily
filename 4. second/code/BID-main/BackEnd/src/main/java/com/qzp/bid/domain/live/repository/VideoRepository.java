package com.qzp.bid.domain.live.repository;

import com.qzp.bid.domain.live.entity.Video;
import java.util.List;
import java.util.Optional;
import org.springframework.data.jpa.repository.JpaRepository;

public interface VideoRepository extends JpaRepository<Video, Long> {

    Optional<Video> findByDealId(long dealId);

    List<Video> findAllByDealId(long dealId);
}
