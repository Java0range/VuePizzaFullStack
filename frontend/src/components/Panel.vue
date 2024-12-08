<script setup>
import AdminCartList from '@/components/AdminCartList.vue'
import { onMounted, ref } from 'vue'
import axios from 'axios'
import AddPizza from '@/components/AddPizza.vue'

const items = ref([])
const createWindow = ref(false)

const openCreateWindow = () => {
  createWindow.value = true;
}

const closeCreateWindow = () => {
  createWindow.value = false
}

const deleteItem = async (item) => {
  try {
    const fromData = {
      name: item.name,
    }
    await axios.delete("/delete/", { data: fromData })
    getItems();
  } catch (err) {
    console.log(err);
  }
}

const getItems = async () => {
  try {
    const { data } = await axios.get("/items/name")
    items.value = data;
  } catch (err) {
    console.log(err);
  }
}

onMounted(async () => {
  try {
    const { data } = await axios.get("/items/name")
    items.value = data;
  } catch (err) {
    console.log(err);
  }
})
</script>
<template>
  <AddPizza v-if="createWindow" :close-clicked="closeCreateWindow" :get-items="getItems" />
  <div class="bg-white w-4/5 m-auto rounded-xl shadow-xl mt-14">
    <div class="p-10">
      <div class="flex justify-between p-4 items-center max-sm:flex-col max-sm:gap-2">
        <h2 class="text-3xl font-bold">Админ Панель</h2>
        <button
          class="bg-lime-500 hover:bg-lime-400 text-white py-2 px-4 rounded-full"
          @click="openCreateWindow"
        >
          Добавить
        </button>
      </div>
      <div class="mt-8">
        <AdminCartList :items="items" @remove-item="deleteItem" />
      </div>
    </div>
  </div>
</template>
