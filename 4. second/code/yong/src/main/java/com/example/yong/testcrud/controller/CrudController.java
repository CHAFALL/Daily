package com.example.yong.testcrud.controller;


// 장고의 urls


import com.example.yong.testcrud.entity.Member;
import com.example.yong.testcrud.service.CrudService;
import com.example.yong.testcrud.service.CrudServiceImpl;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/crud")
@Slf4j
@RequiredArgsConstructor
public class CrudController {

    private final CrudServiceImpl crudService;


    @PostMapping("/save/member")
    public ResponseEntity<RuntimeException> SaveMember(@RequestParam(name = "name") String name){
        crudService.SaveMember(name);
        return ResponseEntity.ok(new RuntimeException("멤버 저장에 성공"));
    }

    @GetMapping("/get/{name}")
    public Member GetMember(@PathVariable(name = "name") String name){
        Member member = crudService.GetMember(name);
        return member;
    }

    @DeleteMapping("/delete/{name}")
    public ResponseEntity<RuntimeException> DeleteMember(@PathVariable(name = "name") String name){
        crudService.DeleteMemeber(name);
        return ResponseEntity.ok(new RuntimeException("멤버 삭제 성공"));
    }

    @PatchMapping("/update/{name}/{newName}")
    public ResponseEntity<RuntimeException> UpdateMember(@PathVariable(name = "name") String name, @PathVariable(name = "newName") String newName){
        crudService.UpdateMemeber(name, newName);
        return ResponseEntity.ok(new RuntimeException("멤버 삭제 성공"));
    }
}
