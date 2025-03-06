<!--题目列表页面，用于显示题目列表-->
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



    <div class="container mt-5">
    <div class="columns is-multiline">
      <div class="column is-one-quarter" v-for="topic in topics" :key="topic.pk">
        <router-link class="box " :to="{ name: 'TopicDes', params: { id: topic.pk } }">
          {{ topic.name }}
        </router-link>
      </div>
    </div>
  </div>


  </div>
  
</template>


<script>
import axios from 'axios';


    export default{
        name:"TopicList",
        data(){
            return{
              topics:{},
              errors:[],
              showInput:false,
            }
        },
        mounted(){
          this.GetTopicList()
        },
      methods: {
        async GetTopicList(){
          this.$store.commit('setIsLoading',true)

          await axios
            .get('/api/v1/Topic/List')
            .then(response=>{
              this.topics=response.data
              console.log(this.topics)
            })
            .catch(error => {
              console.log(error)
            })
          

          this.$store.commit('setIsLoading',false)

        },

        openInput(){
          this.showInput=true
        }
    },


    }
   
</script>


