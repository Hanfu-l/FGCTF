<template>
    <div>
        <section class="hero is-black is-small pb-6">
            <div class="hero-body container is-max-desktop">
              <p class="title  ">
                {{ $t('Seting.Statistics') }}
              </p>
            </div>
          </section>
    </div>
</template>


<script>
import axios from 'axios'
import bulma from 'bulma'
import {toast} from 'bulma-toast'

export default {
    name:"Setings",
    data(){
      return{
      }
    },
    methods:{
    }
}
</script>