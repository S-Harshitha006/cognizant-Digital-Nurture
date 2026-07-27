<template>
  <div class="card">

    <h3>{{ name }}</h3>

    <p><strong>Code:</strong> {{ code }}</p>

    <p><strong>Credits:</strong> {{ credits }}</p>

    <p><strong>Grade:</strong> {{ grade }}</p>

    <RouterLink :to="'/courses/' + id">
      <button>View Details</button>
    </RouterLink>

  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  id: Number,
  name: String,
  code: String,
  credits: Number,
  grade: String
})
</script>

<style scoped>
.card{
    background:white;
    margin:15px 0;
    padding:20px;
    border-radius:10px;
    box-shadow:0 2px 8px rgba(0,0,0,.15);
}

button{
    margin-top:15px;
    padding:10px 18px;
    border:none;
    background:#1976d2;
    color:white;
    border-radius:5px;
    cursor:pointer;
}

button:hover{
    background:#1259a7;
}
</style>