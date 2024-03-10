package com.d212.taiso.repository;

import com.d212.taiso.domain.Todo;
import com.d212.taiso.repository.search.TodoSearch;
import org.springframework.data.jpa.repository.JpaRepository;

public interface TodoRepository extends JpaRepository<Todo, Long>, TodoSearch {
}
