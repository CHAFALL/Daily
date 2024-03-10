package com.d212.taiso.config;

import com.d212.taiso.controller.formatter.LocalDateFormatter;
import lombok.extern.log4j.Log4j2;
import org.springframework.context.annotation.Configuration;
import org.springframework.format.FormatterRegistry;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
@Log4j2
public class CustomServletConfig implements WebMvcConfigurer {
    @Override
    public void addFormatters(FormatterRegistry registry) {

       log.info("-----------------------------------");
       log.info("addFormatters");

        registry.addFormatter(new LocalDateFormatter());
    }

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        // 모든 경로
        registry.addMapping("/**")
                .maxAge(500)
                //"OPTIONS"는 미리 한번 찔러볼 때 날라오는 방식이다
                .allowedMethods("GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS")
                // 어디에서 들어오는 연결을 허락?
                .allowedOrigins("*");


    }
}
