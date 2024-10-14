package com.example.bookstore.domain.model;

import jakarta.persistence.*;
import lombok.*;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;

@Entity
@Getter
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Setter
public class Book {
    @Id @GeneratedValue
    private Long id;
    private String title;
    private int price;
    @Enumerated(EnumType.STRING)
    private BookType type;
    @ManyToOne
    private Author author;
    @ManyToOne
    private Publisher publisher;
    @OneToMany(mappedBy = "book", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Tag> tags;
}
