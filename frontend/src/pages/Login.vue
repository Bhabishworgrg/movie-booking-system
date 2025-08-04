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

		const token = res.data.data.token
		localStorage.setItem('token', token)
		axios.defaults.headers.common['Authorization'] = `Bearer ${token}`

		const payloadBase64 = token.split('.')[1]
		const decodedPayload = JSON.parse(atob(payloadBase64))
		localStorage.setItem('user', JSON.stringify(decodedPayload))

		alert(res.data.message)
		router.push('/')
	} catch (err) {
		console.error(err)
	}
}

const goToHome = () => router.push('/')
</script>