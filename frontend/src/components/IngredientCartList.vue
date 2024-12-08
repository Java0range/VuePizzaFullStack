<script setup>
import IngredientCart from '@/components/IngredientCart.vue'

const emit = defineEmits(["removeItem"])

defineProps({
  items: Array
})
</script>

<template>
  <div class="flex flex-col gap-1">
    <IngredientCart
      v-for="item in items"
      :key="item.id"
      :name="item.name"
      @delete-clicked="() => emit('removeItem', item)"
    />
  </div>
</template>
