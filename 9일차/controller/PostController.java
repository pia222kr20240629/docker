package com.example.builletinboard.controller

import com.example.builletinboard.model.Post;
import com.example.builletinboard.repository.PorstRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("posts"){
	@Autowired
	private PostRepository postRepository;

	@GetMapping
	public List<Post> getAllPosts(){
		return postRepository.findAll();
	}

	@PostMapping
	public Post createPost(@RequestBody Post post){
		return postRepository.save(post);
	}
}
