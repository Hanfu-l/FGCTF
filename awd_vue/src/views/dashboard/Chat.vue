<template>
<div class="hero is-dark is-fullheight">
    <div class="hero-body">
      <div class="container is-flex is-flex-direction-column" style="max-width: 1000px;">
        
        <!-- 标题 -->
        <h1 class="title has-text-white has-text-centered">智问demo</h1>

        <!-- 聊天内容 -->
        <div class="box has-background-dark p-4 is-flex-grow-1 is-clipped" 
             style="height: 1000px; overflow-y: auto;">
            
        <div v-for="data in questions">
          <!-- 用户消息 -->
          <div class="notification is-primary has-text-right mt-6">
            {{data.question}}🚀
          </div>

          <!-- AI 回复 -->
          <div class="notification is-light">
            {{ data.answer }}
          </div>


        </div>
          
          
        </div>

        <!-- 输入框（静态展示，不可输入） -->
        <div class="field has-addons mt-3">
          <div class="control is-expanded">
            <input 
              v-model="content"
              class="input" 
              type="text" 
              placeholder="输入消息..." 
            />
          </div>
          <div class="control">
            <button class="button is-primary" @click="Chat()">
              发送
            </button>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';


    export default{
        name:"LangChain",
        data(){
            return{
              questions:[],
              content:'',
            }
        },
        mounted(){
          this.GetQue()
        },
        methods:{
          async Chat(){
                this.$store.commit('setIsLoading',true)

                const formData={
                    question:this.content

                }

                await axios
                  .post('/api/v1/GPT',formData)
                  .then(response=>{
                    this.GetQue()
                  })
                  .catch(error => {
                    console.log(error)
                  })
                

                this.$store.commit('setIsLoading',false)
              },
            async GetQue(){
              this.$store.commit('setIsLoading',true)

              await axios
                .get('/api/v1/GetQuestions')
                .then(response=>{
                  this.questions=response.data
                  console.log(this.questions)
                })
                .catch(error => {
                  console.log(error)
                })
              

              this.$store.commit('setIsLoading',false)
            },
        }

    }

</script>