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
          


        </div>
        <div class="box is-wight-8 mt-6 has-background-black">

          
          <div class="notification is-black">
          <strong>FGCTF</strong> 网络安全训练平台 基于Django和Vue共同实现，使用Docker作为题目管理容器，目前已实现大部分核心功能，但仍有部分功能需要优化，欢迎使用，如果遇到问题，请联系我们！
          <br>
          <div class="has-text-right">
            <strong>Hanfu</strong> 3493665801@qq.com
          </div>
        </div>
        </div>
        
    
        </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import Typed from './typed.vue';

export default {
  name: 'HomeView',
  components: {
    HelloWorld,
    Typed
  }
}
</script>