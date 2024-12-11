<script setup>
import axios from 'axios'
import { provide, ref } from 'vue'

const serverUrl = ref('http://80.249.150.206')

axios.defaults.baseURL = serverUrl.value

provide('serverUrl', { serverUrl })
</script>
<template>
  <router-view />
</template>
