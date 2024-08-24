package com.example.builletinboard.repository

import com.example.builletinboard.model.Post;
import org.springframework.data.jpa.repository.JpaRepository

public interface PostRepository extends JpaRepository<Post, Long>{
}
