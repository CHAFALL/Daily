package com.example.bookstore.controller;

import com.example.bookstore.application.PublisherAppService;
import com.example.bookstore.controller.response.PublisherResponse;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/publishers")
@RequiredArgsConstructor
public class PublisherController {
    private final PublisherAppService publisherAppService;
    @GetMapping
    public List<PublisherResponse.ListElem> retrieveList(){
        return publisherAppService.retrieveList();
    }
}
