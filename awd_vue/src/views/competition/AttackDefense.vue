<template>
    <div>
      <div class="columns">
        <div class="column is-one-fifth mt-6">
          <article class="panel is-pulled-left">
            <p class="panel-heading">
                靶机列表
            </p>
          </article>      
        </div>
          <div class="column">
            <div class="message is-wight-8 mt-6">
              <div class="message-header">
                  <span class="icon">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-chevron-left">
                      <polyline points="15 18 9 12 15 6"></polyline>
                    </svg>
                  </span>
                  <span class="icon">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-chevron-right">
                      <polyline points="9 18 15 12 9 6"></polyline>
                    </svg>
                  </span>
                </div>
                <div class="message-body has-background-black has-text-light">
                  <h2 class="title is-2 has-text-centered has-text-light">Web1</h2>
                  <div>
                    <p class="title is-5 has-text-light has-text-centered">开放服务及端口</p>
                    <div class="has-text-centered">
                          <p class="input is-wight-5 has-background-black-ter has-text-light" ></p>
                    </div>
                        <p class="title is-5 has-text-light mt-4">SSH账密</p>
                        <div class="control ">
                              <input class="input is-wight-5 has-background-black-ter has-text-light" type="text">
                              <span class="icon mt-2 ml-6">
                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-globe">
                                  <circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line>
                                  <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
                                </svg>
                              </span>
                        </div>
                        
                      
                  </div>
                </div>
            </div>
          </div>
          <div class="column is-one-fifth mt-6 ml-5 is-full">
            <article class="panel is-pulled-right mr-4">
              <p class="panel-heading">
                  <p>团队名</p>
                  <p>排行</p>
                  <p>当前积分</p>
                  <p>本轮积分</p>
              </p>
            </article>      
          </div>

     
      </div>
      
      
    
    

        
    </div>
    
</template>

<script>
import axios from 'axios'

export default {
    name:"AttackDefense",
    data() {
        return{
              Competition:{},
              Topics:[]
        }
    },
    mounted(){
        this.getCompetitions()
    },
    methods:{
      async getCompetitions() {
            this.$store.commit('setIsLoading', true)
            const data={
                token:this.$route.params.token
            }
            await axios
                .post('/api/v1/competitions/attackdefense/',data)
                .then(response => {
                    this.Competition=response.data.Competition
                    this.Topics=response.data.Topics

                })
                .catch(error => {
                    console.log(error)
                })
            
            this.$store.commit('setIsLoading', false)
        },
        async getCompetitions() {
            this.$store.commit('setIsLoading', true)
            const data={
                token:this.$route.params.token
            }
            await axios
                .post('/api/v1/competitions/attackdefense/',data)
                .then(response => {
                    this.Competition=response.data.Competition
                    this.Topics=response.data.Topics

                })
                .catch(error => {
                    console.log(error)
                })
            
            this.$store.commit('setIsLoading', false)
        },
    }
}
</script>
