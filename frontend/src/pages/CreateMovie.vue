<template>
	<div style="padding: 20px;">
		<h2>Create Movie</h2>
		<form @submit.prevent="createMovie">
			<div>
				<label>Title:</label>
				<input v-model="name" required />
			</div>
			<div>
				<label>Duration (minutes):</label>
				<input v-model.number="duration" type="number" min="1" required />
			</div>
			<div>
				<label>Description:</label>
				<textarea v-model="description" required></textarea>
			</div>
			<button type="submit">Create</button>
			<button type="button" @click="goBack">Cancel</button>
		</form>
	</div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const name = ref('')
const duration = ref(90)
const description = ref('')

const router = useRouter()

const createMovie = async () => {
	try {
		const token = localStorage.getItem('token')

		const res = await axios.post('http://localhost:8000/api/v1/movies', {
			name: name.value,
			description: description.value,
			duration: duration.value
		}, {
			headers: { Authorization: `Bearer ${token}` }
		})

		alert(res.data.message)
		router.push('/movies')
	} catch (err) {
		alert(err.response.data.detail)
	}
}

const goBack = () => router.back()
</script>