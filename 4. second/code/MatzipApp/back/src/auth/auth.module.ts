import { Module } from '@nestjs/common';
import { AuthController } from './auth.controller';
import { AuthService } from './auth.service';
import { User } from './user.entity';
import { TypeOrmModule } from '@nestjs/typeorm';
import { JwtModule } from '@nestjs/jwt';
import { JwtStrategy } from './jwt.strategy';
import { PassportModule } from '@nestjs/passport';

@Module({
  // 기능 확장 (다른 모듈에서 제공하는 기능을 가져와 사용할 수 있습니다. ), 의존성 관리(모듈 간의 의존성을 명시적으로 설정하여, 필요한 서비스와 기능을 모듈 내에서 사용할 수 있도록 합니다. 이를 통해 코드의 재사용성과 유지보수성을 높일 수 있습니다.), 모듈화
  imports: [
    PassportModule.register({ defaultStrategy: 'jwt' }),
    JwtModule.register({}),
    TypeOrmModule.forFeature([User]),
  ],
  controllers: [AuthController],
  // 서비스 등록, 전략 등록, 의존성 주입 관리를 해줌.
  providers: [AuthService, JwtStrategy],
  exports: [JwtStrategy, PassportModule],
})
export class AuthModule {}
