<template>

<div class="container">

    <h2>Available Courses</h2>

    <input
        v-model="searchTerm"
        placeholder="Search Course..."
        class="search"
    >

    <CourseCard
        v-for="course in filteredCourses"
        :key="course.id"
        :id="course.id"
        :name="course.name"
        :code="course.code"
        :credits="course.credits"
        :grade="course.grade"
    />

</div>

</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import CourseCard from '../components/CourseCard.vue'

const searchTerm = ref('')

const courses = ref([])

onMounted(() => {

    courses.value = [

        {
            id:1,
            name:'Angular',
            code:'CS301',
            credits:4,
            grade:'A'
        },

        {
            id:2,
            name:'React',
            code:'CS302',
            credits:3,
            grade:'A+'
        },

        {
            id:3,
            name:'Vue',
            code:'CS303',
            credits:4,
            grade:'A'
        },

        {
            id:4,
            name:'Python',
            code:'CS304',
            credits:5,
            grade:'B+'
        },

        {
            id:5,
            name:'Java',
            code:'CS305',
            credits:4,
            grade:'A'
        }

    ]

})

const filteredCourses = computed(() => {

    return courses.value.filter(course =>
        course.name
            .toLowerCase()
            .includes(searchTerm.value.toLowerCase())
    )

})

</script>

<style scoped>

.container{
    width:90%;
    margin:30px auto;
}

.search{
    width:100%;
    padding:12px;
    margin-bottom:20px;
    border:1px solid #ccc;
    border-radius:6px;
}

</style>