package com.d212.taiso.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.web.multipart.MultipartFile;

import java.util.ArrayList;
import java.util.List;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class ProductDTO {

    private Long pno;

    private String pname;

    private int price;

    private String pdesc;

    // 소프트 딜리트
    // 왜 이렇게 하냐? 얘와 걸리는 외래키가 많이 걸릴 것이므로
    // 얘가 없어진다면 작살남.(그래서 실제로 삭제를 하는 것이 아니라)
    //(삭제가 된 것처럼 표현)(회원도 보통 그렇게 함)

    private boolean delFlag;

    @Builder.Default
    private List<MultipartFile> files = new ArrayList<>();

    @Builder.Default
    private List<String> uploadFileNames = new ArrayList<>();
}
