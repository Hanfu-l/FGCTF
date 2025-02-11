<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12 ">
                <h1 class="title">题目信息</h1>      
            </div>
        </div>
        <div class="box">
            <div>
                                
                <form @submit.prevent="submitNewTopic">
                    <div class="field">
                        <label>题目名称</label>
                        <div class="control">
                            <input type="text" name="TopicName" class="input" v-model="TopicName">
                        </div>
                    </div>
                    <div class="field">
                        <label>对外地址</label>
                        <div class="control">
                            <input type="text" name=" Topicexternal" class="input" v-model="Topicexternal">
                        </div>
                    </div>
                    <div class="field">
                        <label>对内地址</label>
                        <div class="control">
                            <input type="text" name=" Topicinterior" class="input" v-model="Topicinterior">
                        </div>
                    </div>
                    <div class="field">
                        <label>对内账户</label>
                        <div class="control">
                            <input type="text" name=" Topicsshname" class="input" v-model="Topicsshname">
                        </div>
                    </div>
                    <div class="field">
                        <label>对内密码</label>
                        <div class="control">
                            <input type="text" name=" Topicsshpassword" class="input" v-model="Topicsshpassword">
                        </div>
                    </div>
                    <div class="field">
                        <label>Flag存储路径</label>
                        <div class="control">
                            <input type="text" name=" Topicimagenname" class="input" v-model="TopicFlagPath">
                        </div>
                    </div>
                    <div class="field">
                        <label>可允许访问路径</label>
                        <div class="control">
                            <input type="text" name=" Topicimagenname" class="input" v-model="TopicinteriorPath">
                        </div>
                    </div>
                    <div class="field">
                        <label>初始分数</label>
                        <div class="control">
                            <input type="text" name=" Topicinitscore" class="input" v-model="Topicinitscore">
                        </div>
                    </div>
                    <div class="field">
                        <label>攻击得分</label>
                        <div class="control">
                            <input type="text" name="Topicattackscore" class="input" v-model="Topicattackscore">
                        </div>
                    </div>
                    <div class="field">
                        <label>Check得分</label>
                        <div class="control">
                            <input type="text" name="Topiccheckscore" class="input" v-model="Topiccheckscore">
                        </div>
                    </div>
                        <div class="field">
                            <div class="control">
                                <button class="button is-success">初始化题目信息</button>
                            </div>
                        </div>

                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'CompetitionAndTopic',
        data(){
            return{
                TopicName:'',
                Topicexternal:'',
                Topicinterior:'',
                Topicsshname:'',
                Topicsshpassword:'',
                TopicinteriorPath:'',
                TopicFlagPath:'',
                Topicinitscore:1000,
                Topicattackscore:100,
                Topiccheckscore:100,
                TopicCompetition:0,
            }
        },
        methods:{
            async submitNewTopic(){

                this.$store.commit('setIsLoading', true)

                const topic = {
                    name:this.TopicName,
                    external:this.Topicexternal,
                    interior:this.Topicinterior,
                    sshname:this.Topicsshname,
                    sshpassword:this.Topicsshpassword,
                    interiorpath:this.TopicinteriorPath,
                    flagpath:this.TopicFlagPath,
                    attackscore:this.Topicattackscore,
                    checkscore:this.Topiccheckscore,
                    initscore:this.Topicinitscore,
                    competition:this.$route.params.id
                }

                await axios
                    .post('/api/v1/Seting/SetingCompetitions/Competition/TopicAdd/', topic)
                    .then(response => {
                        toast({
                            message: 'The competition was Created',
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
                
                    this.$router.push('/Setings/Competitions/')

                this.$store.commit('setIsLoading', false)
               
            }
        }
            
        }
    
</script>