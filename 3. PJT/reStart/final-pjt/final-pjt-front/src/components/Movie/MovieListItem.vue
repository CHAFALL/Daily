<template>
  <div>
    <h3>{{ truncate(movie.title) }}</h3>
    <RouterLink :to="{ name: 'movie', params: { id: movie.id } }">
      <img :src="'https://image.tmdb.org/t/p/w185' + movie.poster_path" style="height: 280px;" alt="">
    </RouterLink>
    <div class="progress-bar">
      <div class="progress-bg"></div>
      <div :style="{ width: getProgressWidth(movie.vote_average).width }" :class="getProgressWidth(movie.vote_average).color"></div>
      <strong class="value" style="font-size: 14px; color: white; margin-left: -35px;">{{ (Math.round(movie.vote_average*100)/100).toFixed(2) }}</strong>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';

const props = defineProps({
  movie: Object,
});

const imgUrl = 'https://image.tmdb.org/t/p/w185';

const truncate = (text, length = 11, clamp = '...') => {
  return text.length > length ? text.slice(0, length) + clamp : text;
};

const getProgressWidth = (voteAverage) => {
  const width = ((voteAverage) / 10) * 100;
  let colorClass = 'gray';

  if (voteAverage > 7) {
    colorClass = 'green';
  } else if (voteAverage > 5) {
    colorClass = 'yellow';
  } else {
    colorClass = 'red';
  }

  return { width: `${width}%`, color: colorClass };
};
</script>

<style scoped>
.progress-bar {
  position: relative;
  width: 100%;
  height: 20px;
  margin-top: 10px;
  display: flex;
  background-color: #ffffff;
  border-radius: 10px;
  text-align: left;
}


.progress {
  height: 100%;

  transition: width 0.3s ease-in-out;
}

.red {
  background-color: rgb(95, 6, 6);
  border-radius: 10px;
}

.yellow {
  background-color: rgb(163, 185, 35);
  border-radius: 10px;
}

.green {
  background-color: rgb(30, 185, 30);
  border-radius: 10px;
}
</style>
