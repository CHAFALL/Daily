package com.example.bookstore.controller.response;

import com.example.bookstore.domain.model.Author;
import com.example.bookstore.domain.model.Book;
import lombok.Builder;
import lombok.Data;

import java.util.List;


public class BookResponse {
    @Data
    @Builder
    public static class ListElem{
        private Long id;
        private String title;
        private AuthorResponse.Detail author;

        public static ListElem of(Book book){
            return ListElem.builder()
                    .id(book.getId())
                    .title(book.getTitle())
                    .author(AuthorResponse.Detail.of(book.getAuthor()))
                    .build();
        }
    }

    @Data
    @Builder
    public static class Detail{
        private Long id;
        private String title;
        private int price;
        private PublisherResponse.ListElem publisher;
        private AuthorResponse.Detail author;


        public static Detail of(Book book){
            return Detail.builder()
                    .id(book.getId())
                    .title(book.getTitle())
                    .price(book.getPrice())
                    .publisher(PublisherResponse.ListElem.of(book.getPublisher()))
                    .author(AuthorResponse.Detail.of(book.getAuthor()))
                    .build();
        }
    }
}
