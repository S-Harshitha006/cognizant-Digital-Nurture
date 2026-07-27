<template>

<div class="container">

<h2>My Enrolled Courses</h2>

<div
v-for="course in store.enrolledCourses"
:key="course.id"
class="card"
>

<h3>{{ course.name }}</h3>

<p>{{ course.code }}</p>

<p>{{ course.credits }} Credits</p>

<button @click="store.unenroll(course.id)">
Remove
</button>

</div>

<h3>Total Credits : {{ store.totalCredits }}</h3>

</div>

</template>

<script setup>
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()
</script>

<style scoped>

.container{
    width:90%;
    margin:30px auto;
}

.card{
    background:white;
    margin:15px 0;
    padding:20px;
    border-radius:8px;
    box-shadow:0 2px 8px rgba(0,0,0,.15);
}

button{
    margin-top:10px;
    background:red;
    color:white;
    border:none;
    padding:8px 15px;
    border-radius:5px;
}

</style>