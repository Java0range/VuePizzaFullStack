<script setup>
import { inject } from 'vue'
import CardItem from "@/components/CardItem.vue";

const { cartItems, removeToCart } = inject("drawerActions")
</script>

<template>
  <div class="flex flex-col gap-3">
    <CardItem
      v-for="item in cartItems"
      :key="item.id"
      :img-url="item.imgUrl"
      :title="item.name"
      :price="item.price"
      @close-click="() => removeToCart(item)"
    />
  </div>
</template>
