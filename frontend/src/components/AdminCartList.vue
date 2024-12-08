<script setup>
import AdminCart from "@/components/AdminCart.vue";
defineProps({
  items: Array
})
const emit = defineEmits(["removeItem"])
</script>

<template>
  <div class="grid xl:grid-cols-4 gap-5 lg:grid-cols-3 md:grid-cols-2">
    <AdminCart
      v-for="item in items"
      :key="item.id"
      :img-url="item.imgUrl"
      :title="item.name"
      :price="item.price"
      @delete-clicked="() => emit('removeItem', item)"
    />
  </div>
</template>
