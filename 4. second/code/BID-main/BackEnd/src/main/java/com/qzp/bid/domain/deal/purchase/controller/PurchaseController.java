package com.qzp.bid.domain.deal.purchase.controller;

import com.qzp.bid.domain.deal.dto.SearchParam;
import com.qzp.bid.domain.deal.purchase.dto.ApplyFormReq;
import com.qzp.bid.domain.deal.purchase.dto.PurchaseListPage;
import com.qzp.bid.domain.deal.purchase.dto.PurchaseReq;
import com.qzp.bid.domain.deal.purchase.dto.PurchaseRes;
import com.qzp.bid.domain.deal.purchase.service.PurchaseService;
import com.qzp.bid.global.result.ResultCode;
import com.qzp.bid.global.result.ResultResponse;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import java.util.List;
import lombok.RequiredArgsConstructor;
import org.springdoc.core.annotations.ParameterObject;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestPart;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

@RestController
@RequestMapping("/deals/purchases")
@RequiredArgsConstructor
@Tag(name = "PurchaseController", description = "구매/역경매 api")
public class PurchaseController {

    private final PurchaseService purchaseService;

    @Operation(summary = "구매글 생성")
    @PostMapping(consumes = MediaType.MULTIPART_FORM_DATA_VALUE)
    public ResponseEntity<ResultResponse> createPurchase(@RequestPart PurchaseReq purchaseReq,
        @RequestPart List<MultipartFile> photos) {
        purchaseService.createPurchase(purchaseReq, photos);
        return ResponseEntity.status(HttpStatus.CREATED)
            .body(ResultResponse.of(ResultCode.CREATE_PURCHASE_SUCCESS));
    }

    @Operation(summary = "구매글 상세조회")
    @GetMapping("/{purchaseId}")
    public ResponseEntity<ResultResponse> getPurchase(@PathVariable Long purchaseId) {
        PurchaseRes purchaseRes = purchaseService.getPurchase(purchaseId);
        return ResponseEntity.ok(ResultResponse.of(ResultCode.GET_PURCHASE_SUCCESS, purchaseRes));
    }

    @Operation(summary = "구매글 삭제")
    @DeleteMapping("/{purchaseId}")
    public ResponseEntity<ResultResponse> deletePurchase(@PathVariable Long purchaseId) {
        purchaseService.deletePurchase(purchaseId);
        return ResponseEntity.ok(ResultResponse.of(ResultCode.DELETE_PURCHASE_SUCCESS));
    }

    @Operation(summary = "구매글 목록 조회")
    @GetMapping
    public ResponseEntity<ResultResponse> getPurchases(
        @ModelAttribute @ParameterObject SearchParam searchParam) {
        PurchaseListPage purchaseListPage = purchaseService.getPurchases(searchParam);
        return ResponseEntity.ok(
            ResultResponse.of(ResultCode.GET_PURCHASE_SUCCESS, purchaseListPage));
    }

    @Operation(summary = "역경매 참가 신청")
    @PostMapping(value = "/{purchasesId}/applyforms", consumes = MediaType.MULTIPART_FORM_DATA_VALUE)
    public ResponseEntity<ResultResponse> CreateApplyForm(@PathVariable Long purchasesId,
        @RequestPart ApplyFormReq applyFormReq, @RequestPart MultipartFile image) {
        purchaseService.createApplyForm(purchasesId, applyFormReq, image);
        return ResponseEntity.ok(ResultResponse.of(ResultCode.CREATE_APPLYFORM_SUCCESS));
    }
}
