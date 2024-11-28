<script setup>
  defineProps({
    imgUrl: String,
    title: String,
    price: Number,
    desc: Array,
    addClicked: Function,
    closeClicked: Function
  })
</script>

<template>
  <div class="fixed top-0 left-0 h-full w-full bg-black z-10 opacity-50"></div>
  <div class="fixed top-1/2 left-1/2 -translate-y-1/2 -translate-x-1/2 rounded-3xl bg-white xl:w-5/12 lg:w-2/4 md:w-3/4 sm:w-1/2 h-96 z-20 p-8">
    <div class="flex justify-between gap-6">
      <div class="flex gap-5">
        <img :src="imgUrl" alt="pizza" class="max-w-64">
        <ul class="list-disc marker:text-orange-400">
          <li v-for="item in desc" :key="item">
            {{ item }}
          </li>
        </ul>
      </div>
      <img src="/close.svg" @click="closeClicked" alt="close" class="opacity-100 hover:shadow-xl cursor-pointer transition left-full -translate-x-12 fixed" />
    </div>
    <p>{{ title }}</p>
    <div class="flex justify-between">
      <div class="flex flex-col">
        <span class="text-slate-400">Цена:</span>
        <b>{{ price }} ₽</b>
      </div>
      <button @click="addClicked" class="bg-orange-500 rounded-3xl text-white opacity-100 p-3 hover:opacity-85 transition">В корзину за {{ price }} ₽</button>
    </div>
  </div>
</template>
