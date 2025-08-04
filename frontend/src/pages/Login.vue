<template>
	<div style="display: flex; justify-content: space-between; align-items: center; padding: 20px;">
		<div>
			<h2>Login</h2>
			<form @submit.prevent="login">
				<input v-model="email" placeholder="Email" required />
				<input v-model="password" type="password" placeholder="Password" required />
				<button type="submit">Login</button>
			</form>
		</div>
		<div>
			<button @click="goToHome">Home</button>
		</div>
	</div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const router = useRouter()

const login = async () => {
	try {
		const res = await axios.post('http://localhost:8000/api/v1/auth/login', {
			email: email.value,
			password: password.value
		})

		const token = res.data.access_token
		localStorage.setItem('token', token)
		axios.defaults.headers.common['Authorization'] = `Bearer ${token}`

		alert(res.data.message)
		router.push('/')
	} catch (err) {
		alert(err.response.data.detail)
	}
}

const goToHome = () => router.push('/')
</script>