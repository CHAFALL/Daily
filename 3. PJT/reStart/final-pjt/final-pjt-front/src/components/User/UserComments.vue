<template>
  <div class="accordion">
    <div class="accordion-item">
      <div class="accordion-title" @click="showComments = !showComments">
        <h2>{{ user.username }}'s Comment</h2>
      </div>
      <transition name="slide-fade" appear>
        <div v-if="showComments" class="accordion-detail">
          <div v-if="paginatedComments && paginatedComments.length > 0">
            <div
              class="accordion-subItem"
              v-for="comment in paginatedComments"
              :key="comment.id"
            >
              <div @click="router.push({name: 'article', params:{id: comment.article.id}})" class="accordion-subTitle">
                {{ comment.content }} - {{ comment.article.title }}에 작성
              </div>
            </div>
            <!-- Pagination -->
            <div class="pagination">
              <button @click="changePage(page - 1)" class="next-prev" :disabled="page === 1">Prev</button>
              <span>Page {{ page }} of {{ totalPages }}</span>
              <button @click="changePage(page + 1)" class="next-prev" :disabled="page === totalPages">Next</button>
            </div>
          </div>
          <div v-else>
            <p>아직 작성한 댓글이 없습니다.</p>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
const router = useRouter()

const comments = ref(null)
const showComments = ref(false)
const page = ref(1)
const pageSize = 4

const props = defineProps({
  user: Object,
})

const fetchData = async () => {
  try {
    const response = await axios.get(`${userStore.API_URL}/api/v1/community/${props.user.username}/comments/`)
    comments.value = response.data
  } catch (error) {
    console.log(error)
  }
}

onMounted(fetchData)

watch(() => props.user, () => {
  fetchData()
  page.value = 1
})

const paginatedComments = ref([])
const totalPages = ref(1)

watch([comments, page], () => {
  if (comments.value) {
    const start = (page.value - 1) * pageSize
    const end = start + pageSize
    paginatedComments.value = comments.value.slice(start, end)
    totalPages.value = Math.ceil(comments.value.length / pageSize)
  }
})

const changePage = (newPage) => {
  if (newPage >= 1 && newPage <= totalPages.value) {
    page.value = newPage
  }
}
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
  align-items: center;
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
