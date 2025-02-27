import { createRouter, createWebHistory } from 'vue-router'
import PingVue from '../components/PingVue.vue'

const routes = [
    {
        path: '/ping',
        name: 'ping',
        component: PingVue
    },
]

const router = createRouter({
    history: createWebHistory('/'),
    routes,
})

export default router;