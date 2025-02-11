<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">加入团队</h1>
            
                <form @submit.prevent="submitJoinTeam">
                    <div class="field">
                        <label>TeamToken</label>
                        <div class="control">
                            <input type="text" name="TeamToken" class="input" v-model="TeamToken">
                        </div>
                    </div>
                   
                        
                        <div class="field">
                            <div class="control">
                                <button class="button is-success">提交</button>
                            </div>
                        </div>
                </form>
                
            </div>
            
        </div>
    </div>
</template>
<script>
import axios from 'axios'
import bulma from 'bulma'
import {toast} from 'bulma-toast'

export default {
    name:"JoinTeam",
    data(){
      return{
        TeamToken:'',
      }
    },
    methods:{
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