package com.d212.taiso.domain;

import jakarta.persistence.*;
import lombok.*;

import java.util.ArrayList;
import java.util.List;

@Entity
@Getter
@Table(name = "tbl_product")
@Builder
@AllArgsConstructor
@NoArgsConstructor
@ToString(exclude = "imageList")
// ToString -> 이 객체가 다른 객체와 연관관계를 맺던 아니면 지금처럼 엘리먼트 컬렉션을 맺던
// 이런 관계에서는 항상 ToString을 일단 빼놓고 생각
public class Product {

    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long pno;

    private String pname;

    private int price;

    private String pdesc;

    private boolean delFlag;

    // ElementCollection의 주의점: 엘리먼트 컬렉션은 엘리먼트 컬렉션 자체가 주인공이 되지 않는다는 점
    // ex. 상품의 이미지를 수정한다고 우리가 표현하는 것이 아니라
    // 상품정보를 수정한다고 함
    // 그래서 엔티티가 뭘 하냐면 엔티티에서 엘리먼트 컬렉션들을 처리하는 것을 해줌.
    // 관리할 것이 많아져서 매니투원으로 빼기도 함

    // 그냥 상품에서 상품 이미지까지 같이 관리하는구나라고 생각하면 됨.
    @ElementCollection
    @Builder.Default
    private List<ProductImage> imageList = new ArrayList<>();


    public void changePrice(int price) {
        this.price = price;
    }
    public void changeDesc(String desc){
        this.pdesc = desc;
    }
    public void changeName(String name){
        this.pname = name;
    }

    public void changeDel(boolean delFlag) {
        this.delFlag = delFlag;
    }

    public void addImage(ProductImage image) {
        // 사이즈에 따라서 알아서 순번 맞춰서 들어감
        image.setOrd(this.imageList.size());
        imageList.add(image);
    }
    // 이미지가 이미 문자열로 다 되어 있는 이미지가 있는데 그런 것들을 저장할 때
    public void addImageString(String fileName){
        ProductImage productImage = ProductImage.builder()
                .fileName(fileName)
                .build();
        addImage(productImage);
    }
    public void clearList() {
        this.imageList.clear();
    }
}




