import { createRouter, createWebHistory } from 'vue-router'
import PingVue from '../components/PingVue.vue'
import DangDo from '../components/DangDo.vue'

const routes = [
    {
        path: '/ping',
        name: 'ping',
        component: PingVue
    },
    {
        path: '/',
        name: 'DangDo',
        component: DangDo
    },
]

const router = createRouter({
    history: createWebHistory('/'),
    routes,
})

export default router;