<template>
	<div>
		<!-- Top Bar -->
		<div style="display: flex; justify-content: space-between; align-items: center; padding: 20px;">
			<h1>Showtimes</h1>
			<div>
				<button @click="goToHome">Home</button>
			</div>
		</div>

		<!-- Showtimes List -->
		<ul>
			<li v-for="show in showtimes" :key="show.id" style="margin-bottom: 20px;">
				<h3>{{ show.movie_title }}</h3>
				<p><strong>Time:</strong> {{ show.time }}</p>
				<p><strong>Location:</strong> {{ show.location }}</p>
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
	const res = await axios.get('http://localhost:8000/api/v1/showtimes')
	showtimes.value = res.data
})

const goToHome = () => router.push('/')
</script>
