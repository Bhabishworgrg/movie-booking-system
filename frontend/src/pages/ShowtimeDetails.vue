<template>
	<div v-if="showtime">
		<h1>{{ showtime.movie.name }}</h1>
		<p><strong>Start Time:</strong> {{ showtime.start_time }}</p>
		<p><strong>Duration:</strong> {{ showtime.movie.duration }} minutes</p>
		<p><strong>Description:</strong> {{ showtime.movie.description }}</p>
		<h3>Seats</h3>
		<ul>
			<li v-for="seat in showtime.seats" :key="seat.id">
				<label v-if="!seat.is_booked">
					<input
							type="checkbox"
							:value="seat.id"
							v-model="selectedSeats"
							/>
					{{ seat.number }} (Available)
				</label>
				<span v-else>
					{{ seat.number }} (Booked)
				</span>
			</li>
		</ul>

		<button @click="bookSeats" :disabled="selectedSeats.length === 0">
			Book Selected Seats
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
const showtime = ref(null)
const selectedSeats = ref([])

onMounted(async () => {
	try {
		const res = await axios.get(`http://localhost:8000/api/v1/showtimes/${route.params.id}`)
		showtime.value = res.data.data
	} catch (err) {
		alert(err.response.data.detail)
	}
})


const bookSeats = async () => {
	try {
		const token = localStorage.getItem('token')

		const booking_res = await axios.post('http://localhost:8000/api/v1/bookings', {
			showtime_id: showtime.value.id,
			seat_ids: selectedSeats.value,
		}, {
			headers: { Authorization: `Bearer ${token}` }
		})
		alert(booking_res.data.message)
		selectedSeats.value = []

		const showtime_res = await axios.get(`http://localhost:8000/api/v1/showtimes/${route.params.id}`)
		showtime.value = showtime_res.data.data
	} catch (err) {
		alert(err.response.data.detail)
	}
}

const goBack = () => router.back()
</script>