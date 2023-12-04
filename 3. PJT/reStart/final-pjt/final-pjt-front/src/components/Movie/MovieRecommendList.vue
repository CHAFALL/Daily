<template>
    <div class="wrapper">
      <carousel :autoplay="2000" :wrap-around="true" items-to-show='10'> <!-- items-to-show='15' -->
        <slide v-for="movie in movies" :key="movie.id">
            <div class="carousel__item">
              <img class="slideImg" :src="imgUrl + movie.poster_path" alt="" @click="router.push({name: 'movie', params: {id: movie.id}})">
            </div>
        </slide>
        <template #addons>
          <Navigation/>
        </template>
      </carousel>
    </div>
</template>


<script setup>

import { useRouter } from 'vue-router'
const router = useRouter()
const props = defineProps({
  movies: Object,
})

const imgUrl = 'https://image.tmdb.org/t/p/w185'

</script>

<script>
  import {Carousel, Slide, Navigation, Pagination} from 'vue3-carousel'
  import { defineComponent } from 'vue'
  
  import 'vue3-carousel/dist/carousel.css'

  export default defineComponent({
    name: 'Autoplay',
    components:{
      Carousel,
      Slide,
      Navigation,
    },
  })
</script>



<style>
.carousel__slide {
  padding: 5px;
}


.carousel__track {
  transform-style: preserve-3d;
}

.carousel__slide--sliding {
  transition: 0.5s;
}

.carousel__slide {
  opacity: 0.9;
  transform:  scale(0.8);
}

.carousel__slide--active ~ .carousel__slide {
  transform:  scale(0.8);
}

.carousel__slide--prev {
  opacity: 1;
  transform:  scale(0.9);
}

.carousel__slide--next {
  opacity: 1;
  transform:  scale(0.9);
}

.carousel__slide--active {
  opacity: 1;
  transform:  scale(1.1);
}

.carousel__item{
  border-radius: 8px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.carousel__slide {
  padding: 10px;
}

.carousel__prev,
.carousel__next {
  box-sizing: content-box;
  border: 3px solid white;
  border-radius: 10px;
  color: white;
  background-color: black;
}

.slideImg {
  width: auto;
  height: 300px;
  transform: scale(1.1);
}

.wrapper {
  margin-top: 3vh;
}

</style>