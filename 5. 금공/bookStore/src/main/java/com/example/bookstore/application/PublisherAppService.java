package com.example.bookstore.application;

import com.example.bookstore.controller.response.PublisherResponse;
import com.example.bookstore.domain.repository.PublisherRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@RequiredArgsConstructor
@Service
public class PublisherAppService {
    private final PublisherRepository publisherRepository;

    public List<PublisherResponse.ListElem> retrieveList(){
        return publisherRepository.findAll().stream()
                .map(PublisherResponse.ListElem::of)
                .toList();
    }
}
