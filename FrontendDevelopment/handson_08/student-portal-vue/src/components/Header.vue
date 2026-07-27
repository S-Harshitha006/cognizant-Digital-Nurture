<template>
  <header class="header">
    <h2>🎓 Student Portal</h2>

    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/courses">Courses</RouterLink>
      <RouterLink to="/profile">
        Profile ({{ store.enrolledCourses.length }})
      </RouterLink>
    </nav>
  </header>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()
</script>

<style scoped>
.header{
    background:#1976d2;
    color:white;
    padding:18px 35px;

    display:flex;
    justify-content:space-between;
    align-items:center;
}

nav{
    display:flex;
    gap:25px;
}

a{
    color:white;
    text-decoration:none;
    font-weight:bold;
}

a:hover{
    color:#ffd54f;
}
</style>