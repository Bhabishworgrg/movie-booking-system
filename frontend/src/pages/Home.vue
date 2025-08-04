<template>
	<div>
		<!-- Top bar with heading and auth buttons -->
		<div style="display: flex; justify-content: space-between; align-items: center; padding: 20px;">
			<h1>Movie Booking System</h1>
			<div>
				<button @click="goToLogin" style="margin-right: 10px;">Login</button>
				<button @click="goToRegister">Register</button>
			</div>
		</div>

		<!-- Main action buttons -->
		<div style="text-align: center; margin-top: 100px;">
			<button @click="goToMovies" style="font-size: 24px; padding: 20px 40px; margin: 20px;">Browse Movies</button>
			<button @click="goToShowtimes" style="font-size: 24px; padding: 20px 40px; margin: 20px;">View Showtimes</button>
		</div>
	</div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goToLogin = () => router.push('/login')
const goToRegister = () => router.push('/register')
const goToMovies = () => router.push('/movies')
const goToShowtimes = () => router.push('/showtimes')
</script>