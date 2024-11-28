<script setup>
import Cart from "@/components/Cart.vue";
  defineProps({
    items: Array
})
const emit = defineEmits(["bigCartOpen"])
</script>

<template>
  <div class="grid xl:grid-cols-4 gap-5 lg:grid-cols-3 md:grid-cols-2">
    <Cart
      v-for="item in items"
      :key="item.id"
      :img-url="item.imgUrl"
      :title="item.name"
      :price="item.price"
      :big-cart-open="() => emit('bigCartOpen', item)"
    />
  </div>
</template>
