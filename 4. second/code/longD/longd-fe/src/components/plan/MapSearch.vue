<template>
  <div
    class="container max-h-[600px] border-2 border-red-200 rounded-lg overflow-y-auto"
  >
<<<<<<< HEAD
    <h2 class="ml-4 text-lg">
      ① 지도에서 장소 검색<br />
      ② 원하는 곳 하트 누르기<br />
      ③ '일정짜기'에서 여행계획 세우기
    </h2>
    <ul class="p-2">
      <li
        v-for="place in planStore?.searchResults"
        :key="place.place_id"
        class="mb-4 shadow-md rounded"
=======
    <h2 class="ml-4 text-lg">검색결과</h2>
    <ul class="p-4">
      <li
        v-for="place in planStore?.searchResults"
        :key="place.place_id"
        class="mb-4"
>>>>>>> 8495d94509e1a62cd0fceeba6fddf4986e70922f
      >
        <strong>{{ place.name }}</strong
        ><br />
        {{ place.address }}
        <button
          @click="planStore.addHopeList(place)"
          :class="{ 'text-red-500': planStore.isHeartSelected(place) }"
          class="text-2xl"
        >
          ❤
        </button>
      </li>
    </ul>
  </div>
<<<<<<< HEAD
=======

  <!-- 누르면 아래가 보이는 형태 ver -->
  <!-- <div class="collapse bg-base-200">
          <input type="checkbox" />
          <div class="collapse-title text-xl font-medium">
            <strong>{{ place.name }}</strong
            ><br />
            {{ place.address }}
          </div>
  
          <div class="collapse-content">
            <p>주소: {{ place.address }}</p>
            <p>위도: {{ place.geometry.location.lat() }}</p>
            <p>경도: {{ place.geometry.location.lng() }}</p>
          </div>
        </div> -->
>>>>>>> 8495d94509e1a62cd0fceeba6fddf4986e70922f
</template>

<script setup>
import { usePlanStore } from '@/stores/plan.js';
const planStore = usePlanStore();
</script>

<style scoped>
/* 스크롤바 커스터마이징 */
.container::-webkit-scrollbar {
  width: 12px; /* 스크롤바 너비 */
}

.container::-webkit-scrollbar-thumb {
  background-color: #f56868; /* 스크롤바 색상 */
  border-radius: 4px; /* 스크롤바 모양 */
}

.container::-webkit-scrollbar-track {
  background-color: #cbd5e0; /* 스크롤바 트랙 색상 */
}
</style>
