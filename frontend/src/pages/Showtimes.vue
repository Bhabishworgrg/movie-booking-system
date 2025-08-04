<template>
	<div>
		<!-- Top Bar -->
		<div style="display: flex; justify-content: space-between; align-items: center; padding: 20px;">
			<h1>Showtimes</h1>
			<div>
				<button @click="goToHome">Home</button>
				<button @click="goToCreateShowtime">Add Showtime</button>
			</div>
		</div>

		<!-- Showtimes List -->
		<ul>
			<li v-for="show in showtimes" :key="show.id" style="margin-bottom: 20px;" @click="goToShowtime(show.id)">
				<h3>{{ show.movie.name }}</h3>
				<p><strong>Time:</strong> {{ show.start_time }}</p>
			</li>
		</ul>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const showtimes = ref([])
const router = useRouter()

onMounted(async () => {
	try {
		const res = await axios.get('http://localhost:8000/api/v1/showtimes')
		showtimes.value = res.data.data
	} catch (err) {
		alert(err.response.data.detail)
	}
})

const goToHome = () => router.push('/')
const goToCreateShowtime = () => router.push('/showtimes/create')
const goToShowtime = (id) => router.push(`/showtimes/${id}`)
</script>