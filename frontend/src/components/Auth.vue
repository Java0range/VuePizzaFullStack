<script setup>
import { ref } from 'vue'

const emit = defineEmits(["auth"])

const User = ref({
  username: "",
  password: ""
})
</script>

<template>
  <div class="flex items-center justify-center">
    <div
      class="bg-white mt-48 rounded-2xl h-96 flex justify-center items-center flex-col gap-3 xl:w-1/3 max-xl:w-2/4 max-md:w-full"
    >
      <h2 class="text-xl">Login</h2>
      <form class="max-w-sm">
        <div class="flex">
          <span
            class="inline-flex items-center px-3 text-sm text-gray-900 bg-white border border-e-0 border-gray-300 rounded-s-md"
          >
            <svg
              class="w-4 h-4 text-gray-500 dark:text-gray-400"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="currentColor"
              viewBox="0 0 20 20"
            >
              <path
                d="M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm0 5a3 3 0 1 1 0 6 3 3 0 0 1 0-6Zm0 13a8.949 8.949 0 0 1-4.951-1.488A3.987 3.987 0 0 1 9 13h2a3.987 3.987 0 0 1 3.951 3.512A8.949 8.949 0 0 1 10 18Z"
              />
            </svg>
          </span>
          <input
            v-model="User.username"
            type="text"
            class="rounded-none rounded-e-lg bg-white border border-gray-300 text-gray-900 focus:ring-blue-500 focus:outline-none focus:border-blue-500 block flex-1 min-w-0 w-full text-sm p-2.5"
            placeholder="Username"
          />
        </div>
      </form>
      <form class="max-w-sm">
        <div class="flex">
          <span
            class="inline-flex items-center px-3 text-sm border border-e-0 rounded-s-md bg-white text-gray-400 border-gray-300"
          >
            <svg
              class="w-4 h-4 text-gray-400"
              xmlns="http://www.w3.org/2000/svg"
              aria-hidden="true"
              fill="currentColor"
              viewBox="0 0 20 20"
            >
              <path
                d="M 12 1 C 8.6761905 1 6 3.6761905 6 7 L 6 8 C 4.9 8 4 8.9 4 10 L 4 20 C 4 21.1 4.9 22 6 22 L 18 22 C 19.1 22 20 21.1 20 20 L 20 10 C 20 8.9 19.1 8 18 8 L 18 7 C 18 3.6761905 15.32381 1 12 1 z M 12 3 C 14.27619 3 16 4.7238095 16 7 L 16 8 L 8 8 L 8 7 C 8 4.7238095 9.7238095 3 12 3 z M 12 13 C 13.1 13 14 13.9 14 15 C 14 16.1 13.1 17 12 17 C 10.9 17 10 16.1 10 15 C 10 13.9 10.9 13 12 13 z"
              ></path>
            </svg>
          </span>
          <input
            v-model="User.password"
            type="password"
            class="rounded-none rounded-e-lg bg-gray-50 border border-gray-300 text-gray-900 focus:ring-blue-500 focus:border-blue-500 focus:outline-none block flex-1 min-w-0 w-full text-sm p-2.5"
            placeholder="Password"
          />
        </div>
      </form>
      <button
        @click="() => emit('auth', User.username, User.password)"
        class="bg-lime-500 hover:bg-lime-400 text-white py-2 px-4 rounded-full"
      >
        Login
      </button>
    </div>
  </div>
</template>
