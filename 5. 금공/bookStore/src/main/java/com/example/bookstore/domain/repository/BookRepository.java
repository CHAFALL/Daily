package com.example.bookstore.domain.repository;

import com.example.bookstore.domain.model.Book;
import org.springframework.data.jpa.repository.JpaRepository;

public interface BookRepository extends JpaRepository<Book, Long> {
}
