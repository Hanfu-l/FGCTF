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

         <table class="table has-background-black is-fullwidth has-text-white ">
          <thead>
            <tr>
              <th class="has-text-centered has-text-white">{{$t('Competition.Title')}}</th>
              <th class="has-text-centered has-text-white">{{$t('Competition.StartTime')}}</th>
              <th class="has-text-centered has-text-white">{{$t('Competition.EndTime')}}</th>
              <th class="has-text-centered has-text-white">{{$t('Competition.RoundNumber')}}</th>
              <th class="has-text-centered has-text-white">{{$t('Competition.RoundNumber')}}</th>
            </tr>
          </thead>
          <tbody>
            
                <tr
                v-for="Com in Competitions"
                v-bind:key="Com.id"
                
                >
                  <td><router-link :to="{ name: 'EditCompetition', params: { id: Com.id }}">{{Com.name}}</router-link></td>
                  <td>{{Com.starttime}}</td>
                  <td>{{Com.endtime}}</td>
                  <td>{{Com.rountnumber}}</td>
                  <td>{{Com.rounttime}}</td>
                </tr>
        
         </tbody>
         </table>
        </div>
    </div>
</template>
<script>
import axios from 'axios'

export default {
    name:"SetCompetitions",
    data() {
        return{
            Competitions:{}
        }
    },
    mounted(){
        this.CompetitionList()
    },
    methods:{
      async CompetitionList(){
                this.$store.commit('setIsLoading', true)

                await axios
                    .get('/api/v1/Seting/SetingCompetitions')
                    .then(response=>{
                       this.Competitions=response.data.Competitions
                       console.log(this.Competitions)
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            }
    }
}
</script>
