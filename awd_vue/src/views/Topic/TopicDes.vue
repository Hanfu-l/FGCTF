<!--题目详情页面，用于显示题目详情-->
<template>
    <div class="container">
        <!-- 题目内容 -->
        <section class="section">
          <div class="columns is-vcentered">
            <!-- 题目名称 -->
            <div class="column">
              <h1 class="title is-3 has-text-white">{{ topicdata.name}}</h1>
            </div>
          </div>

          <!-- 题目分数 -->
          <div class="level">
            <div class="level-left">
              <p class="level-item has-text-white">分数   {{ topicdata.score}}</p>
            </div>
          </div>

          <!-- 题目描述 -->
          <div class="level">
            <div class="level-left">
              <p class="level-item has-text-white"><strong class="has-text-white">描述 :  </strong>   {{ topicdata.Description}}</p>
            </div>
          </div>

          <div v-if="!(RunDockerData['RunDockerTopicId']==topicdata.pk)">
              <!--启动题目环境-->
              <div class="level">
                <div class="level-left mb-6">
                  <button class="button is-primary" @click="OpenEnv">启动环境</button>
                </div>
              </div>
          </div>
          
          <div v-else>
              <!--环境启动后的显示-->
              

              <a :href="RunDockerUrl">{{this.RunDockerUrl}}</a>
              <h2 class="title is-6 has-text-white" ><strong class="has-text-white">题目地址 :  </strong>{{this.RunDockerUrl}}</h2>

              <!--关闭题目环境-->
              <div class="level mb-5">
                <div class="level-left">
                  <button class="button is-danger" @click="CloseDocker">关闭环境</button>
                </div>
              </div>

          </div>

          <!-- 答案提交 -->
          <div class="answer-container">
            <h2 class="title is-6 has-text-white">提交你的答案 (CTF Flag)</h2>
            <div class="field has-addons">
              <div class="control is-expanded">
                <input
                  v-model="flag"
                  class="input is-dark has-text-black"
                  type="text"
                  placeholder="请输入CTF flag..."
                />
              </div>
              <div class="control">
                <button @click="SubmitFlag()" class="button is-primary">
                  提交答案
                </button>
              </div>
            </div>
          </div>
        </section>
      </div>
</template>


<script>

import axios from 'axios';


    export default{
        name:"TopicDes",
        data(){
            return{
              topicdata:{},
              flag:'',
              RunDockerData:{},
              RunDockerUrl:'',
            }
        },
        mounted(){
          this.GetDockerData()
          this.GetTopicList()
        },
      methods: {
        async GetTopicList(){
          this.$store.commit('setIsLoading',true)

          await axios
            .get(`/api/v1/Topic/GetTopic/${ this.$route.params.id }`)
            .then(response=>{
              this.topicdata=response.data
              console.log(this.topics)
            })
            .catch(error => {
              console.log(error)
            })
          

          this.$store.commit('setIsLoading',false)

        },

        async OpenEnv(){
                this.$store.commit('setIsLoading',true)

                const formData={
                    topicid:this.topicdata.pk

                }

                await axios
                  .post('/api/v1/Topic/RunTopic',formData)
                  .then(response=>{
                    this.$forceUpdate()
                  })
                  .catch(error => {
                    console.log(error)
                  })
                

                this.$store.commit('setIsLoading',false)
              },
          
              async CloseDocker(){
                this.$store.commit('setIsLoading',true)

                await axios
                  .get('/api/v1/Topic/CloseTopic')
                  .then(response=>{
          
                  })
                  .catch(error => {
                    console.log(error)
                  })
                

                this.$store.commit('setIsLoading',false)
              },

              async GetDockerData(){
                this.$store.commit('setIsLoading',true)

                await axios
                  .get('/api/v1/Topic/GetRunDocker')
                  .then(response=>{
                    this.RunDockerData=response.data
                    this.RunDockerUrl=this.RunDockerData['RunDockerUrl'] +':'+this.RunDockerData['RunDockerPort']
                  })
                  .catch(error => {
                    console.log(error)
                  })
                

                this.$store.commit('setIsLoading',false)
              },
              async SubmitFlag(){
                this.$store.commit('setIsLoading',true)

                const formData={
                    topicid:this.topicdata.pk,
                    submitflag:this.flag

                }

                await axios
                  .post('/api/v1/Topic/SubmitFlag',formData)
                  .then(response=>{
                    console.log(response.data)
                  })
                  .catch(error => {
                    console.log(error)
                  })
                

                this.$store.commit('setIsLoading',false)
              },

        },
      
    }


</script>