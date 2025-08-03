<script setup>
import { ref } from 'vue'
import axios from 'axios'

const username = ref('')
const email = ref('')
const password = ref('')
const loginEmail = ref('')
const loginPassword = ref('')
const token = ref('')

const register = async () => {
    try {
        await axios.post('http://localhost:8000/api/v1/auth/register', {
            username: username.value,
            email: email.value,
            password: password.value
        })
        alert('Registration successful! Please login.')
        username.value = ''
        email.value = ''
        password.value = ''
    } catch (err) {
        alert('Registration failed')
    }
}

const login = async () => {
    try {
        const res = await axios.post('http://localhost:8000/api/v1/auth/login', {
            email: loginEmail.value,
            password: loginPassword.value
        })
        token.value = res.data.access_token
        alert('Login successful!')
    } catch (err) {
        alert('Login failed')
    }
}
</script>

<template>
    <div>
        <h2>Register</h2>
        <form @submit.prevent="register">
            <input v-model="username" placeholder="Username" required />
            <input v-model="email" placeholder="Email" required />
            <input v-model="password" type="password" placeholder="Password" required />
            <button type="submit">Register</button>
        </form>

        <hr />

        <h2>Login</h2>
        <form @submit.prevent="login">
            <input v-model="loginEmail" placeholder="Email" required />
            <input v-model="loginPassword" type="password" placeholder="Password" required />
            <button type="submit">Login</button>
        </form>
    </div>
</template>