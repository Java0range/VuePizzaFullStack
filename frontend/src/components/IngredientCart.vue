<script setup>
const emit = defineEmits(["deleteClicked"])
defineProps({
  name: String
})
</script>

<template>
  <div class="bg-white flex justify-between items-center border-2 rounded-xl p-1">
    <p>{{ name }}</p>
    <img @click="emit('deleteClicked')" src="/delete.png" alt="delete" class="h-8 w-8 hover:shadow-xl cursor-pointer opacity-50 hover:opacity-100 transition" />
  </div>
</template>
