package com.qzp.bid.domain.deal.service;

public interface DealService {

    void addWish(long dealId);

    void deleteWish(long dealId);

    void auctionStartAlarm();
}