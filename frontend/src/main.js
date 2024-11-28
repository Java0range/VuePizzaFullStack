import './assets/main.css'

import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'

import HomePage from './pages/HomePage.vue'
import AdminPanel from './pages/AdminPanel.vue'

const app = createApp(App)

const routes = [
  { path: '/', name: "Home", component: HomePage },
  { path: '/admin', name:"AdminPanel", component: AdminPanel },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

app.use(router)
app.mount('#app')
