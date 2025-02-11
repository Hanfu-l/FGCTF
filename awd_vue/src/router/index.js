import { createRouter, createWebHistory } from 'vue-router'
import store  from '@/store'

import HomeView from '../views/HomeView.vue'
import Login from '../views/Login.vue'
import SignUp from '../views/SignUp.vue'
import MyAccount from '../views/MyAccount.vue'
import Leaderboard from '../views/Leaderboard.vue'
import Notice from '../views/Notice.vue'


import Team from '../views/dashboard/Team.vue'
import JoinTeam from '../views/dashboard/JoinTeam.vue'

import Competition from '../views/competition/Competition.vue'
import AddCompetition from '../views/competition/AddCompetition.vue'
import CompetitionMenu from '../views/competition/CompetitionMenu.vue'

import AttackDefense from '../views/competition/AttackDefense.vue'

import Setings from '../views/dashboard/Setings.vue'
import SetUsers from '../views/dashboard/SetUsers.vue'
import SetTeams from '../views/dashboard/SetTeams.vue'
import Statistics from '../views/dashboard/Statistics.vue'
import SetCompetitions from '../views/dashboard/SetCompetitions.vue'
import EditCompetition from '../views/dashboard/EditCompetition.vue'
import CompetitionAndTopic from '../views/dashboard/CompetitionAndTopic.vue'
import SetTopics from '../views/dashboard/SetTopics.vue'
import CreateTopic from '../views/dashboard/CreateTopic.vue'
import SetNotice from '../views/dashboard/SetNotice.vue'
import CreateNotice from '../views/dashboard/CreateNotice.vue'

const routes = [
  {
    path: '/home',
    name: 'home',
    component: HomeView,
    beforeEnter: (to, from, next) => {
      // 在特定路由切换前执行的操作
      LoadCss(to)
      next()  // 继续路由切换
    },
  },
  {
    path: '/about',
    name: 'about',
    beforeEnter: (to, from, next) => {
      // 在特定路由切换前执行的操作
      LoadCss(to)
      next()  // 继续路由切换
    },
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    beforeEnter: (to, from, next) => {
      // 在特定路由切换前执行的操作
      LoadCss(to)
      next()  // 继续路由切换
    }
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp,
    beforeEnter: (to, from, next) => {
      // 在特定路由切换前执行的操作
      LoadCss(to)
      next()  // 继续路由切换
    }
  },
  {
    path: '/myaccount',
    name: 'MyAccount',
    component: MyAccount,
    beforeEnter: (to, from, next) => {
      // 在特定路由切换前执行的操作
      LoadCss(to)
      next()  // 继续路由切换
    },
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/team',
    name: 'Team',
    component: Team,
    beforeEnter: (to, from, next) => {
      // 在特定路由切换前执行的操作
      LoadCss(to)
      next()  // 继续路由切换
    },
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/leaderboard',
    name: 'Leaderboard',
    component: Leaderboard,
    beforeEnter: (to, from, next) => {
      // 在特定路由切换前执行的操作
      LoadCss(to)
      next()  // 继续路由切换
    },
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/notice',
    name: 'Notice',
    component: Notice,
    beforeEnter: (to, from, next) => {
      // 在特定路由切换前执行的操作
      LoadCss(to)
      next()  // 继续路由切换
    },
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/jointeam',
    name: 'JoinTeam',
    component: JoinTeam,
    beforeEnter: (to, from, next) => {
      // 在特定路由切换前执行的操作
      LoadCss(to)
      next()  // 继续路由切换
    },
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/competition',
    name: 'Competition',
    component: Competition,
    beforeEnter: (to, from, next) => {
      // 在特定路由切换前执行的操作
      LoadCss(to)
      next()  // 继续路由切换
    },
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/competitionmenu/:token',
    name: 'CompetitionMenu',
    component: CompetitionMenu,
    beforeEnter: (to, from, next) => {
      // 在特定路由切换前执行的操作
      LoadCss(to)
      next()  // 继续路由切换
    },
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/competition/attackdefense/:token',
    name: 'AttackDefense',
    component: AttackDefense,
    beforeEnter: (to, from, next) => {
      // 在特定路由切换前执行的操作
      LoadCss(to)
      next()  // 继续路由切换
    },
    meta: {
      requireLogin: true,
      isadmin:true
    }
  },
  {
    path: '/add_competition',
    name: 'AddCompetition',
    component: AddCompetition,
    beforeEnter: (to, from, next) => {
      // 在特定路由切换前执行的操作
      LoadCss(to)
      next()  // 继续路由切换
    },
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/Setings',
    name: 'Setings',
    component: Setings,
    beforeEnter: (to, from, next) => {
      // 在特定路由切换前执行的操作
      LoadCss(to)
      next()  // 继续路由切换
    },
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/Setings/Statistics',
    name: 'Statistics',
    component: Statistics,
    beforeEnter: (to, from, next) => {
      // 在特定路由切换前执行的操作
      LoadCss(to)
      next()  // 继续路由切换
    },
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/Setings/SetUsers',
    name: 'SetUsers',
    component: SetUsers,
    beforeEnter: (to, from, next) => {
      // 在特定路由切换前执行的操作
      LoadCss(to)
      next()  // 继续路由切换
    },
    meta: {
      requireLogin: true,
      isadmin:true
    }
  },
  {
    path: '/Setings/SetTeams',
    name: 'SetTeams',
    component: SetTeams,
    beforeEnter: (to, from, next) => {
      // 在特定路由切换前执行的操作
      LoadCss(to)
      next()  // 继续路由切换
    },
    meta: {
      requireLogin: true,
      isadmin:true
    }
  },
  {
    path: '/Setings/SetTopics',
    name: 'SetTopics',
    component: SetTopics,
    beforeEnter: (to, from, next) => {
      // 在特定路由切换前执行的操作
      LoadCss(to)
      next()  // 继续路由切换
    },
    meta: {
      requireLogin: true,
      isadmin:true
    }
  },
  {
    path: '/Setings/CreateTopic',
    name: 'CreateTopic',
    component: CreateTopic,
    beforeEnter: (to, from, next) => {
      // 在特定路由切换前执行的操作
      LoadCss(to)
      next()  // 继续路由切换
    },
  meta: {
    requireLogin: true,
    isadmin:true
  }
},
    {
      path: '/Setings/SetNotice',
      name: 'SetNotice',
      component: SetNotice,
      beforeEnter: (to, from, next) => {
        // 在特定路由切换前执行的操作
        LoadCss(to)
        next()  // 继续路由切换
      },
      meta: {
        requireLogin: true,
        isadmin:true
      }
    },
    {
      path: '/Setings/CreateNotice',
      name: 'CreateNotice',
      component: CreateNotice,
      beforeEnter: (to, from, next) => {
        // 在特定路由切换前执行的操作
        LoadCss(to)
        next()  // 继续路由切换
      },
    meta: {
      requireLogin: true,
      isadmin:true
    }
  },
  {
    path: '/Setings/SetCompetitions',
    name: 'SetCompetitions',
    component: SetCompetitions,
    beforeEnter: (to, from, next) => {
      // 在特定路由切换前执行的操作
      LoadCss(to)
      next()  // 继续路由切换
    },
    meta: {
      requireLogin: true,
      isadmin:true
    }
  },
  {
    path: '/Setings/EditCompetitions/:id',
    name: 'EditCompetition',
    component: EditCompetition,
    beforeEnter: (to, from, next) => {
      // 在特定路由切换前执行的操作
      LoadCss(to)
      next()  // 继续路由切换
    },
    meta: {
      requireLogin: true,
      isadmin:true
    }
  },
  {
    path: '/Setings/EditCompetitions/CompetitionAndTopic/:id',
    name: 'CompetitionAndTopic',
    component: CompetitionAndTopic,
    beforeEnter: (to, from, next) => {
      // 在特定路由切换前执行的操作
      LoadCss(to)
      next()  // 继续路由切换
    },
    meta: {
      requireLogin: true
    }
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
      next('/login')
  } else {
      next()
  }
})

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
export default router
