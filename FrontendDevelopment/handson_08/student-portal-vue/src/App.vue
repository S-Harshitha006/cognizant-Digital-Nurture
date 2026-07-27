<template>
  <div>
    <Header />
    <RouterView />
  </div>
</template>

<script setup>
import Header from './components/Header.vue'
import { RouterView } from 'vue-router'
</script>

<style>
body{
  margin:0;
  font-family:Arial, Helvetica, sans-serif;
  background:#f4f6f9;
}

*{
  box-sizing:border-box;
}
</style>