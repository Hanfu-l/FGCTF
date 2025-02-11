<template>
  <div class="container is-max-desktop">
    <teamplate v-if="TeamToken">
        <div class="media notification has-background-grey-light has-text-white mt-6 pt-6 pb-6">
            <figure class="media-left">
              <p class="image is-128x128">
                <img src="../../assets/logo.png">
              </p>
            </figure>
            <div class="media-content">
              <div class="content">
                
                <template v-if="Teamname">
                <h5 class="title is-5">{{$t('Team.Title')}}:  {{this.Teamname}}</h5>
                <h5 class="title is-5">{{$t('User.TeamToken')}}:  {{this.TeamToken}}</h5>
                </template>
        
        
              </div>
            </div>
        </div>

        <div class="notification has-text-white has-background-grey-dark">
            <h5 class="title is-5">{{$t('Team.TeamMembers')}}</h5>
            <div class="box has-background-grey-dark ">
                <table class="table is-fullwidth has-background-grey-dark has-text-white">
                    <thead>
                        <tr>
                            <th class="has-text-white">{{$t('Team.MemberName')}}</th>
                            <th></th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr
                            v-for="member in members"
                            v-bind:key="member.id"
                        >
                            <td>{{member.username}}</td>
                            <button @click="deletemember(member.username)" class="button is-danger mt-1">{{$t('Team.DeleteMember')}}</button>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

       

    </teamplate>
    <teamplate v-else>
        <div class="container is-max-desktop">
            <form @submit.prevent="SubmitCreateTeam">
                <div class="notification has-background-primary mt-6">
                        <h4 class=" title is-4">{{$t('Team.Title')}}</h4>
                        <div class="control">
                            <input type="text" name="TeamName" class="input" v-model="CreateTeamName">
                        </div>
                        <button class="button is-warning mt-2 is-medium">{{$t('Team.CreateTeam')}}</button>
                </div>
            </form>
             <form @submit.prevent="submitJoinTeam">
            <div class="notification has-background-info mt-6">
                <h4 class=" title is-4">{{$t('Team.Token')}}</h4>
                <div class="control">
                    <input type="text" name="CompetitionToken" class="input" v-model="CompetitionToken">
                </div>
                <button class="button is-warning mt-2 is-medium">{{$t('Team.Join')}}</button>
            </div>
        </form>

        </div>
    </teamplate>
  </div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

export default {
  name: 'Team',
  data(){
      return{
          CreateTeamName:'',
          Teamname:'',
          TeamToken:'',
          members:[],
          CompetitionToken:'',
      }
  },
  mounted(){
      this.getTeam()
  },
  methods: {
    async SubmitCreateTeam(){
            this.$store.commit('setIsLoading', true)

                const team = {
                    name: this.CreateTeamName
                }

                await axios
                    .post('/api/v1/teams/', team)
                    .then(response => {
                        toast({
                            message: 'The team was Created',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })

                        
                    })
                    .catch(error => {
                        console.log(error)
                    })
                
                    this.$router.push('/team')

                this.$store.commit('setIsLoading', false)
            },
      async getTeam() {
      this.$store.commit('setIsLoading', true)
      await axios
          .get('/api/v1/teams/get_my_team/')
          .then(response => {
              console.log(response.data)
              this.Teamname=response.data.name
              this.TeamToken=response.data.TeamToken
              this.members=response.data.members
          })
          .catch(error => {
              console.log(error)
          })
      
      this.$store.commit('setIsLoading', false)
  },
  async deletemember(membername) {
                this.$store.commit('setIsLoading', true)

        await axios
                    .post(`/api/v1/teams/delete_member/${membername}/`)
                    .then(response => {
                        console.log(response.data)
                        this.getTeam()
                        this.$router.push('/team')
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            },
    async submitJoinCompetition() {
                this.$store.commit('setIsLoading', true)

                const data = {
                    CompetitionToken:this.CompetitionToken
                }

                await axios
                .post('/api/v1/competitions/join_competition/', data)
                    .then(response => {
                        toast({
                            message: 'The team was Created',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })

                        
                    })
                    .catch(error => {
                        console.log(error)
                    })


                this.$router.push('/team')
                this.$store.commit('setIsLoading', false)
            },
    async submitJoinTeam(){
            this.$store.commit('setIsLoading', true)

                const data = {
                    TeamToken:this.TeamToken
                }

                await axios
                .post('/api/v1/teams/join_team/',data)
                .then(response => {
                })
                .catch(error => {
                    console.log(error)
                })



                this.$router.push('/myaccount')
                this.$store.commit('setIsLoading', false)
          
                    }
      
  }
}
</script>