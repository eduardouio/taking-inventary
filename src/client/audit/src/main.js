import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'

// booststrap
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'

// fontawesome
import "@fortawesome/fontawesome-free/css/all.min.css";
import "@fortawesome/fontawesome-free/js/all.min.js";
import './App.css';

createApp(App).mount('#app')
