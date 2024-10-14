package com.example.bookstore.domain.model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Entity
@Getter
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class Tag {
    @Id @GeneratedValue
    private Long id;
    private String name;
    @ManyToOne
    private Book book;
}
