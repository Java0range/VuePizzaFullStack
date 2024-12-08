<script setup>
import { inject } from 'vue'
const { serverUrl } = inject("serverUrl");
defineProps({
  imgUrl: String,
  title: String,
  price: Number,
})
const emit = defineEmits(["deleteClicked"])
</script>

<template>
  <div class="relative bg-white border border-slate-100 rounded-3xl p-8 cursor-pointer hover:-translate-y-2 hover:shadow-xl transition">
    <img :src="serverUrl + imgUrl" alt="pizza">
    <p>{{ title }}</p>
    <div class="flex justify-between">
      <div class="flex flex-col">
        <span class="text-slate-400">Цена:</span>
        <b>{{ price }} ₽</b>
      </div>
      <img @click="emit('deleteClicked')" src="/delete.png" alt="delete" class="h-9 w-9 hover:shadow-xl cursor-pointer opacity-50 hover:opacity-100 transition" />
    </div>
  </div>
</template>
