<template>
  <div class="flex justify-end">
    <div class="flex items-center space-x-4">
      <AppDropdown>
        <template v-slot>
          <li @click="folderCreate"><a>폴더 추가</a></li>
          <li @click="folderDelete"><a>폴더 삭제</a></li>
        </template>
      </AppDropdown>
    </div>
  </div>

  <GalleryFolderGrid :items="folders">
    <template v-slot="{ item }">
      <p :id="item.id" @click="goList(folderName)">{{ item.folderName }}</p>
    </template>
  </GalleryFolderGrid>
</template>

<script setup>
import AppDropdown from '@/components/app/AppDropdown.vue';
import GalleryFolderGrid from '@/components/gallery/GalleryFolderGrid.vue';
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { getFolders } from '@/utils/api/folders';
import Swal from 'sweetalert2';
import { createFolder } from '@/utils/api/folders';

const router = useRouter();

const params = ref({
  _sort: 'id', // 무엇을
  _order: 'desc', // 내림차순
});

const folderCreate = async () => {
  const { value: title } = await Swal.fire({
    title: '폴더 이름 작성',
    input: 'text',
    inputPlaceholder: '추가할 폴더 이름을 작성해주세요.',
    showCancelButton: true,
  });
  if (title) {
    Swal.fire('Saved!', '', 'success');
    try {
      console.log(title);
      await createFolder({ folderName: title });
      // 새로고침 해야 추가되는 현상있음
      router.push({ name: 'GalleryFolder' });
    } catch (error) {
      console.log(error);
    }
  }
};

const folders = ref([]);

const fetchFolders = async () => {
  try {
    const { data } = await getFolders(params.value);
    folders.value = data;
    console.log('------------------');
    console.log(data);
  } catch (err) {
    console.err(err);
  }
};

onMounted(() => {
  fetchFolders();
});

const folderName = '사물';

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
