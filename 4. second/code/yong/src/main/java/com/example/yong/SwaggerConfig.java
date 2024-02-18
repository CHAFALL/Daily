package com.example.yong;

import io.swagger.v3.oas.models.Components;
import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Info;
import io.swagger.v3.oas.models.security.SecurityRequirement;
import io.swagger.v3.oas.models.security.SecurityScheme;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpHeaders;
@Configuration

public class SwaggerConfig {
    @Bean
    public OpenAPI openAPI() {
        Info info = new Info()
                .title("BID 프로젝트 API Document")
                .version("v0.0.1")
                .description("BID 프로젝트의 API 명세서입니다.");

        // Security 요청 설정
        return new OpenAPI()

                .info(info);
    }
}