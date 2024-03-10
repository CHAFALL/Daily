package com.d212.taiso.repository.search;

import com.d212.taiso.domain.Todo;
import com.d212.taiso.dto.PageRequestDTO;
import org.springframework.data.domain.Page;

public interface TodoSearch {

    Page<Todo> search1(PageRequestDTO pageRequestDTO);
}
