package com.qzp.bid.domain.member.dto;

import java.util.List;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
public class ReviewListPage {

    private List<ReviewSimpleRes> reviewSimpleRes;
    private int pageNumber;
    private int pageSize;
    private boolean last; //다음 페이지 존재 여부
    private long total; //리뷰 전체 개수
}
