package com.example.bookstore.application;

import com.example.bookstore.controller.response.AuthorResponse;
import com.example.bookstore.domain.repository.AuthorRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class AuthorAppService {
    private final AuthorRepository authorRepository;

    public List<AuthorResponse.Detail> retrieveList() {
        return authorRepository.findAll().stream()
                .map(AuthorResponse.Detail::of).toList();
    }
}
