package com.example.bookstore.controller;

import com.example.bookstore.application.BookAppService;
import com.example.bookstore.controller.request.BookRequest;
import com.example.bookstore.controller.response.BookResponse;
import com.example.bookstore.domain.repository.BookRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/books")
@RequiredArgsConstructor
public class BookController {
    private final BookAppService bookAppService;

    @GetMapping
    public List<BookResponse.ListElem> retrieveList(){
        return bookAppService.retrieveList();
    }

    @GetMapping("/{id}")
    public BookResponse.Detail retrieveDetail(@PathVariable Long id){
        return bookAppService.retrieveDetail(id);
    }

    @PostMapping
    public BookResponse.Detail createBook(@RequestBody BookRequest.Create request){
        return bookAppService.createBook(request);
    }

    @PutMapping("/{id}")
    public void modifyBook(@PathVariable Long id, @RequestBody BookRequest.Create reqeust){
        bookAppService.modifyBook(id, reqeust);
    }

    @DeleteMapping("/{id}")
    public void deleteBook(@PathVariable Long id){
        bookAppService.deleteBook(id);
    }

}
