<template>

<div class="container">

    <h2>{{ course.name }}</h2>

    <p><strong>Code:</strong> {{ course.code }}</p>

    <p><strong>Credits:</strong> {{ course.credits }}</p>

    <p><strong>Grade:</strong> {{ course.grade }}</p>

    <button @click="enrollCourse">
        Enroll
    </button>

</div>

</template>

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { useEnrollmentStore } from '../stores/enrollment'

const route = useRoute()
const router = useRouter()
const store = useEnrollmentStore()

const courses = [

    {id:1,name:'Angular',code:'CS301',credits:4,grade:'A'},
    {id:2,name:'React',code:'CS302',credits:3,grade:'A+'},
    {id:3,name:'Vue',code:'CS303',credits:4,grade:'A'},
    {id:4,name:'Python',code:'CS304',credits:5,grade:'B+'},
    {id:5,name:'Java',code:'CS305',credits:4,grade:'A'}

]

const course =
    courses.find(c => c.id == route.params.id)

function enrollCourse(){

    store.enroll(course)

    router.push('/profile')

}
</script>

<style scoped>

.container{
    width:80%;
    margin:40px auto;
}

button{
    margin-top:20px;
    padding:12px 20px;
    border:none;
    background:#1976d2;
    color:white;
    border-radius:6px;
    cursor:pointer;
}

</style>