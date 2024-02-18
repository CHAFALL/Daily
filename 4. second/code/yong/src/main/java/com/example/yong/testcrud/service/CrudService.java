package com.example.yong.testcrud.service;


import com.example.yong.testcrud.entity.Member;

public interface CrudService {

    void SaveMember(String name);

    Member GetMember(String name);

    void DeleteMemeber(String name);

    void UpdateMemeber(String name, String newName);

}
