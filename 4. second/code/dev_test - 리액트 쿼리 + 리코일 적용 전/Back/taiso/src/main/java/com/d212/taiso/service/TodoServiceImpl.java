package com.d212.taiso.service;

import com.d212.taiso.domain.Todo;
import com.d212.taiso.dto.PageRequestDTO;
import com.d212.taiso.dto.PageResponseDTO;
import com.d212.taiso.dto.TodoDTO;
import com.d212.taiso.repository.TodoRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.log4j.Log4j2;
import org.springframework.data.domain.Page;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

// 서비스 계층에서 사실 제일 신경 써야 되는 것 중에 하나가
// 르랜잭션
// 트랜잭션에 대한 선언은 세 군데서 할 수 있다.
// 인터페이스, 클래스, 메소드 이렇게 3군데
// 우린 인터페이스에 할끼다

@Service
@Log4j2
// 의존성 주입을 받으면 그거에 맞는 생성자가 필요
@RequiredArgsConstructor
public class TodoServiceImpl implements TodoService{

    // 의존성 주입 받기
    private final TodoRepository todoRepository;

    @Override
    public TodoDTO get(Long tno) {

        Optional<Todo> result = todoRepository.findById(tno);

        Todo todo = result.orElseThrow();

        return entityToDTO(todo);
    }

    @Override
    public Long register(TodoDTO dto) {

        Todo todo = dtoToEntity(dto);

        Todo result = todoRepository.save(todo);

        return result.getTno();
    }

    @Override
    public void modify(TodoDTO dto) {

        Optional<Todo> result = todoRepository.findById(dto.getTno());

        Todo todo = result.orElseThrow();
        todo.changeTitle(dto.getTitle());
        todo.changeContent(dto.getContent());
        todo.changeComplete(dto.isComplete());
        todo.changeDueDate(dto.getDueDate());

        todoRepository.save(todo);

    }

    @Override
    public void remove(Long tno) {
        todoRepository.deleteById(tno);
    }

    @Override
    public PageResponseDTO<TodoDTO> getList(PageRequestDTO pageRequestDTO) {

        //JPA
        Page<Todo> result = todoRepository.search1(pageRequestDTO);

        // Todo List => TodoDTO List 로 변환 되어야 됨
        List<TodoDTO> dtoList = result.get()
                .map(todo -> entityToDTO(todo))
                .collect(Collectors.toList());

        PageResponseDTO<TodoDTO> responseDTO =
                PageResponseDTO.<TodoDTO>withAll()
                        .dtoList(dtoList)
                        .pageRequestDTO(pageRequestDTO)
                        .total(result.getTotalElements())
                        .build();


        return responseDTO;
    }
}
