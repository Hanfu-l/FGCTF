<template>
  <div>
      <section class="hero is-black is-small pb-6">
          <div class="hero-body container is-max-desktop">
            <p class="title  ">
              {{ $t('Notice.CreateNotice') }}
            </p>
          </div>
        </section>
         <div class="box is-wight-7 mt-6 has-background-black">

       
<form @submit.prevent="SubmitCreateNotice">
        <div class="field">
          <label class="label has-text-white">  {{ $t('Notice.Name') }}</label>
            <div class="control">
              <input class="input" type="text" placeholder="Title input" name="NoticeName" v-model="NoticeName">
            </div>
          </div>

          <div class="field">
            <label class="label has-text-white">{{ $t('Notice.Visable') }}</label>
              <div class="control">
                <div class="select" >
                  <select name="NoticeVisable" v-model="NoticeVisable">
                    <option disable value="true">{{ $t('Topic.Visable') }}</option>
                    <option disable value="false">{{ $t('Topic.UnVisable') }}</option>
                  </select>
                </div>
              </div>
          </div>

          <div class="field">
            <label class="label has-text-white">{{ $t('Notice.Description') }}</label>
              <div class="control">
                <textarea class="textarea" placeholder="Textarea" name="NoticeDescription" v-model="NoticeDescription"></textarea>
              </div>
          </div>

          <div class="field is-grouped">
            <div class="control">
              <button class="button is-link" type="submit">{{ $t('Notice.Create') }}</button>
            </div>
            <div class="control">
              <button class="button is-link is-light">{{ $t('Notice.CancelCreate') }}</button>
            </div>
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
  name:"CreateNotice",
  data(){
    return{
      NoticeName:'',
      NoticeVisable:'',
      NoticeDescription:'',
    }
  },
  methods:{
  },
  methods:{

    async SubmitCreateNotice(){

      this.$store.commit('setIsLoading', true)

      const notice={
        name:this.NoticeName,
        Visable:this.NoticeVisable,
        Description:this.NoticeDescription
      }
      await axios
              .post('/api/v1/notice/', notice)
              .then(response => {
                  toast({
                      message: 'The notice was Created',
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

    }

  }
}
</script>