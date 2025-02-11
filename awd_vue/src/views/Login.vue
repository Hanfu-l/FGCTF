<template>
    <div>
        <div>
            <section class="hero is-black is-small pb-6">
                <div class="hero-body container is-max-desktop">
                  <p class="title  ">
                    {{ $t("login.Title") }}
                  </p>
                </div>
              </section>
        </div>
    <div class="container is-max-desktop pr-6 pl-6">
        <div class="notification has-background-dark has-text-white">
            <section class="section">    
                <form  @submit.prevent="submitForm">
                    <div class="field">
                      <div class="control">
                        <h4 class="title is-4">{{$t('login.Username')}}</h4>
                        <input class="input is-medium is-rounded" name="username" v-model="username"/>
                      </div>
                    </div>
                    <div class="field">
                      <div class="control">
                        <h4 class="title is-4">{{$t('login.Password')}}</h4>
                        <input class="input is-medium is-rounded" name="password" type="password" v-model="password"/>
                      </div>
                    </div>
                    <br />
                    
                    <button class="button is-block  is-primary is-medium is-rounded is-pulled-right" type="submit">
                        {{ $t("login.Title") }}
                    </button>
                    <br />
                    <br />
                    <br />

                    <router-link to="/signup" >
                        {{ $t("login.Signup") }}
                    </router-link>
                    
                    
                    
                  </form>
            
              </section>
        </div>
    </div>
    </div>
</template>


<script>
import axios from 'axios'
import store from '@/store'
import {toast} from 'bulma-toast'

    export default {
        name: 'Login',
        data(){
            return{
                Title:this.$t('login.Title'),
                username:'',
                password:'',
                errors:[]
            }
        },
        methods:{
            async submitForm(){
                this.$store.commit('setIsLoading',true)

                axios.defaults.headers.common['Authorization'] = ''
                localStorage.removeItem('token')

                const formData = {
                    username: this.username,
                    password: this.password
                }

                await axios
                    .post('/api/v1/token/login/', formData)
                    .then(response => {
                        const token = response.data.auth_token
                        this.$store.commit('setToken', token)

                        axios.defaults.headers.common['Authorization'] = 'Token ' + token

                        localStorage.setItem('token', token)

                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again!')
                        }
                    })

                    this.$router.push('/myaccount')
                

                this.$store.commit('setIsLoading',false)
            }
        }
    }
</script>