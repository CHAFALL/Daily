<template>
  <div class="navbar">
    <h1>{{ route.params.username }} 's Profile</h1>
    <div v-if="user">
      <button 
        v-if="userStore.user !== null && user.username !== userStore.user"
        @click="follow"
        class="follow-btn"
      >
        {{ isFollowing ? '팔로우 취소' : '팔로우' }}
      </button>
      <p style="font-size: 20px;">followers : {{ user.follower_count }}, followings : {{ user.following_count }} </p>
      <UserFollowing :user="user" :key="user.username" :followings="user.followings"/>
      <UserFollower :user="user" :key="user.username" :followers="user.followers"/>
      <UserArticles :user="user" :key="user.username"/>
      <UserComments :user="user" :key="user.username"/>
      <UserLikeArticles :user="user" :key="user.username"/>
      <UserLikeMovies :user="user" :key="user.username"/>
    </div>
  </div>
</template>

<script setup>
import UserFollower from '@/components/User/UserFollower.vue'
import UserFollowing from '@/components/User/UserFollowing.vue'
import UserArticles from '@/components/User/UserArticles.vue'
import UserComments from '@/components/User/UserComments.vue'
import UserLikeMovies from '@/components/User/UserLikeMovies.vue'
import UserLikeArticles from '@/components/User/UserLikeArticles.vue'
import { ref, onMounted, watch } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRoute } from 'vue-router'
import axios from 'axios'
const userStore = useUserStore()
const route = useRoute()
const user = ref(null)
const isFollowing = ref(false)


const fetchUserData = function () {
  axios({
    method: 'get',
    url: `${userStore.API_URL}/accounts/profile/${route.params.username}/`,
    headers: {
      Authorization: `Token ${userStore.token}`
    }
  })
    .then(res => {
      user.value = res.data
      for (const follower of res.data.followers) {
        if (follower.username === userStore.user) {
          isFollowing.value = true
        }
      }
    })
    .catch(err => console.log(err))
}


onMounted(() => {
  fetchUserData()
})

watch(() => route.params.username, () => {
  fetchUserData()
})

const follow = function () {
  axios({
    method: 'post',
    url: `${userStore.API_URL}/accounts/profile/${route.params.username}/followers/`,
    headers: {
      Authorization: `Token ${userStore.token}`
    }
  })
    .then(res => {
      isFollowing.value = res.data.isFollow
      user.value.follower_count = res.data.followerCount
      if (isFollowing.value) {
        user.value.followers.push({"username": userStore.user})
      } else {
        const idx = user.value.followers.findIndex(follower => follower.username === userStore.user)
        user.value.followers.splice(idx, 1)
      }
    })
    .catch(err => console.log(err))
}
</script>

<style scoped>
  .follow-btn {
  border: 3px solid lightgrey;
  background-color: white;
  height: 30px;
  font-size: 12px;
  margin-right: 0px;
  border-radius: 10px;
  transition: .4s;
}

.follow-btn:hover {
  background-color: lightgrey;
  transform: scale(1.1);
  color: white;
}
</style>