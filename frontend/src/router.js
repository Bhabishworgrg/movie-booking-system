import { createRouter, createWebHistory } from 'vue-router'
import Home from './pages/Home.vue'
import Login from './pages/Login.vue'
import Register from './pages/Register.vue'
import Movies from './pages/Movies.vue'
import Showtimes from './pages/Showtimes.vue'

export default createRouter({
	history: createWebHistory(),
	routes: [
		{ path: '/', component: Home },
		{ path: '/login', component: Login },
		{ path: '/register', component: Register },
		{ path: '/movies', component: Movies },
		{ path: '/showtimes', component: Showtimes }
	]
})