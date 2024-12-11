<script setup>
import axios from 'axios'
import { provide, ref } from 'vue'

const serverUrl = ref('http://77.223.99.133')

axios.defaults.baseURL = serverUrl.value

provide('serverUrl', { serverUrl })
</script>
<template>
  <router-view />
</template>
