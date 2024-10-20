package com.example.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@RestController
public class SlapController {
    @GetMapping("/slap")
    public Map<String, String> getBesos(
            @RequestParam(value = "slaps", defaultValue = "0") Long slaps,
            @RequestParam(value = "slapper", defaultValue = "jon") String slapper
    ) {
        Map<String, String> besos = new HashMap<>();
        besos.put("response", "you received "
                +slaps.toString()
                +" slaps by "
                +slapper
        );
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