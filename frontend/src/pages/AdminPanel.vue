<script setup>
import Auth from '@/components/Auth.vue'
import { ref } from 'vue'
import Panel from '@/components/Panel.vue'
import axios from 'axios'
import ErrorWindow from '@/components/ErrorWindow.vue'
const authUser = ref(false)
const errorWindow = ref(false)
const errorWindowClose = () => {
  errorWindow.value = false
}
const auth =  async (username, password) => {
  try {
    const { data } = await axios.post("/auth/", {
      username: username,
      password: password,
    });
    if (data === "true") {
      authUser.value = true;
    } else {
      errorWindow.value = true;
    }
  } catch {
    errorWindow.value = true;
  }
}
</script>

<template>
  <Auth v-if="!authUser" @auth="auth"/>
  <Panel v-if="authUser"/>
  <ErrorWindow v-if="errorWindow" :widow-close="errorWindowClose"/>
</template>
