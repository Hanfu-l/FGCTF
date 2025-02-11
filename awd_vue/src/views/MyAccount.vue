<template>
    
    <div class="container is-max-desktop">
        
        
        <div class="message is-wight-8 mt-6">
            <div class="message-header">
                <span class="icon">
                    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-user">
                        <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                        <circle cx="12" cy="7" r="4"></circle>
                    </svg>
                </span>
                <span>
                    <a class="text has-text-light">{{ $t('navbar.Personal') }}</a>
                </span>
              </div>
              <div class="message-body has-background-black has-text-light">
              
                <div class="card has-background-black has-text-light">
                    <div class="card-image">
                        <div class="is-pulled-right">
                            <figure class="image is-128x128 ">
                                <img class="is-rounded " src="../assets/logo.png">
                            </figure>
                        </div>
                    </div>
                    <div class="card-content">
                      <div class="media">
                        <div class="media-content">
                          <p class="title is-5 has-text-light">用户名</p>
                          <div class="control">
                                <input class="input is-wight-4 has-background-black-ter has-text-light" type="text" v-model="username">
                          </div>
                        </div>
                      </div>
                      <div class="content">
                        <p class="title is-5 has-text-light">邮箱号</p>
                        <div class="control">
                          <input class="input is-wight-4 has-background-black-ter" type="text" :placeholder="email" disabled>
                        </div>
                      </div>
                      <div class="content">
                        
                            <p class="title is-5 has-text-light">隶属团队</p>
                            <div class="control">
                                <input class="input is-wight-4 has-background-black-ter" type="text" :placeholder="TeamToken" disabled>
                            </div>
                            <p class="title is-5 has-text-light mt-6">描述</p>
                            <textarea class="textarea has-background-black-ter has-text-light" placeholder="textarea"></textarea>
                        
                      </div>
                    </div>
                  </div>


                <div class="is-pulled-right">
                   
                </div>
              </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import store from '@/store'

    export default {
        name: 'MyAccount',
        data(){
            return{
                username:'',
                Teamname:'',
                TeamToken:'',
                email:'',
            }
        },
        mounted(){
            this.GetMyAccount()
            this.getTeam()
        },
        methods: {
            
            async GetMyAccount(){
                this.$store.commit('setIsLoading', true)

                await axios
                    .get('/api/v1/users/me')
                    .then(response=>{
                        this.username=response.data.username
                        this.email=response.data.email
                    })
                    .catch(error => {
                        console.log(error)
                    })
                await axios
                .get('/api/v1/score/user/')
                .then(response=>{
                })
                .catch(error => {
                    console.log(error)
                })

                this.$store.commit('setIsLoading', false)
            },
            async getTeam() {
            this.$store.commit('setIsLoading', true)
            await axios
                .get('/api/v1/teams/get_my_team/')
                .then(response => {
                    this.Teamname=response.data.name
                    this.TeamToken=response.data.TeamToken
                })
                .catch(error => {
                    console.log(error)
                })
            
            this.$store.commit('setIsLoading', false)
        }
            
        }
    }
</script>

