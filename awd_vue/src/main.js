import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import  {createI18n}  from 'vue-i18n'
import './assets/global.css'
import {VueFeatherIcons} from 'feather-icons'

axios.defaults.baseURL = 'http://127.0.0.1:8000'

const i18n = createI18n({
    locale: 'zh', // 设置默认语言
    messages: {
      'en': require('../language/en.json'), 
      'zh': require('../language/zh.json') 
    }
  })


createApp(App).use(store).use(i18n).use(router).use(VueFeatherIcons).mount('#app')



