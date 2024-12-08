<script setup>
import { inject } from 'vue'
const { serverUrl } = inject("serverUrl");
const emit = defineEmits(["closeClick"])
defineProps({
  id: Number,
  imgUrl: String,
  title: String,
  price: Number,
})
</script>

<template>
  <div class="flex items-center border border-slate-200 p-4 rounded-xl gap-3">
    <img :src="serverUrl + imgUrl" alt="pizza" class="w-16 h-16">
    <div class="flex flex-col w-full">
      <p>{{ title }}</p>
      <div class="flex justify-between mt-1">
        <b>{{ price }} ₽</b>
        <img src="/close.svg" @click="emit('closeClick')" alt="close" class="opacity-60 hover:opacity-100 cursor-pointer transition" />
      </div>
    </div>
  </div>
</template>
