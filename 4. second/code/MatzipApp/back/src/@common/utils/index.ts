import { basename, extname } from 'path';

export function getUniqueFileName(file: Express.Multer.File, id: number) {
  // 확장자 명 받기
  const ext = extname(file.originalname);
  const fileName = basename(file.originalname, ext) + id + ext;

  return fileName;
}
