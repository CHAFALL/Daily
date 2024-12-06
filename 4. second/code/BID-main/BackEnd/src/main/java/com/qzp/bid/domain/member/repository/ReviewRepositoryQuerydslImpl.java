package com.qzp.bid.domain.member.repository;

import com.querydsl.core.types.ExpressionUtils;
import com.querydsl.core.types.Projections;
import com.querydsl.jpa.JPAExpressions;
import com.querydsl.jpa.impl.JPAQueryFactory;
import com.qzp.bid.domain.member.dto.ReviewListPage;
import com.qzp.bid.domain.member.dto.ReviewSimpleRes;
import com.qzp.bid.domain.member.entity.QMember;
import com.qzp.bid.domain.member.entity.QReview;
import java.util.List;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Pageable;

@RequiredArgsConstructor
public class ReviewRepositoryQuerydslImpl implements ReviewRepositoryQuerydsl {

    private final JPAQueryFactory jpaQueryFactory;

    @Override
    public ReviewListPage getReviewListPageByWriterId(long reviewerId, Pageable pageable) {
        return getReviewListPageByMemberId(reviewerId, pageable, true);
    }

    @Override
    public ReviewListPage getReviewListPageByTargetId(long targetId, Pageable pageable) {
        return getReviewListPageByMemberId(targetId, pageable, false);
    }

    private ReviewListPage getReviewListPageByMemberId(long memberId, Pageable pageable,
        boolean isReviewer) {
        QReview review = QReview.review;
        QMember member = QMember.member;

        long total = jpaQueryFactory.select(review.count())
            .from(review)
            .where(isReviewer ? review.reviewerId.eq(memberId) : review.targetId.eq(memberId))
            .fetchOne();

        List<ReviewSimpleRes> reviewSimpleResList = jpaQueryFactory.select(Projections.fields(
                ReviewSimpleRes.class,
                review.id,
                review.content,
                review.score,
                review.createTime,
                review.role,

                ExpressionUtils.as(
                    JPAExpressions.select(member.nickname)
                        .from(member)
                        .where(member.id.eq(review.reviewerId)),
                    "reviewerNickname"
                ),
                ExpressionUtils.as(
                    JPAExpressions.select(member.nickname)
                        .from(member)
                        .where(member.id.eq(review.targetId)),
                    "tergetNickname"
                )
            ))
            .from(review)
            .where(isReviewer ? review.reviewerId.eq(memberId) : review.targetId.eq(memberId))
            .offset(pageable.getOffset())
            .limit(pageable.getPageSize() + 1)
            .orderBy(review.createTime.desc())
            .fetch();

        boolean hasNext = false;
        if (reviewSimpleResList.size() > pageable.getPageSize()) {
            reviewSimpleResList.remove(pageable.getPageSize());
            hasNext = true;
        }
        return new ReviewListPage(reviewSimpleResList, pageable.getPageNumber(),
            pageable.getPageSize(), !hasNext, total);
    }
}
