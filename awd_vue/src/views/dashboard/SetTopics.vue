<template>

<div>
    <div>
        <section class="hero is-black is-small pb-6">
            <div class="hero-body container is-max-desktop">
              <p class="title  ">
                {{ $t('Topic.Titele') }}
              </p>
            </div>
          </section>
    </div>   

        
        <div class="box is-wight-7 mt-6 has-background-black">
        <div>
            <router-link :to="{name:'CreateTopic'}" class="button is-info">
                {{ $t('Topic.CreateTopic') }}
            </router-link>
          </div>
         <table class="table has-background-black is-fullwidth has-text-white ">
          <thead>
            <tr>
              <th class="has-text-centered has-text-white">{{$t('Topic.Titele')}}</th>
              <th class="has-text-centered has-text-white">{{$t('Topic.Type')}}</th>
              <th class="has-text-centered has-text-white">{{$t('Topic.Points')}}</th>
            </tr>
            
          </thead>
          <tbody>
            <tr
            v-for="topic in Topics"
            v-bind:key="topic.pk"
            >
              <td>{{topic.name}}</td>
              <td>{{topic.DockerName}}</td>
              <td>{{topic.score}}</td>
            </tr>
         </tbody>
         </table>
        </div>
      </div>          

</template>


<script>
import axios from 'axios'
import bulma from 'bulma'
import {toast} from 'bulma-toast'

export default {
    name:"SetTopics",
    data(){
      return{
        Topics:{}
      }
    },
    mounted(){
      this.getTopicList()
    },
    methods:{
      async getTopicList(){
                this.$store.commit('setIsLoading', true)

                await axios
                    .get('/api/v1/topics/')
                    .then(response=>{
                       this.Topics=response.data
                       console.log(this.Topics)
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            }

    }
}
</script>