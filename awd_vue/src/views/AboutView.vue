<template>
  <div>
      <div>
          <section class="hero is-black is-small pb-6">
              <div class="hero-body container is-max-desktop">
                <p class="title  ">
                  {{ $t('navbar.About') }}
                </p>
              </div>
          </section>
      </div>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  name:"About",
  data(){
            return{
            }
        },
  mounted(){
  },
  methods:{
  }
}
</script>
