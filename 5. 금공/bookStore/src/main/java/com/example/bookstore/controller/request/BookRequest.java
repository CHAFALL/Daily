package com.example.bookstore.controller.request;

import com.example.bookstore.domain.model.BookType;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

public class BookRequest {
    @Data
    @Builder
    public static class Create{
        private String title;
        private int price;
        private Long publisherId;
        private Long authorId;
    }
}
