<script setup>
import Auth from '@/components/Auth.vue'
import { ref } from 'vue'
import Panel from '@/components/Panel.vue'
const auth = ref(false)
</script>

<template>
 <Auth v-if="!auth"/>
 <Panel v-if="auth"/>
</template>
