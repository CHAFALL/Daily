package com.d212.taiso.controller;

import com.d212.taiso.dto.PageRequestDTO;
import com.d212.taiso.dto.PageResponseDTO;
import com.d212.taiso.dto.TodoDTO;
import com.d212.taiso.service.TodoService;
import lombok.RequiredArgsConstructor;
import lombok.extern.log4j.Log4j2;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@Log4j2
@RequiredArgsConstructor
@RequestMapping("/api/todo")
public class TodoController {

    // TodoService 주입
    private final TodoService todoService;

    @GetMapping("/{tno}")
    public TodoDTO get(@PathVariable("tno") Long tno) {
        return todoService.get(tno);
    }

    @GetMapping("/list")
    public PageResponseDTO<TodoDTO> list(PageRequestDTO pageRequestDTO) {
        log.info("list............." + pageRequestDTO);

        return todoService.getList(pageRequestDTO);
    }

    @PostMapping("/")

    // 리턴 값이 현재 Long타입으로 리턴하도록 되어있는데 제이슨으로 리턴해주는 것이 좋기 때문에 map 타입으로 바꿔서 리턴을 해줄것임

    // json 형식을 받으려면 @RequestBody가 필요 -> 그리고 json 파일을 TodoDto타입으로 받겠다!
    public Map<String, Long> register(@RequestBody TodoDTO dto) {
        log.info("todoDTO: " + dto);

        // 새로 만들어진 tno 값
        Long tno = todoService.register(dto);

        return Map.of("TNO", tno);
    }

    @PutMapping("/{tno}")
    public Map<String, String > modify(@PathVariable("tno") Long tno,
                                       @RequestBody TodoDTO todoDto) {
        todoDto.setTno(tno);

        todoService.modify(todoDto);

        return Map.of("RESULT", "SUCCESS");

    }

    @DeleteMapping("/{tno}")
    public Map<String, String> remove(@PathVariable Long tno) {
        todoService.remove(tno);

        return Map.of("RESULT", "SUCCESS");
    }
}
