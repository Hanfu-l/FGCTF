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
            <a class="text has-text-light">个人信息</a>
          </span>
        </div>
  
        <div class="message-body has-background-black has-text-light">
          <div class="card has-background-black has-text-light">
            <div class="card-image">
              <div class="is-pulled-right">
                <figure class="image is-64x64">
                  <img class="is-rounded" src="../assets/user.gif" />
                </figure>
              </div>
            </div>
            <div class="card-content">
              <div class="content">
                <p><strong>用户名 :</strong> {{ this.user.username }}</p>
                <p><strong>当前排名 :</strong> {{ this.user.rank+1 }}</p>
                <p><strong>积分 :</strong> {{ this.user.score }}</p>
              </div>
            </div>
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
                user:{},
            }
        },
        mounted(){
            this.GetMyAccount()
        },
        methods: {
            
            async GetMyAccount(){
                this.$store.commit('setIsLoading', true)

                await axios
                    .get('/api/v1/GetMydata')
                    .then(response=>{
                      this.user=response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },

        }
    }
</script>