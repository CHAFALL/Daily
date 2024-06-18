// import * as fs from 'fs';
// import { diskStorage } from 'multer';
// import { extname, basename } from 'path';
import { AuthGuard } from '@nestjs/passport';
import { FilesInterceptor } from '@nestjs/platform-express';
import {
  Controller,
  Post,
  UploadedFiles,
  UseGuards,
  UseInterceptors,
} from '@nestjs/common';

import { numbers } from 'src/@common/constants';
import { PutObjectCommand, S3Client } from '@aws-sdk/client-s3';
import { getUniqueFileName } from 'src/@common/utils';

// 디렉토리로 저장하는 방식----------------------------------

// 디렉토리 확인 및 생성
// try {
//   fs.readdirSync('uploads');
// } catch (error) {
//   console.error('create uploads folder');
//   fs.mkdirSync('uploads');
// }

// @Controller('images')
// @UseGuards(AuthGuard())
// export class ImageController {
//   @UseInterceptors(
//     FilesInterceptor('images', numbers.MAX_IMAGE_COUNT, {
//       storage: diskStorage({
//         // destination: 파일이 저장될 디렉토리를 uploads/로 설정합니다.
//         destination(req, file, cb) {
//           cb(null, 'uploads/'); // 첫번째 인자는 에러
//         },
//         filename(req, file, cb) {
//           // 파일의 확장자 명 가져오기
//           const ext = extname(file.originalname);
//           cb(null, basename(file.originalname, ext) + Date.now() + ext);
//         },
//       }),
//       limits: { fileSize: numbers.MAX_IMAGE_SIZE },
//     }),
//   )
//   @Post('/')
//   uploadImages(@UploadedFiles() files: Express.Multer.File[]) {
//     const uris = files.map((file) => file.filename);

//     return uris;
//   }
// }

//  fs 모듈은 파일 시스템 조작, diskStorage는 Multer의 디스크 저장소 엔진, extname과 basename은 파일 경로와 이름을 다루기 위해 사용됩니다. AuthGuard는 인증을 위한 가드, FilesInterceptor는 파일 업로드를 처리하기 위한 인터셉터입니다.

// fs: 파일 시스템
// cb: 콜백

// 마지막으로 정적 컨텐츠를 사용하기 위해서는 서브 스태틱 모듈을 추가해줘야 한다. (app.module.ts에)

// ------------------------------------------------

@Controller('images')
@UseGuards(AuthGuard())
export class ImageController {
  @UseInterceptors(
    FilesInterceptor('images', numbers.MAX_IMAGE_COUNT, {
      limits: { fileSize: numbers.MAX_IMAGE_SIZE },
    }),
  )
  @Post('/')
  async uploadImages(@UploadedFiles() files: Express.Multer.File[]) {
    const s3Client = new S3Client({
      region: process.env.AWS_BUCKET_REGION,
      credentials: {
        accessKeyId: process.env.S3_ACCESS_KEY_ID,
        secretAccessKey: process.env.S3_SECRET_ACCESS_KEY,
      },
    });

    const uuid = Date.now();

    const uploadPromises = files.map((file) => {
      const fileName = getUniqueFileName(file, uuid);
      const uploadParams = {
        Bucket: process.env.AWS_BUCKET_NAME,
        Key: `original/${fileName}`,
        Body: file.buffer,
      };
      const command = new PutObjectCommand(uploadParams);

      return s3Client.send(command);
    });
    await Promise.all(uploadPromises);

    const uris = files.map((file) => {
      const fileName = getUniqueFileName(file, uuid);

      return `https://${process.env.AWS_BUCKET_NAME}.s3.${process.env.AWS_BUCKET_REGION}.amazonaws.com/original/${fileName}`;
    });

    return uris;
  }
}

// Promise.all()는 JavaScript에서 제공하는 Promise API의 메서드입니다. 이 메서드는 여러 개의 Promise를 동시에 실행하고, 모든 Promise가 완료될 때까지 기다린 후에 결과를 반환합니다.
