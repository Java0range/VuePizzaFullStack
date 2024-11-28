<script setup>
import DrawerHead from '@/components/DrawerHead.vue'
import CardListitem from '@/components/CardListitem.vue'
import InfoBlock from '@/components/InfoBlock.vue'
defineProps({
  totalPrice: Number,
})
const emit = defineEmits(['createOrder'])
</script>

<template>
  <div class="fixed top-0 left-0 h-full w-full bg-black z-10 opacity-50"></div>
  <div class="fixed right-0 top-0 bg-white w-96 h-full z-20 p-8">
    <DrawerHead />
    <CardListitem />
    <InfoBlock v-if="!totalPrice"/>
    <div class="flex flex-col gap-3 mb-2 mt-4" v-if="totalPrice">
      <div class="flex">
        <span>Итого:</span>
        <div class="flex-1 border-b border-dashed"></div>
        <b>{{ totalPrice }} ₽</b>
      </div>
      <button
        :disabled="!totalPrice"
        @click="() => emit('createOrder')"
        class="bg-lime-500 w-full disabled:bg-slate-400 rounded-xl py-3 text-white hover:bg-lime-600 transition active:bg-lime-700 cursor-pointer"
      >
        Оформить заказ
      </button>
    </div>
  </div>
</template>
