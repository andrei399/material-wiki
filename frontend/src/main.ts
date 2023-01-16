import { createApp } from 'vue'
import App from './App.vue'
// @ts-ignore
import router from './router'
// @ts-ignore
import store from './store'
import axios from './plugins/axios'
// @ts-ignore
import vuetify from './plugins/vuetify'
// @ts-ignore
import { loadFonts } from './plugins/webfontloader'
// import axios from 'axios';


loadFonts()


const app = createApp(App)
app.config.globalProperties.theme = "orange"
// app.config.globalProperties.$axios = axios
app.use(router)
app.use(store)
app.use(vuetify)
app.use(axios, {
  baseURL: 'http://localhost:8000',
})
app.mount('#app')