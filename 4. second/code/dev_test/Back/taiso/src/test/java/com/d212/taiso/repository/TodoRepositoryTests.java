package com.d212.taiso.repository;

import com.d212.taiso.domain.Todo;
import lombok.extern.log4j.Log4j2;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;

import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

@SpringBootTest
@Log4j2
public class TodoRepositoryTests {

    @Autowired
    private TodoRepository todoRepository;

    @Test
    public void test1() {
        Assertions.assertNotNull(todoRepository);

        log.info(todoRepository.getClass().getName());
    }

    @Test
    public void testInsert() {

        for (int i = 0 ; i < 100 ; i++) {

        Todo todo = Todo.builder()
                .title("Title"+ i)
                .content("Content..." + i)
                .dueDate(LocalDate.of(2023, 12, 30))
                .build();

        Todo result = todoRepository.save(todo);

        log.info(result);

        }

    }

    @Test
    public void testRead() {
        Long tno = 1L;

        Optional<Todo> result = todoRepository.findById(tno);

        // 문제 있으면 예외로 던지고 아니면 todo 끄집어 냄
        Todo todo = result.orElseThrow();

        log.info(todo);
    }

    @Test
    public void testUpdate() {
        // 먼저 로딩 하고 엔티티 객체를 변경 / setter

        // 가져오기
        Long tno = 1L;

        Optional<Todo> result = todoRepository.findById(tno);

        // 문제 있으면 예외로 던지고 아니면 todo 끄집어 냄
        Todo todo = result.orElseThrow();

        // 변경
        todo.changeTitle("Update Title");
        todo.changeContent("updated content");
        todo.changeComplete(true);

        todoRepository.save(todo);
    }

    @Test
    public void testPaging() {
        // page 번호는 0부터 시작함
        // Pageable import 때 조심
        Pageable pageable = PageRequest.of(0, 10, Sort.by("tno").descending());

        // 파라미터가 pageable이면 무조건 페이지 타입으로 나온다.
        // findAll 지정시(import) 조심
        Page<Todo> result = todoRepository.findAll(pageable);

        log.info(result.getTotalElements());

        // 전체 내용을 보고파
        log.info(result.getContent());
    }

//    @Test
//    public void testSearch1() {
//        todoRepository.search1();
//    }
}
