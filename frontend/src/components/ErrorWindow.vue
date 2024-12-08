<script setup>
defineProps({
  widowClose: Function
})
</script>

<template>
  <div class="fixed top-0 left-0 h-full w-full bg-black z-10 opacity-50"></div>
  <div class="fixed top-28 left-1/2 -translate-x-1/2 rounded-3xl bg-white h-48 w-96 z-20 flex justify-center items-center gap-2 flex-col">
    <img src="/error.png" alt="error">
    <h3 class="text-lg">Ошибка</h3>
    <img @click="widowClose" src="/close.svg" alt="close" class="opacity-100 hover:shadow-xl cursor-pointer transition left-full -translate-x-12 top-1/4 -translate-y-8 fixed" />
  </div>
</template>
