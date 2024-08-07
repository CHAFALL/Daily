package com.qzp.bid.domain.deal.dto;

import com.qzp.bid.domain.deal.entity.Category;
import com.qzp.bid.domain.deal.entity.DealStatus;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.media.Schema.RequiredMode;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Schema(description = "검색 조건 파라미터")
public class SearchParam {

    @Schema(description = "페이지 번호", example = "0", defaultValue = "0", requiredMode = RequiredMode.REQUIRED)
    private int page;
    @Schema(description = "한 페이지 당 글 갯수", example = "10", defaultValue = "10", requiredMode = RequiredMode.REQUIRED)
    private int size;
    @Schema(description = "검색 카테고리 (ALL, FASHION, BEAUTY, CHILD, LIVING, DIGITAL, BOOK, TOY, PET, ETC)")
    private Category catg;
    @Schema(description = "검색 지역")
    private String area;
    @Schema(description = "정렬 (status와 함께 사용)  [최신순(desc) / 시작or마감 임박(asc) / 인기순(hot)]")
    private String order; // 기본 최신순 desc / 마감임박 or 시작임박  asc
    @Schema(description = "거래 진행 상태 (BEFORE, LIVE, AUCTION, END)")
    private DealStatus status;
    @Schema(description = "제목 검색 키워드")
    private String keyword;
}
