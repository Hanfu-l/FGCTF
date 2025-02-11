<template>
    <div>
        <section class="hero is-black is-small pb-6">
            <div class="hero-body container is-max-desktop">
              <p class="title  ">
                {{ $t('Topic.CreateTopic') }}
              </p>
            </div>
          </section>
          
<form @submit.prevent="SubmitCreateTopic">
  <div class="box is-wight-7 mt-6 has-background-black">
         <div class="field">
          <label class="label has-text-white">  {{ $t('Topic.Name') }}</label>
          <div class="control">
            <input class="input" type="text" placeholder="TopicName input" name="TopicName" v-model="TopicName">
          </div>
        </div>

      <div class="field">
        <label class="label has-text-white">{{ $t('Topic.DockerName') }}</label>
        <div class="control has-icons-left has-icons-right">
          <input class="input" type="text" placeholder="DockerName Input" name="DockerName" v-model="DockerName">
        </div>
      </div>
        <div class="field">
          <label class="label has-text-white">{{ $t('Topic.DockerPort') }}</label>
          <div class="control has-icons-left has-icons-right">
            <input class="input" type="text" placeholder="Port Input" name="DockerPort" v-model="DockerPort">
          </div>
        </div>
        <div class="field">
          <label class="label has-text-white">{{ $t('Topic.DockerPort') }}</label>
          <div class="control has-icons-left has-icons-right">
            <input class="input" type="text" placeholder="Url Input" name="TopicUrlPath" v-model="TopicUrlPath">
          </div>
        </div>

        <div class="field">
          <label class="label has-text-white">{{ $t('Topic.Points') }}</label>
          <div class="control has-icons-left has-icons-right">
            <input class="input" type="number" placeholder="Points Input" name="TopicPoints" v-model="TopicPoint">
          </div>
        </div>

        <div class="field">
          <label class="label has-text-white">{{ $t('Topic.KeyValue') }}</label>
          <div class="control has-icons-left has-icons-right">
            <input class="input" type="text" placeholder="Points Input" name="TopicKeyvalue" v-model="TopicKeyvalue">
          </div>
        </div>

          <div class="field">
            <label class="label has-text-white">{{ $t('Topic.isVisable') }}</label>
            <div class="control">
              <div class="select">
                <select name="TopicVisable" v-model="TopicVisabel">
                  <option disable value="true">{{ $t('Topic.Visable') }}</option>
                  <option disable value="false">{{ $t('Topic.UnVisable') }}</option>
                </select>
              </div>
            </div>
          </div>

          <div class="field">
            <label class="label has-text-white">{{ $t('Topic.Description') }}</label>
            <div class="control">
              <textarea class="textarea" placeholder="Textarea" name="TopicDescription" v-model="TopicDescription"></textarea>
            </div>
          </div>
            <div class="field is-grouped">
              <div class="control">
                <button class="button is-link" type="submit">Submit</button>
              </div>
              <div class="control">
                <button class="button is-link is-light">Cancel</button>
              </div>
            </div>
        </div>
</form>
    </div>
</template>


<script>
import axios from 'axios'
import bulma from 'bulma'
import {toast} from 'bulma-toast'

export default {
    name:"CreateTopic",
    data(){
      return{
        TopicName:'',
        DockerName:'',
        DockerPort:'',
        TopicUrlPath:'',
        TopicPoint:'',
        TopicVisabel:'',
        TopicDescription:'',
        TopicKeyvalue:'',
      }
    },
    methods:{

      async SubmitCreateTopic(){

this.$store.commit('setIsLoading', true)

const topic={
  name:this.TopicName,
  score:this.TopicPoint,
  DockerName:this.DockerName,
  UrlPath:this.TopicUrlPath,
  DockerPort:this.DockerPort,
  Description:this.TopicDescription,
  Visable:this.TopicVisable,
  Keyvalue:this.TopicKeyvalue,
}
await axios
        .post('/api/v1/topics/', topic)
        .then(response => {
            toast({
                message: 'The topic was Created',
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