package br.com.fujideia.iesp.tecback.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RequestMapping("/health")
@RestController
public class HealthController {

    @GetMapping
    public String health(){
        return "OK";
    }
    @PostMapping
    public String teste(){
        return "TEste";
    }
}
