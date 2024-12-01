package com.qzp.bid.domain.deal.sale.entity;

import com.qzp.bid.domain.deal.entity.Deal;
import com.qzp.bid.domain.deal.entity.DealStatus;
import jakarta.persistence.DiscriminatorValue;
import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.FetchType;
import jakarta.persistence.OneToOne;
import java.time.LocalDateTime;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;
import org.hibernate.annotations.ColumnDefault;

@Entity
@Getter
@Setter
@ToString
@NoArgsConstructor
@DiscriminatorValue("sale")
public class Sale extends Deal {

    private int immediatePrice;
    @OneToOne(fetch = FetchType.LAZY)
    private Bid highestBid;
    private int startPrice;
    private LocalDateTime endTime;
    @Enumerated(EnumType.STRING)
    private DealStatus status;
    private int liveRequestCount;
    @ColumnDefault("0")
    private Integer bidCount;
}
