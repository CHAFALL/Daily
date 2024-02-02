<template>
  <div class="flex justify-between">
    <GalleryFilter
      v-model:id="params.id_like"
      :limit="params._limit"
      @update:limit="changeLimit"
    >
    </GalleryFilter>

    <div class="flex items-center space-x-4">
      <AppDropdown>
        <template v-slot>
          <li onclick="gallery_create.showModal()">
            <a>open modal</a>
          </li>
          <li @click="goCreate"><a>사진 추가</a></li>
          <li @click="toggleDelete"><a>사진 삭제</a></li>
        </template>
      </AppDropdown>
    </div>
  </div>

  <AppGrid :items="folders">
    <template v-slot="{ item }">
      <p :id="item.id" @click="goList(folderName)">{{ item.id }}</p>
    </template>
  </AppGrid>

  <AppPagination
    :current-page="params._page"
    :page-count="pageCount"
    @page="page => (params._page = page)"
  />
</template>

<script setup>
import AppDropdown from '@/components/app/AppDropdown.vue';
import GalleryFilter from '@/components/gallery/GalleryFilter.vue';
import AppPagination from '@/components/app/AppPagination.vue';
import AppGrid from '@/components/app/AppGrid.vue';
import { ref, computed, watchEffect } from 'vue';
import { useRouter } from 'vue-router';
import { getFolders } from '@/utils/api/folders';

const router = useRouter();

const params = ref({
  _sort: 'createdAt', // 무엇을
  _order: 'desc', // 내림차순
  _limit: 6, // 몇개씩 조회
  _page: 1, // 현재 페이지를 조회
  id_like: '', // 해당 요소 검색 기능
});

const totalCount = ref(0);
const pageCount = computed(() =>
  Math.ceil(totalCount.value / params.value._limit),
);

const changeLimit = value => {
  params.value._limit = value;
  params.value._page = 1; // 갯수 제한이 바뀔 때마다 첫 페이지로 가도록
};

const folders = ref([]);

const fetchFolders = async () => {
  try {
    const { data, headers } = await getFolders(params.value);
    folders.value = data;
    totalCount.value = headers['x-total-count'];
    console.log('------------------');
    console.log(data);
  } catch (err) {
    console.err(err);
  }
};

// watchEffect는 watch와 동일하지만 처음에 한번 바로 실행해주는 점이 다름
// 이거는 폴더에서는 필요없을지도???
// onMounted로 대체 가능할 듯
watchEffect(fetchFolders);

// const folderName = '사물';

// 해당 폴더의 사진 리스트 보러가기
const goList = folderName => {
  router.push({
    name: 'GalleryList',
    params: {
      folderName,
    },
  });
};
</script>

<style lang="scss" scoped></style>
