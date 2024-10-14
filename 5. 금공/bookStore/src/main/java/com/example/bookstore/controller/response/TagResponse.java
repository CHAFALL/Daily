package com.example.bookstore.controller.response;

import com.example.bookstore.domain.model.Tag;
import lombok.Builder;
import lombok.Data;

@Data
@Builder
public class TagResponse {
    private Long id;
    private String name;

    public static TagResponse of(Tag tag){
        return TagResponse.builder()
                .id(tag.getId())
                .name(tag.getName())
                .build();
    }
}
