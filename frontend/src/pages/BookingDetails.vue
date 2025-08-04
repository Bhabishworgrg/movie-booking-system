<template>
	<div v-if="booking">
		<h1>{{ booking.showtime.movie.name }}</h1>
		<p><strong>Showtime:</strong> {{ booking.showtime.start_time }}</p>
		<p><strong>Booked At:</strong> {{ booking.booked_at }}</p>
		<p><strong>Seats:</strong> {{ booking.seats.map(seat => seat.number).join(', ') }}</p>
		<p><strong>Duration:</strong> {{ booking.showtime.movie.duration }} minutes</p>
		<p><strong>Status:</strong> {{ booking.cancelled_at ? 'Cancelled' : 'Booked' }}</p>
		<p v-if="booking.cancelled_at"><strong>Cancelled At:</strong> {{ booking.cancelled_at }}</p>

		<button @click="goBack">Back</button>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const booking = ref(null)

onMounted(async () => {
	try {
		const token = localStorage.getItem('token')

		const res = await axios.get(`http://localhost:8000/api/v1/bookings/${route.params.id}`, {
			headers: { Authorization: `Bearer ${token}` }
		})

		booking.value = res.data.data
	} catch (err) {
		alert(err.response.data.detail)
	}
})

const goBack = () => router.back()
</script>