import { createRouter, createWebHistory } from 'vue-router';
import store from '@/store';

import HomeView from '../views/HomeView.vue';
import Login from '../views/Login.vue';
import SignUp from '../views/SignUp.vue';
import MyAccount from '../views/MyAccount.vue';
import Leaderboard from '../views/Leaderboard.vue';

// 后台
import TopicList from '../views/Topic/TopicList.vue';
import TopicDes from '@/views/Topic/TopicDes.vue';

//Ai
import LangChain from '../views/dashboard/Chat.vue';

//关于
import About from '../views/AboutView.vue'

const routes = [
  {
    path: '/home',
    name: 'home',
    component: HomeView,
    beforeEnter: (to, from, next) => {
      LoadCss(to)
      next();
    },
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    beforeEnter: (to, from, next) => {
      LoadCss(to)
      next();
    },
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp,
    beforeEnter: (to, from, next) => {
      LoadCss(to)
      next();
    },
  },
  {
    path: '/myaccount',
    name: 'MyAccount',
    component: MyAccount,
    beforeEnter: (to, from, next) => {
      LoadCss(to)
      next();
    },
    meta: {
      requireLogin: true,
    },
  },
  {
    path: '/leaderboard',
    name: 'Leaderboard',
    component: Leaderboard,
    beforeEnter: (to, from, next) => {
      LoadCss(to)
      next();
    },
    meta: {
      requireLogin: true,
    },
  },
  {
    path: '/TopicList',
    name: 'TopicList',
    component: TopicList,
    beforeEnter: (to, from, next) => {
      LoadCss(to)
      next();
    },
    meta: {
      requireLogin: true,
    },
  },
  {
    path: '/TopicList/TopicDes/:id',
    name: 'TopicDes',
    component: TopicDes,
    beforeEnter: (to, from, next) => {
      LoadCss(to)
      next();
    },
    meta: {
      requireLogin: true,
    },
  },
  {
    path: '/LangChain',
    name: 'LangChain',
    component: LangChain,
    beforeEnter: (to, from, next) => {
      LoadCss(to)
      next();
    },
    meta: {
      requireLogin: true,
    },
  },
  {
    path: '/About',
    name: 'About',
    component: About,
    beforeEnter: (to, from, next) => {
      LoadCss(to)
      next();
    },
    meta: {
      requireLogin: true,
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL || '/'),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/login');
  } else {
    next();
  }
});


function LoadCss(path){
  var filename
  if(path.path.includes('Setings')){
      
      filename="/Css/admin.css"
  }else{
      filename="/Css/user.css"
  }
  console.log(filename)
  const link = document.createElement('link')
  link.rel = 'stylesheet'
  link.href = filename
  document.head.appendChild(link)
}

export default router;