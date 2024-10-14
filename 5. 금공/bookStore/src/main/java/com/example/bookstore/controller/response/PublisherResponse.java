package com.example.bookstore.controller.response;

import com.example.bookstore.domain.model.Publisher;
import lombok.Builder;
import lombok.Data;

import java.util.List;

public class PublisherResponse {
    @Data
    @Builder
    public static class ListElem{
        private Long id;
        private String name;

        public static ListElem of(Publisher publisher){
            return ListElem.builder()
                    .id(publisher.getId())
                    .name(publisher.getName())
                    .build();
        }
    }
}
