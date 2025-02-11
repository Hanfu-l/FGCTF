<template>
  <div>
        <div>
            <section class="hero is-black is-small pb-6">
                <div class="hero-body container is-max-desktop">
                  <p class="title  ">
                    {{ $t("navbar.Home") }}
                  </p>
                </div>
              </section>
        </div>

        <div>
            <figure class="image container is-256x256">
    <img src="../assets/logo.svg">
</figure>

        </div>
    
    
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  }
}
</script>
