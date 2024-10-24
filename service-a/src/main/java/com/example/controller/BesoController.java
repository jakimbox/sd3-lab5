package com.example.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@RestController
public class BesoController {
    @GetMapping("/besos")
    public Map<String, String> getBesos() {
        Map<String, String> besos = new HashMap<>();
        besos.put("ardiente", "fresa");
        besos.put("baboso", "mango");
        besos.put("mordisco", "manzana");
        besos.put("apretado", "uva");
        besos.put("sorpresa", "kiwi");
        besos.put("abierto", "cereza");
        return besos;
    }

    @GetMapping("/test")
    public Map<String,String> test(){
        Map<String, String> map = new HashMap<>();
        map.put("test", "hello, you successfully reached the service a");
        map.put("author", "this service was developed by Javier Grijalba");
        return map;
    }
}