<script setup>
import axios from 'axios'
import { provide, ref } from 'vue'

const serverUrl = ref('http://192.168.0.15:8000')

axios.defaults.baseURL = serverUrl.value

provide('serverUrl', { serverUrl })
</script>
<template>
  <router-view />
</template>
