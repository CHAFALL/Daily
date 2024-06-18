import {
  Injectable,
  InternalServerErrorException,
  NotFoundException,
} from '@nestjs/common';
import { CreatePostDto } from './dto/create-post.dto';
import { InjectRepository } from '@nestjs/typeorm';
import { Brackets, Repository, SelectQueryBuilder } from 'typeorm';
import { Post } from './post.entity';
import { User } from 'src/auth/user.entity';
import { Image } from 'src/image/image.entity';

@Injectable()
export class PostService {
  constructor(
    // post 엔티티 가져오기
    @InjectRepository(Post)
    private postRepository: Repository<Post>,
    @InjectRepository(Image)
    private imageRepository: Repository<Image>,
  ) {}

  async getAllMarkers(user: User) {
    try {
      const markers = await this.postRepository
        .createQueryBuilder('post')
        .where('post.userId = :userId', { userId: user.id })
        .select([
          'post.id',
          'post.latitude',
          'post.longitude',
          'post.color',
          'post.score',
        ])
        .getMany();

      return markers;
    } catch (error) {
      console.log(error);
      throw new InternalServerErrorException(
        '마커를 가져오는 도중 에러가 발생했습니다.',
      );
    }
  }

  // 이미지만 쏙 꺼내서 정렬
  private getPostsWithOrderImages(posts: Post[]) {
    return posts.map((post) => {
      const { images, ...rest } = post;
      // a.id - b.id가 0보다 작으면, a가 b보다 앞에 위치하게 됩니다.
      // a.id - b.id가 0보다 크면, a가 b보다 뒤에 위치하게 됩니다.
      // a.id - b.id가 0이면, a와 b의 순서는 변경되지 않습니다.
      const newImages = [...images].sort((a, b) => a.id - b.id);
      return { ...rest, images: newImages };
    });
  }

  private async getPostsBaseQuery(
    userId: number,
  ): Promise<SelectQueryBuilder<Post>> {
    return this.postRepository
      .createQueryBuilder('post')
      .leftJoinAndSelect('post.images', 'image')
      .where('post.userId = :userId', { userId })
      .orderBy('post.date', 'DESC');
  }

  // 'post.images': 이는 post 테이블과 images 테이블 간의 관계를 나타냅니다.
  // 'image': 이는 조인된 테이블(이미지 테이블)에 대해 사용할 별칭(alias)입니다. 이 별칭은 쿼리에서 선택된 데이터를 참조할 때 사용됩니다.

  async getPosts(page: number, user: User) {
    const perPage = 10;
    const offset = (page - 1) * perPage; // 페이지 번호에 따라 가져올 게시글의 시작 위치(오프셋)
    const queryBuilder = await this.getPostsBaseQuery(user.id);
    const posts = await queryBuilder
      .take(perPage) // 한번에 가져올 게시글의 수 설정
      .skip(offset) // 앞서 계산한 오프셋만큼 건너뜀
      .getMany(); // 포스트는 하나가 아니라 여러개이므로

    return this.getPostsWithOrderImages(posts);
  }

  // 포스트에서 개별 게시글을 가져올 때 즐겨찾기를 한 게시글인지 아닌지를 알 수 있도록.

  // leftJoinAndSelect: 선택된 결과에 포함(추가)시켜주는 느낌
  async getPostById(id: number, user: User) {
    try {
      const foundPost = await this.postRepository
        .createQueryBuilder('post')
        .leftJoinAndSelect('post.images', 'image')
        .leftJoinAndSelect(
          'post.favorites',
          'favorite',
          'favorite.userId = :userId',
          { userId: user.id },
        )
        .where('post.userId = :userId', { userId: user.id })
        .andWhere('post.id = :id', { id })
        .getOne();

      if (!foundPost) {
        throw new NotFoundException('존재하지 않는 피드입니다.');
      }

      // 즐겨찾기 여부만 추가로 보내주면 되므로
      const { favorites, ...rest } = foundPost;
      // 여부를 boolean 값으로 보내줌.
      const postWithIsFavorites = { ...rest, isFavorite: favorites.length > 0 };

      return postWithIsFavorites;
    } catch (error) {
      console.log(error);
      throw new InternalServerErrorException(
        '장소를 가져오는 도중 에러가 발생했습니다.',
      );
    }
  }

  async createPost(createPostDto: CreatePostDto, user: User) {
    const {
      latitude,
      longitude,
      color,
      address,
      title,
      description,
      date,
      score,
      imageUris,
    } = createPostDto;

    // post 생성 -> 여기까지만 하면 DB에 저장 x
    const post = this.postRepository.create({
      latitude,
      longitude,
      color,
      address,
      title,
      description,
      date,
      score,
      user,
    });

    const images = imageUris.map((uri) => this.imageRepository.create(uri));

    post.images = images;

    // 실제 DB에 저장
    try {
      await this.imageRepository.save(images);
      await this.postRepository.save(post);
    } catch (error) {
      console.log(error);
      throw new InternalServerErrorException(
        '장소를 추가하는 도중 에러가 발생했습니다.',
      );
    }

    // 만들어진 post 보내주기 (유저 빼고)

    const { user: _, ...postWithoutUser } = post;

    return postWithoutUser;
  }

  async deletePost(id: number, user: User) {
    try {
      const result = await this.postRepository
        .createQueryBuilder('post')
        .delete()
        .from(Post)
        .where('userId = :userId', { userId: user.id })
        .andWhere('id = :id', { id })
        .execute();
      // DB에 존재하지 않는 데이터라면
      if (result.affected === 0) {
        throw new NotFoundException('존재하지 않는 피드입니다.');
      }
      return id;
    } catch (error) {
      console.log(error);
      throw new InternalServerErrorException(
        '장소를 삭제하는 도중 에러가 발생했습니다.',
      );
    }
  }

  async updatePost(
    id: number,
    updatePostDto: Omit<CreatePostDto, 'latitude' | 'longitude' | 'address'>,
    user: User,
  ) {
    const post = await this.getPostById(id, user);
    const { title, description, color, date, score, imageUris } = updatePostDto;
    post.title = title;
    post.description = description;
    post.color = color;
    post.date = date;
    post.score = score;

    // image module
    const images = imageUris.map((uri) => this.imageRepository.create(uri));
    // 여기서 엮기겠구나.
    post.images = images;

    try {
      await this.imageRepository.save(images);
      await this.postRepository.save(post);
    } catch (error) {
      console.log(error);
      throw new InternalServerErrorException(
        '장소를 수정하는 도중 에러가 발생했습니다.',
      );
    }
    return post;
  }

  async getPostsByMonth(year: number, month: number, user: User) {
    const posts = await this.postRepository
      .createQueryBuilder('post')
      .where('post.userId = :userId', { userId: user.id })
      .andWhere('extract(year from post.date) = :year', { year })
      .andWhere('extract(month from post.date) = :month', { month })
      .select([
        'post.id AS id',
        'post.title AS title',
        'post.address AS address',
        'EXTRACT(DAY FROM post.date) AS date',
      ])
      .getRawMany();

    const groupPostsByDate = posts.reduce((acc, post) => {
      const { id, title, address, date } = post;

      // date를 키로 하고 값을 배열로 하는 형식으로 변환

      if (!acc[date]) {
        acc[date] = [];
      }
      acc[date].push({ id, title, address });

      return acc;
    }, {});

    return groupPostsByDate;
  }

  async searchMyPostsByTitleAndAddress(
    query: string,
    page: number,
    user: User,
  ) {
    const perPage = 10;
    const offset = (page - 1) * perPage;
    const queryBuilder = await this.getPostsBaseQuery(user.id);
    const posts = await queryBuilder
      .andWhere(
        new Brackets((qb) => {
          qb.where('post.title like :query', { query: `%${query}%` });
          qb.orWhere('post.address like :query', { query: `%${query}%` });
        }),
      )
      .skip(offset)
      .take(perPage)
      .getMany();

    return this.getPostsWithOrderImages(posts);
  }
}

// 각 컨트롤러 메서드에 따라 해당하는 DB 작업 등의 로직이 들어감.
// 서비스에 정의하는 메서드를 컨트롤러에 연결해 줄 것임.
// 서비스를 사용하기 위해서 서비스를 컨트롤러에서 주입시켜서 사용.

// 서비스에서도 레퍼지토리라는 것을 이용해서 DB에 저장 가능
