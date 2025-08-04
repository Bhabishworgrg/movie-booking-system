<template>
	<div>
		<!-- Top bar with heading and auth buttons -->
		<div style="display: flex; justify-content: space-between; align-items: center; padding: 20px;">
			<h1>Movie Booking System</h1>
			<div v-if="user">
				<span>{{ user.username }}</span>
				<button @click="logout">Logout</button>
			</div>
			<div v-else>
				<button @click="goToLogin" style="margin-right: 10px;">Login</button>
				<button @click="goToRegister">Register</button>
			</div>
		</div>

		<!-- Main action buttons -->
		<div style="text-align: center; margin-top: 100px;">
			<button @click="goToMovies" style="font-size: 24px; padding: 20px 40px; margin: 20px;">Browse Movies</button>
			<button @click="goToShowtimes" style="font-size: 24px; padding: 20px 40px; margin: 20px;">View Showtimes</button>
		</div>
		<div style="text-align: center; margin-top: 100px;">
			<button @click="goToBookings" style="font-size: 24px; padding: 20px 40px; margin: 20px;">My Bookings</button>
		</div>
	</div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'

const router = useRouter()
const user = ref(null)

const goToLogin = () => router.push('/login')
const goToRegister = () => router.push('/register')
const goToMovies = () => router.push('/movies')
const goToShowtimes = () => router.push('/showtimes')
const goToBookings = () => router.push('/bookings')

const logout = () => {
	localStorage.removeItem('token')
	localStorage.removeItem('user')
	user.value = null
}

onMounted(() => {
	const storedUser = localStorage.getItem('user')
	if (storedUser) {
		user.value = JSON.parse(storedUser)
	}
})
</script>