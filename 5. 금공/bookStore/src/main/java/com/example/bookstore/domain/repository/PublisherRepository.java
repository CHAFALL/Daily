package com.example.bookstore.domain.repository;

import com.example.bookstore.domain.model.Publisher;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PublisherRepository extends JpaRepository<Publisher, Long> {
}
