<template>
 <div> 
  <div>
        <section class="hero is-black is-small pb-6">
            <div class="hero-body container is-max-desktop">
              <p class="title  ">
                {{ $t('Notice.Title') }}
              </p>
            </div>
          </section>
    </div>   

        
        <div class="box is-wight-7 mt-6 has-background-black">
        <div>
            <router-link :to="{name:'CreateNotice'}" class="button is-info">
                {{ $t('Notice.CreateNotice') }}
            </router-link>
          </div>
         <table class="table has-background-black is-fullwidth has-text-white ">
          <thead>
            <tr>
              <th class="has-text-centered has-text-white">{{$t('Notice.Name')}}</th>
              <th class="has-text-centered has-text-white">{{$t('Notice.Description')}}</th>
              <th class="has-text-centered has-text-white">{{$t('Notice.Visable')}}</th>
            </tr>
            
          </thead>
          <tbody>
            <tr
            v-for="notice in Notices"
            v-bind:key="notice.pk"
            >
              <td>{{notice.name}}</td>
              <td>{{notice.Description}}</td>
              <td>{{notice.Visable}}</td>
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
    name:"SetNotice",
    data(){
      return{
        Notices:{
        }

       
      }
    },
    mounted(){
      this.NoticeList()
    },
    methods:{
      async NoticeList(){
                this.$store.commit('setIsLoading', true)

                await axios
                    .get('/api/v1/notice/')
                    .then(response=>{
                       this.Notices=response.data
                       console.log(this.Notices)
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            }
    }
}
</script>