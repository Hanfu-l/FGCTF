<template>
    <div>
        <div>
            <section class="hero is-black is-small pb-6">
                <div class="hero-body container is-max-desktop">
                  <p class="title  ">
                    {{ $t('navbar.Notice') }}
                  </p>
                </div>
            </section>
        </div>
        <div class="box is-wight-7 mt-6 has-background-black">

         <table class="table has-background-black is-fullwidth has-text-white ">
          <thead>
            <tr>
              <th class="has-text-centered has-text-white">{{$t('Notice.Title')}}</th>
              <th class="has-text-centered has-text-white">{{$t('Notice.Description')}}</th>
            </tr>
            
          </thead>
          <tbody>
            <tr
            v-for="notice in Notices"
            v-bind:key="notice.pk"
            >
              <td>{{notice.name}}</td>
              <td>{{notice.Description}}</td>
            </tr>
         </tbody>
         </table>
        </div>
    </div>
</template>
<script>
import axios from 'axios'

export default {
    name:"SetUsers",
    data() {
        return{
          Notices:{
        }
        }
    },
    mounted(){
        this.GetMyAccount()
    },
    methods:{
      async GetMyAccount(){
                this.$store.commit('setIsLoading', true)

                await axios
                    .get('/api/v1/notices/list/')
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
