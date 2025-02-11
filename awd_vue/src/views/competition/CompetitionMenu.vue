<template>
    <div class="container is-max-desktop">

        <div class="box mt-6 has-background-grey-dark has-text-white">
            <figure class="image is-3by1 ">
                <img src="../../assets/logo.png">
              </figure>

              <div class="hero mt-6 has-background-grey-dark has-text-white is-small">
                <div class="hero-body container is-max-desktop">
                    <p class="title  has-text-white">
                      {{ Competition.name }}
                    </p>
                  </div>    

              </div>

              <div class="notification mt-6 has-background-grey-dark has-text-white">
                <p>1.禁止不同参赛人员/队伍合作，共享flag、hint等任何比赛相关信息。</p>
                <p>2. 禁止攻击比赛平台，如果发现平台漏洞，请务必向我们报告。</p>
                <p>3. 禁止对提交的flag进行爆破。</p>
                <p>4. 最终排名根据每个队伍的总分确定，在多个队伍得分相同的情况下，越早达到这一分值的排名越高。</p>
              </div>
              
              <div class="has-background-grey-dark ">
                <div>
                    <router-link class="button is-danger is-medium ml-4 " :to="{ name: 'AttackDefense', params: { token: Competition.token }}">
                        {{ $t('Competition.AttackAndDefense') }}
                    </router-link>
                </div>
              </div>

        </div>
    </div>
</template>
<script>
    import axios from 'axios'
    
    export default {
        name: 'CompetitionMenu',
        data(){
            return{
                Competition:{},
                competitionID:this.$route.params.id
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
                    this.Competition=response.data
                    console.log(this.Competition.token)

                })
                .catch(error => {
                    console.log(error)
                })
            
            this.$store.commit('setIsLoading', false)
        },   
        }
    }
    
</script>