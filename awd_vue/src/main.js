import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import  {createI18n}  from 'vue-i18n'
import './assets/global.css'
import {VueFeatherIcons} from 'feather-icons'


let protocol=window.Location.protocol
let host=window.Location.host

axios.defaults.baseURL = "http://192.168.245.136:8000/"

const i18n = createI18n({
    locale: 'zh', // 设置默认语言
    messages: {
      'en': require('../language/en.json'), 
      'zh': require('../language/zh.json') 
    }
  })


createApp(App).use(store).use(i18n).use(router).use(VueFeatherIcons).mount('#app')



