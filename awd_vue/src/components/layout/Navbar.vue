<template>
<div>
    <template v-if="!$route.path.includes('/Setings')">
    <nav class="navbar is-black is-spaced">
        <div class="navbar-brand">
          <a class="navbar-item">
            
              <img src="../../assets/bulma-logo-white.png" width="112" height="28">
            
          </a>
        </div>
      
        <div  class="navbar-menu ">
          <div class="navbar-start">
            <router-link class="navbar-item" to="/home">
                {{ $t('navbar.Home') }}
            </router-link>
            <router-link class="navbar-item" to="/competition">
                {{ $t('navbar.Competition') }}
            </router-link>
            <router-link class="navbar-item" to="/team">
                {{ $t('navbar.Team') }}
            </router-link>
            
             <router-link class="navbar-item" to="/leaderboard">
                {{ $t('navbar.Leaderboard') }}
            </router-link>
             <router-link class="navbar-item" to="/notice">
                 {{ $t('navbar.Notice') }}
            </router-link>
          </div>
          <div class="navbar-end">
            <div class="navbar-item">
              <div class="field is-grouped">
                <template v-if="$store.state.isAuthenticated">
 
                    <template v-if="$store.state.isadmin">

                    <router-link class="text has-text-light mr-3"  to="Setings">
                        <span class="icon-text">
                            <span class="icon">
                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-tool">
                                    <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>
                                </svg>
                            </span>
                            <span>
                                <p>{{ $t('navbar.Setings') }}</p>
                            </span>
                        </span>
                    </router-link>

                    </template>



                    <span class="icon-text">
                        <span class="icon">
                            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-user">
                                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                                <circle cx="12" cy="7" r="4"></circle>
                            </svg>
                        </span>
                        <span>
                            <router-link class="text has-text-light"  to="/myaccount">{{ $t('navbar.Personal') }}</router-link>
                        </span>
                    </span>

                    <span class="icon-text ml-4">
                        <span class="icon" @click="logout">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-log-out">
                                <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
                                <polyline points="16 17 21 12 16 7"></polyline>
                                <line x1="21" y1="12" x2="9" y2="12"></line>
                            </svg>
                        </span>
                        <span>
                            <router-link class="text has-text-light"  to="/"></router-link>
                        </span>
                    </span>
                </template>
                <template v-else>
                    <router-link class="text" to="/login">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-log-in">
                            <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"></path>
                            <polyline points="10 17 15 12 10 7"></polyline>
                            <line x1="15" y1="12" x2="3" y2="12"></line>
                        </svg>
                    </router-link>
                </template>
                
              </div>
            </div>
          </div>
        </div>
      </nav>
    </template>
    <template v-else>
        <nav class="navbar is-black is-spaced">
            <div class="navbar-brand">
              <a class="navbar-item">
                <router-link to="/">
                    <img src="../../assets/bulma-logo-white.png" width="112" height="28">
                </router-link>
              </a>
            </div>
          
            <div  class="navbar-menu ">
              <div class="navbar-start">
                <router-link class="navbar-item" :to="{name:'Statistics'}">
                    {{ $t('Seting.Statistics') }}
                </router-link>
                <router-link class="navbar-item" :to="{name:'SetUsers'}">
                    {{ $t('Seting.Users') }}
                </router-link>
                <router-link class="navbar-item" :to="{name:'SetTeams'}">
                    {{ $t('Seting.Teams') }}
                </router-link>
                <router-link class="navbar-item" :to="{name:'SetTopics'}">
                    {{ $t('Seting.Topics') }}
                </router-link>
                <router-link class="navbar-item" :to="{name:'SetNotice'}">
                    {{ $t('Seting.Notice') }}
                </router-link>
              </div>
              <div class="navbar-end">
                <div class="navbar-item">
                  <div class="field is-grouped">
                  </div>
                </div>
              </div>
            </div>
          </nav>
    </template>
</div>
</template>

<script>
import store from '@/store'
import axios from 'axios'
import bulma from 'bulma'
import Login from '../../views/Login.vue'

export default {
  components: { Login },
        name: 'Navbar',
        data(){
            return{
                token:localStorage.getItem('token')
            }
        },
        mounted(){
           this.getmy(),
           this.getStanding()
        },
        methods:{
            async getmy(){
                console.log(store.state.isadmin)
                
            },
            async logout() {
                await axios
                    .post('/api/v1/token/logout/')
                    .then(response => {
                        console.log('Logged out')
                    })
                    .catch(error => {
                        console.log(JSON.stringify(error))
                    })
                    
                axios.defaults.headers.common['Authorization'] = ''
                localStorage.removeItem('token')
                this.$store.commit('setIsadmin', false)
                this.$store.commit('removeToken')
                this.$store.commit('initializeStore')
                this.$router.push('/login')
            },
            async getStanding(){
                this.$store.commit('setIsLoading', true)

                await axios
                    .post('/api/v1/control/is_standing/')
                    .then(response=>{
                       this.$store.commit('setIsadmin', response.data.isadmin)
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            }
        }

   
    }
</script>