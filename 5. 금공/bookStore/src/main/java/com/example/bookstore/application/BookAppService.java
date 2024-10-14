package com.example.bookstore.application;

import com.example.bookstore.controller.request.BookRequest;
import com.example.bookstore.controller.response.BookResponse;
import com.example.bookstore.domain.model.Author;
import com.example.bookstore.domain.model.Book;
import com.example.bookstore.domain.model.Publisher;
import com.example.bookstore.domain.repository.AuthorRepository;
import com.example.bookstore.domain.repository.BookRepository;
import com.example.bookstore.domain.repository.PublisherRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
@RequiredArgsConstructor
@Transactional
public class BookAppService {
    private final BookRepository bookRepository;
    private final PublisherRepository publisherRepository;
    private final AuthorRepository authorRepository;

    public List<BookResponse.ListElem> retrieveList(){
        return bookRepository.findAll().stream()
                .map(BookResponse.ListElem::of)
                .toList();
    }

    public BookResponse.Detail createBook(BookRequest.Create request) {
        Publisher publisher = publisherRepository.findById(request.getPublisherId())
                .orElseThrow();

        Author author = authorRepository.findById(request.getAuthorId())
                .orElseThrow();

        Book book = Book.builder()
                .title(request.getTitle())
                .price(request.getPrice())
                .author(author)
                .publisher(publisher)
                .build();

        bookRepository.save(book);

        return BookResponse.Detail.of(book);
    }

    public BookResponse.Detail retrieveDetail(Long id) {
        Book book = bookRepository.findById(id)
                .orElseThrow();

        return BookResponse.Detail.of(book);
    }

    public void modifyBook(Long id, BookRequest.Create reqeust) {
        Book book = bookRepository.findById(id)
                .orElseThrow();

        Publisher publisher = publisherRepository.findById(reqeust.getPublisherId())
                .orElseThrow();

        Author author = authorRepository.findById(reqeust.getAuthorId())
                .orElseThrow();

        book.setAuthor(author);
        book.setPublisher(publisher);
        book.setTitle(reqeust.getTitle());
        book.setPrice(reqeust.getPrice());
    }

    public void deleteBook(Long id) {
        Book book = bookRepository.findById(id)
                .orElseThrow();

        bookRepository.delete(book);
    }
}
