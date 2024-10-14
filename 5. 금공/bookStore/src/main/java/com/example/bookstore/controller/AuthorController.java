package com.example.bookstore.controller;

import com.example.bookstore.application.AuthorAppService;
import com.example.bookstore.controller.response.AuthorResponse;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/authors")
@RequiredArgsConstructor
public class AuthorController {
    private final AuthorAppService authorAppService;

    @GetMapping
    public List<AuthorResponse.Detail> retrieveList(){
        return authorAppService.retrieveList();
    }
}
