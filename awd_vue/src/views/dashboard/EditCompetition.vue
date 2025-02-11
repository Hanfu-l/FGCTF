<template>
    <div>
        <div>
            <section class="hero is-black is-small pb-6">
                <div class="hero-body container is-max-desktop">
                  <p class="title  ">
                    {{ $t('Seting.Competitions') }}
                  </p>
                </div>
            </section>
        </div>
        <div class="box is-wight-7 mt-6 has-background-black">
        
        <button class="button is-success" @click="ApschedulerAdd">初始化竞赛</button>
        <router-link :to="{ name: 'CompetitionAndTopic', params: {  id: Competition.pk }}" >123</router-link>
        </div>
    </div>
</template>
<script>
import axios from 'axios'

export default {
    name:"EditCompetition",
    data() {
        return{
            Competition:{}
        }
    },
    mounted(){
        this.GetCompetition()
    },
    methods:{
      async GetCompetition(){
                this.$store.commit('setIsLoading', true)
                const data={
                    token:this.$route.params.token
                }

                await axios
                    .post('/api/v1/Seting/SetingCompetitions/GetCompetition/',data)
                    .then(response=>{
                       this.Competitions=response.data
                       console.log(this.Competitions)
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            },
        async ApschedulerAdd(){
                this.$store.commit('setIsLoading', true)
                const data={
                    CompetitionID:this.$route.params.id
                }

                await axios
                    .post('/api/v1/Seting/SetingCompetitions/Competition/ApschedulerAdd/',data)
                    .then(response=>{
                       this.Competitions=response.data
                       console.log(this.Competitions)
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            },
    }
}
</script>
