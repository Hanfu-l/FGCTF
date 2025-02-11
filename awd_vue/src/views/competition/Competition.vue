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
             <table class="table has-background-black is-fullwidth has-text-white ">
              <thead>
                <tr>
                  <th class="has-text-centered has-text-white">{{$t('Topic.Titele')}}</th>
                  <th class="has-text-centered has-text-white">访问地址</th>
                </tr>
                
              </thead>
              <tbody>
                <tr
                v-for="topic in Topics"
                v-bind:key="topic.pk"
                >
                  <td>{{topic.name}}</td>
                  <td>{{topic.UrlPath}}</td>
                </tr>
             </tbody>
             </table>
             <form @submit.prevent="SubmitFlag">
              <div class="notification has-background-primary mt-6">
                      <h4 class=" title is-4">提交答案</h4>
                      <div class="control">
                          <input type="text" name="Flag" class="input" v-model="Flag">
                      </div>
                      <button class="button is-warning mt-2 is-medium">提交</button>
              </div>
          </form>
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
            Topics:{},
            Flag:''
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
                },
            async SubmitFlag(){
            this.$store.commit('setIsLoading', true)

               const data={
                flag:this.Flag
               }

                await axios
                    .post('/api/v1/topics/submitflag/', data)
                    .then(response => {
                        toast({
                            message: '提交成功',
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
              

                this.$store.commit('setIsLoading', false)
            },
                
    
        }
    }
    </script>