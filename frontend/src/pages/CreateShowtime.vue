<template>
	<div style="padding: 20px;">
		<h2>Create Showtime</h2>
		<form @submit.prevent="createShowtime">
			<div>
				<label>Start Time:</label>
				<input v-model="startTime" type="datetime-local" required />
			</div>
			<div>
				<label>Movie:</label>
				<select v-model="selectedMovieId" required>
					<option disabled value="">Select a movie</option>
					<option v-for="movie in movies" :key="movie.id" :value="movie.id">
						{{ movie.name }}
					</option>
				</select>
			</div>
			<button type="submit">Create</button>
			<button type="button" @click="goBack">Cancel</button>
		</form>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const startTime = ref('')
const selectedMovieId = ref('')

const movies = ref([])

const router = useRouter()

onMounted(async () => {
	try {
		const res = await axios.get('http://localhost:8000/api/v1/movies')
		movies.value = res.data.data || res.data // Adjust if backend wraps data inside `data`
	} catch (err) {
		alert('Failed to load movies')
	}
})

const createShowtime = async () => {
	try {
		const token = localStorage.getItem('token')

		await axios.post('http://localhost:8000/api/v1/showtimes', {
			start_time: startTime.value,
			movie_id: selectedMovieId.value
		}, {
			headers: { Authorization: `Bearer ${token}` }
		})

		alert('Showtime created successfully')
		router.push('/showtimes')
	} catch (err) {
		alert(err.response?.data?.detail || 'Failed to create showtime')
	}
}

const goBack = () => router.back()
</script>
