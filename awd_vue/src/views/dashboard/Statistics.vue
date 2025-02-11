<template>
    <div>
        <div>
            <section class="hero is-black is-small pb-6">
                <div class="hero-body container is-max-desktop">
                  <p class="title  ">
                    {{ $t('Seting.Statistics') }}
                  </p>
                </div>
            </section>
        </div>

        <div>
            <div class="tile is-ancestor">
                <div class="tile is-vertical is-8">
                  <div class="tile">
                    <div class="tile is-parent is-vertical">
                      <article class="tile is-child notification is-primary">
                        <p class="title">当前用户数量</p>
                        <p class="subtitle" >6 人</p>
                      </article>
                      <article class="tile is-child notification is-warning">
                        <p class="title">当前题目数量</p>
                        <p class="subtitle">3 题</p>
                      </article>
                    </div>
                    <div class="tile is-parent">
                      <article class="tile is-child notification is-info">
                        <p class="title">首页</p>
                        <p class="subtitle">首页图片</p>
                        <figure class="image is-4by3">
                          <img src="../../assets/logo.svg">
                        </figure>
                      </article>
                    </div>
                  </div>
                  <div class="tile is-parent">
                    <article class="tile is-child notification is-danger">
                      <p class="title">系统警告</p>
                      <p class="subtitle">无</p>
                      <div class="content">
                        <!-- Content -->
                      </div>
                    </article>
                  </div>
                </div>
                <div class="tile is-parent">
                  <article class="tile is-child notification is-success">
                    <div class="content">
                      <p class="title">公告信息</p>
                      <p class="subtitle">空</p>
                      <div class="content">
                        <table class="table has-background-black is-fullwidth has-text-white ">
                          <thead>
                            <tr>
                              <th class="has-text-centered has-text-white">{{$t('Notice.Name')}}</th>
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
                              <td>{{notice.Visable}}</td>
                            </tr>
                         </tbody>
                         </table>
                      </div>
                    </div>
                  </article>
                </div>
              </div>
        </div>

    </div>
</template>
<script>
import axios from 'axios'

export default {
    name:"Statistics",
    data() {
        return{
            data:{},
            Usernumber:'',
            Teamnumber:'',
            Notices:{},
        }
    },
    mounted(){
        this.GetMyAccount(),
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
            },
      async GetMyAccount(){
                this.$store.commit('setIsLoading', true)

                await axios
                    .get('/api/v1/topics/Statistics')
                    .then(response=>{
                       console.log(this.users)
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            }
    }
}
</script>
