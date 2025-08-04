<template>
	<div>
		<!-- Top Bar -->
		<div style="display: flex; justify-content: space-between; align-items: center; padding: 20px;">
			<h1>Movies</h1>
			<div>
				<button @click="goToHome">Home</button>
				<button @click="goToCreateMovie">Add Movie</button>
			</div>
		</div>

		<!-- Movie List -->
		<ul>
			<li v-for="movie in movies" :key="movie.id" style="margin-bottom: 20px;" @click="goToMovie(movie.id)">
				<h3>{{ movie.name }}</h3>
			</li>
		</ul>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const movies = ref([])
const router = useRouter()

onMounted(async () => {
	try {
		const res = await axios.get('http://localhost:8000/api/v1/movies')
		movies.value = res.data.data
	} catch (err) {
		alert(err.response.data.detail)
	}
})

const goToHome = () => router.push('/')
const goToCreateMovie = () => router.push('/movies/create')
const goToMovie = (id) => router.push(`/movies/${id}`)
</script>