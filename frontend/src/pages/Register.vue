<template>
	<div style="display: flex; justify-content: space-between; align-items: center; padding: 20px;">
		<div>
			<h2>Register</h2>
			<form @submit.prevent="register">
				<input v-model="username" placeholder="Username" required />
				<input v-model="email" placeholder="Email" required />
				<input v-model="password" type="password" placeholder="Password" required />
				<button type="submit">Register</button>
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

const username = ref('')
const email = ref('')
const password = ref('')
const router = useRouter()

const register = async () => {
	try {
		const res = await axios.post('http://localhost:8000/api/v1/auth/register', {
		    username: username.value,
		    email: email.value,
		    password: password.value
		})
		alert(res.data.message)
		router.push('/login')
	} catch (err) {
		alert(err.response.data.detail)
	}
}

const goToHome = () => router.push('/')
</script>