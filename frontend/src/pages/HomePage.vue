<script setup>
import { computed, onMounted, provide, ref, watch } from 'vue'
import axios from "axios";
import Header from "@/components/Header.vue";
import CardList from "@/components/CardList.vue";
import Drawer from "@/components/Drawer.vue";
import BigCart from '@/components/BigCart.vue'

const items = ref([]);
const itemBigCart = ref([])
const cartItems = ref([]);

const sortBy = ref("");

const drawerActive = ref(false);

const bigCartActive = ref(false);

const totalPrice = computed(
  () => cartItems.value.reduce((acc, item) => acc + item.price, 0)
)

const drawerOpen = () => {
  drawerActive.value = true;
}

const drawerClose = () => {
  drawerActive.value = false;
}
const bigCartOpen = (item) => {
  itemBigCart.value = item;
  bigCartActive.value = true;
}

const bigCartClose = () => {
  bigCartActive.value = false;
}
const addToCart = () => {
  cartItems.value.push(itemBigCart.value);
}
const removeToCart = (item) => {
  cartItems.value.splice(cartItems.value.indexOf(item), 1);
}
const createOrder = async () => {
  try {
    await axios.post("http://127.0.0.1:8000/orders", {
      items: cartItems.value,
      total_price: totalPrice.value
    })
    cartItems.value = []
  } catch (err) {
    console.log(err);
  }
}
provide("drawerActions", {
  cartItems,
  drawerOpen,
  drawerClose,
  removeToCart
});

const onChangeSort = (event) => {
  sortBy.value = event.target.value
}

onMounted(async () => {
  try {
    const { data } = await axios.get("http://127.0.0.1:8000/items/name")
    items.value = data;
  } catch (err) {
    console.log(err);
  }
  const localCart = localStorage.getItem("cartItems");
  cartItems.value = localCart ? JSON.parse(localCart) : [];
})

watch(sortBy, async () => {
  try {
    console.log(sortBy.value);
    const { data } = await axios.get("http://127.0.0.1:8000/items/" + sortBy.value);
    items.value = data;
    console.log(items.value);
  } catch (err) {
    console.log(err);
  }
})
watch(cartItems, () => {
  items.value = items.value.map((item) => ({
    ...item,
    isAdded: false,
  }))
})
watch(cartItems, () => {
  localStorage.setItem("cartItems", JSON.stringify(cartItems.value));
}, {deep: true})
</script>

<template>
  <div class="bg-white w-4/5 m-auto rounded-xl shadow-xl mt-14">
    <BigCart v-if="bigCartActive"
             :close-clicked="bigCartClose"
             :title="itemBigCart.name"
             :imgUrl="itemBigCart.imgUrl"
             :price="itemBigCart.price"
             :desc="itemBigCart.desc"
             :add-clicked="addToCart"
    />
    <Drawer v-if="drawerActive" :totalPrice="totalPrice" @create-order="createOrder" />
    <Header :total-price="totalPrice" />
    <div class="p-10">
      <div class="md:flex justify-between">
        <h2 class="text-3xl font-bold">Ассортимент</h2>
        <select @change="onChangeSort" class="px-3 py-2 border rounded-md outline-none">
          <option value="name">По названию</option>
          <option value="price">По цене(дешевые)</option>
          <option value="-price">По цене(дорогие)</option>
        </select>
      </div>
      <div class="mt-8">
        <CardList :items="items" @big-cart-open="bigCartOpen"/>
      </div>
    </div>
  </div>
</template>
