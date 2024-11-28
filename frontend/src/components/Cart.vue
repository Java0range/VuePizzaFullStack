<script setup>
  defineProps({
    imgUrl: String,
    title: String,
    price: Number,
    desc: String,
    bigCartOpen: Function
  })
</script>

<template>
  <div class="relative bg-white border border-slate-100 rounded-3xl p-8 cursor-pointer hover:-translate-y-2 hover:shadow-xl transition" @click="bigCartOpen">
    <img :src="imgUrl" alt="pizza">
    <p>{{ title }}</p>
    <div class="flex justify-between">
      <div class="flex flex-col">
        <span class="text-slate-400">Цена:</span>
        <b>{{ price }} ₽</b>
      </div>
    </div>
  </div>
</template>
