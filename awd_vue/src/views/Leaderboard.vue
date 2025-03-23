<template>
    <div>
        <div>
            <section class="hero is-black is-small pb-6">
                <div class="hero-body container is-max-desktop">
                  <p class="title  ">
                    {{ $t('navbar.Leaderboard') }}
                  </p>
                </div>
            </section>
        </div>
        <div class="box is-wight-7 mt-6 has-background-black">

         <table class="table has-background-black is-fullwidth has-text-white ">
          <thead>
            <tr>
              <th class="has-text-centered has-text-white">{{$t('Leaderboard.User')}}</th>
              <th class="has-text-centered has-text-white">{{$t('Leaderboard.Points')}}</th>
            </tr>
            
          </thead>
          <tbody>
            <tr
            v-for="data in LeaderBoardData"
            >
              
              <td>{{data[0]}}</td>
              <td>{{data[1]}}</td>
            </tr>
            
            
         </tbody>
         </table>
        </div>
    </div>
</template>
<script>
import axios from 'axios'

export default {
    name:"LeaderBoard",
    data(){
              return{
                LeaderBoardData:{}
              }
          },
    mounted(){
        this.GetMyAccount()
    },
    methods:{
      async GetMyAccount(){
                this.$store.commit('setIsLoading', true)

                await axios
                    .get('/api/v1/GetLeaderBoard/')
                    .then(response=>{
                        this.LeaderBoardData=response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },
    }
}
</script>
