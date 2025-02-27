import { createApp } from 'vue'
import App from './App.vue'
// router 추가하고 아래 .use(router)로 사용
import router from './router'
// bootstrap 사용
import 'bootstrap/dist/css/bootstrap.css'

createApp(App).use(router).mount('#app')
