<template>
  <div class="accordion">
    <div class="accordion-item">
      <div class="accordion-title" @click="showFollowings = !showFollowings">
        <h2>{{ props.user.username }}'s Followings</h2>
      </div>
      <transition name="slide-fade" appear>
        <div v-if="showFollowings" class="accordion-detail">
          <div v-if="followings && followings.length > 0">
            <div
              class="accordion-subItem"
              v-for="following in followings"
              :key="following.username"
            >
              <div 
                @click="router.push({name: 'profile', params: {username: following.username}})" 
                class="accordion-subTitle"
              >
                {{ following.username }}
              </div>
            </div>
          </div>
          <div v-else>
            <p>아직 팔로잉하는 사람이 없습니다.</p>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const showFollowings = ref(false)
const props = defineProps({
  followings: Object,
  user: Object,
})
</script>

<style scoped>
.accordion {
  width: 80%;
  margin: 0 auto;
  font-family: 'Noto Sans KR', sans-serif;
  transition: 1ms;
}

.accordion-item {
  background: #282828;
  margin-bottom: .5rem;
  box-shadow: 0 .1rem 1rem -.5rem rgba(0,0,0,.4);
  border-radius: 5px;
  overflow: hidden;
}

.accordion-title{
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 1rem;
  background: #333;
  cursor: pointer;
  position: relative;
  height: 50px;
  font-family: 'Indie Flower', cursive;
  color: #fff;
}

.accordion-subTitle {
  padding: 1rem;
  background: #5c5c5c;
  cursor: pointer;
  position: relative;
  border-radius: 10px;
  margin-bottom: 3px;
}

.accordion-detail {
  padding: 1rem;
  background-color: #444;
  color: #fff;
  max-height: 300px;
  overflow-y: scroll;
}

.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: max-height .3s ease, opacity .5s ease;
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  max-height: 0;
  opacity: 0;
}

.slide-fade-enter-to,
.slide-fade-leave-from {
  max-height: 100vh;
  opacity: 1;
}

.pagination {
  display: flex;
  justify-content: center;
  margin-top: 1rem;
}

.pagination button {
  margin: 0 0.5rem;
  cursor: pointer;
}


.pagination span {
  margin: 0 0.5rem;
  font-weight: bold;
}

</style>