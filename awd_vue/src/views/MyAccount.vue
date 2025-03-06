<template>
    <div class="container is-max-desktop">
      <div class="message is-wight-8 mt-6">
        <div class="message-header">
          <span class="icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-user">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
              <circle cx="12" cy="7" r="4"></circle>
            </svg>
          </span>
          <span>
            <a class="text has-text-light">个人信息</a>
          </span>
        </div>
  
        <div class="message-body has-background-black has-text-light">
          <div class="card has-background-black has-text-light">
            <div class="card-image">
              <div class="is-pulled-right">
                <figure class="image is-64x64">
                  <img class="is-rounded" src="../assets/user.gif" />
                </figure>
              </div>
            </div>
            <div class="card-content">
              <div class="content">
                <p><strong>用户名 :</strong> CTF_Player</p>
                <p><strong>邮箱 :</strong> player@example.com</p>
                <p><strong>当前排名 :</strong> #5</p>
                <p><strong>积分 :</strong> 1200</p>
              </div>
            </div>
          </div>
          <!-- 折线图 -->
          <div class="box mt-4">
            <div class="echart" ref="chartRef" :style="myChartStyle"></div>

          </div>
        </div>
      </div>
    </div>
  </template>
  

<script>
    import axios from 'axios'
    import store from '@/store'
    import * as echarts from "echarts";


    export default {
        name: 'MyAccount',
        data(){
            return{
                user: {
                username: "CTF_Player",
                email: "player@example.com",
                rank: 5,
                score: 1200,
                myChart: {},
                xData: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], //横坐标
                yData: [23, 24, 18, 25, 27, 28, 25], //人数数据
                myChartStyle: { float: "left", width: "100%", height: "400px" }
                      },
            }
        },
        mounted(){
            this.GetMyAccount()
            this.$nextTick(() => {
              this.DrawLine();
            });
        },
        methods: {
            
            async GetMyAccount(){
                this.$store.commit('setIsLoading', true)

                await axios
                    .get('/api/v1/users/me')
                    .then(response=>{
                        this.username=response.data.username
                        this.email=response.data.email
                    })
                    .catch(error => {
                        console.log(error)
                    })
                await axios
                .get('/api/v1/score/user/')
                .then(response=>{
                })
                .catch(error => {
                    console.log(error)
                })

                this.$store.commit('setIsLoading', false)
            },

            DrawLine(){
              if (!this.$refs.chartRef) {
                console.error("ECharts 容器未找到！");
                return;
            }
            this.myChart = echarts.init(this.$refs.chartRef);
            this.myChart.setOption({
                xAxis: { type: "category", data: this.xData },
                yAxis: { type: "value" },
                series: [{ data: this.yData, type: "line" }]
            });

            window.addEventListener("resize", () => {
                this.myChart.resize();
            });
            },

        }
    }
</script>