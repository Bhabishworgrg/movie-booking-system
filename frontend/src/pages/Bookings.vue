<template>
	<div>
		<!-- Top Bar -->
		<div style="display: flex; justify-content: space-between; align-items: center; padding: 20px;">
			<h1>Bookings</h1>
			<div>
				<button @click="goToHome">Home</button>
			</div>
		</div>

		<!-- Bookings List -->
		<ul>
			<li v-for="booking in bookings" :key="booking.id" style="margin-bottom: 20px;"
				@click="goToBooking(booking.id)">
				<h3>{{ booking.showtime.movie.name }}</h3>
				<p><strong>Showtime:</strong> {{ booking.showtime.start_time }}</p>
			</li>
		</ul>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const bookings = ref([])
const router = useRouter()

onMounted(async () => {
	try {
		const token = localStorage.getItem('token')
		const user = JSON.parse(localStorage.getItem('user'))

		let res
		if (user.role === 'user') {
			res = await axios.get(`http://localhost:8000/api/v1/users/${user.sub}/bookings`, {
				headers: { Authorization: `Bearer ${token}` }
			})
		} else if (user.role === 'admin') {
			res = await axios.get('http://localhost:8000/api/v1/bookings', {
				headers: { Authorization: `Bearer ${token}` }
			})
		} else {
			alert('Please login to view bookings.')
			return
		}

		bookings.value = res.data.data
	} catch (err) {
		console.error(err)
		alert(err.response.data.detail)
	}
})

const goToHome = () => router.push('/')
const goToBooking = (id) => router.push(`/bookings/${id}`)
</script>