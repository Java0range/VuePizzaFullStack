<script setup>
import IngredientCartList from '@/components/IngredientCartList.vue'
import { ref } from 'vue'
import axios from 'axios'

const items = ref([])
const itemInput = ref("")
const selectedFile = ref("")
const nameItems = ref("")
const priceItem = ref("")

const props = defineProps({
  getItems: Function,
  closeClicked: Function,
  accessToken: String
})

const onFileChange = (e) => {
  selectedFile.value = e.target.files[0];
}

const createItem = async () => {
  try {
    const formData = new FormData();
    formData.append("upload_file", selectedFile.value);
    const headers = {
      headers: {
        token: props.accessToken
      }
    }
    const { data } = await axios.post("/upload", formData)
    const formDataItem = {
      name: nameItems.value,
      img: data,
      desc: items.value,
      price: priceItem.value,
      token: props.accessToken
    }
    await axios.post("/add/", formDataItem)
    props.getItems();
    props.closeClicked();
  } catch (err) {
    console.log(err);
  }
}

const addItem = () => {
  const item = {
    id: items.value.length + 1,
    name: itemInput.value,
  }
  items.value.push(item)
}
const removeItem = (item) => {
  items.value.splice(items.value.indexOf(item), 1)
}
</script>

<template>
  <div class="fixed top-0 left-0 h-full w-full bg-black z-10 opacity-50"></div>
  <div
    class="fixed top-1/2 left-1/2 -translate-y-1/2 -translate-x-1/2 rounded-3xl bg-white z-20 p-10 max-sm:w-full max-lg:w-3/4 w-1/3"
  >
    <img src="/close.svg" @click="closeClicked" alt="close" class="opacity-100 hover:shadow-xl cursor-pointer transition left-full -translate-x-12 top-6 fixed" />
    <div class="gap-2 flex flex-col">
      <h3>Название:</h3>
      <input
        v-model="nameItems"
        type="text"
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
      />
      <h3>Цена:</h3>
      <input
        v-model="priceItem"
        type="text"
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
      />
      <h3>Ингредиенты:</h3>
      <div class="flex">
        <input
          v-model="itemInput"
          type="text"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
        />
        <img
          src="/plus.svg"
          alt="plus"
          class="w-12 hover:shadow-xl cursor-pointer opacity-100 transition"
          @click="addItem"
        />
      </div>
      <IngredientCartList :items="items" @remove-item="removeItem" />
      <h3>Изображение:</h3>
      <input
        @change="onFileChange"
        type="file"
        class="mb-3 block w-full shadow-sm rounded-lg text-sm disabled:opacity-50 disabled:pointer-events-none bg-neutral-900 text-neutral-400 file:border-0 file:me-4 file:py-3 file:px-4 file:bg-lime-500 file:text-white"
      >
      <div class="flex justify-center">
        <button
          @click="createItem"
          class="bg-lime-500 hover:bg-lime-400 text-white py-2 px-4 rounded-full w-28"
        >
          Добавить
        </button>
      </div>
    </div>
  </div>
</template>
