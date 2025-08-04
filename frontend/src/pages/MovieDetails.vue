<template>
	<div v-if="movie">
		<h1>{{ movie.name }}</h1>
		<p><strong>Duration:</strong> {{ movie.duration }} minutes</p>
		<p><strong>Description:</strong> {{ movie.description }}</p>

		<button @click="deleteMovie" v-if="isAdmin">
			Delete Movie
		</button>
		<button @click="goBack">Back</button>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const movie = ref(null)
const isAdmin = ref(false)

const token = localStorage.getItem('token')
if (token) {
	const decodedToken = JSON.parse(atob(token.split('.')[1]))
	isAdmin.value = decodedToken.role === 'admin'
}

onMounted(async () => {
	try {
		const res = await axios.get(`http://localhost:8000/api/v1/movies/${route.params.id}`)
		movie.value = res.data.data
	} catch (err) {
		alert(err.response.data.detail)
	}
})


const bookSeats = async () => {
	try {
		const token = localStorage.getItem('token')

		const booking_res = await axios.post('http://localhost:8000/api/v1/bookings', {
			movie_id: movie.value.id,
			seat_ids: selectedSeats.value,
		}, {
			headers: { Authorization: `Bearer ${token}` }
		})
		alert(booking_res.data.message)
		selectedSeats.value = []

		const movie_res = await axios.get(`http://localhost:8000/api/v1/movies/${route.params.id}`)
		movie.value = movie_res.data.data
	} catch (err) {
		alert(err.response.data.detail)
	}
}

const deleteMovie = async () => {
	try {
		const res = await
		axios.patch(`http://localhost:8000/api/v1/movies/${route.params.id}/archive`,
			{},
			{ headers: { Authorization: `Bearer ${token}` }}
		)
		alert(res.data.message)
		router.push('/movies')
	} catch (err) {
		alert(err.response.data.detail)
	}
}

const goBack = () => router.back()
</script>
