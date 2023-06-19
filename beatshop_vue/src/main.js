import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import { AVPlugin } from 'vue-audio-visual'
import '@fortawesome/fontawesome-free/css/all.css';


axios.defaults.baseURL = 'http://127.0.0.1:8000'

const app = createApp(App).use(store).use(router, axios).use(AVPlugin).mount('#app')
