import { createRouter, createWebHistory } from 'vue-router'

import Home from './pages/Home.vue'
import Login from './pages/Login.vue'
import Register from './pages/Register.vue'

import Movies from './pages/Movies.vue'
import CreateMovie from './pages/CreateMovie.vue'

import Showtimes from './pages/Showtimes.vue'
import CreateShowtime from './pages/CreateShowtime.vue'
import ShowtimeDetails from './pages/ShowtimeDetails.vue'

import Bookings from './pages/Bookings.vue'
import BookingDetails from './pages/BookingDetails.vue'

export default createRouter({
	history: createWebHistory(),
	routes: [
		{ path: '/', component: Home },
		{ path: '/login', component: Login },
		{ path: '/register', component: Register },
		{ path: '/movies', component: Movies },
		{ path: '/movies/create', component: CreateMovie },
		{ path: '/showtimes', component: Showtimes },
		{ path: '/showtimes/create', component: CreateShowtime },
		{ path: '/showtimes/:id', component: ShowtimeDetails },
		{ path: '/bookings', component: Bookings },
		{ path: '/bookings/:id', component: BookingDetails }
	]
})