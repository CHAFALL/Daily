package com.d212.taiso.service;

import com.d212.taiso.domain.Todo;
import com.d212.taiso.dto.PageRequestDTO;
import com.d212.taiso.dto.PageResponseDTO;
import com.d212.taiso.dto.TodoDTO;
import jakarta.transaction.Transactional;


@Transactional
public interface TodoService {

    TodoDTO get(Long tno);

    Long register(TodoDTO dto);

    void modify(TodoDTO dto);

    void remove(Long tno);


    PageResponseDTO<TodoDTO> getList(PageRequestDTO pageRequestDTO);

    default TodoDTO entityToDTO(Todo todo) {

        TodoDTO todoDto =
                TodoDTO.builder()
                        .tno(todo.getTno())
                        .title(todo.getTitle())
                        .content(todo.getContent())
                        .complete(todo.isComplete())
                        .dueDate(todo.getDueDate())
                        .build();
        return todoDto;
    }
    default Todo dtoToEntity(TodoDTO todoDto) {

        return Todo.builder()
                        .tno(todoDto.getTno())
                        .title(todoDto.getTitle())
                        .content(todoDto.getContent())
                        .complete(todoDto.isComplete())
                        .dueDate(todoDto.getDueDate())
                        .build();

    }
}
