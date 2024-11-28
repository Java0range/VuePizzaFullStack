<script setup>
import { inject } from 'vue'
defineProps({
  totalPrice: Number
})
const { drawerOpen } = inject('drawerActions')
</script>

<template>
  <header class="flex justify-between border-b border-slate-300 px-8 py-5">
    <div class="flex align-center gap-4">
      <img src="/logo.png" alt="logo" class="w-12 h-12" />
      <div>
        <h2 class="text-xl font-bold uppercase">Vue Pizza</h2>
        <p class="text-slate-400">Лучшая пицерия</p>
      </div>
    </div>
    <ul class="flex items-center gap-4" @click="drawerOpen">
      <li
        class="flex items-center gap-3 text-gray-500 hover:text-black cursor-pointer transition"
      >
        <img src="/cart.svg" alt="cart" />
        <span>{{ totalPrice }} ₽</span>
      </li>
    </ul>
  </header>
</template>
