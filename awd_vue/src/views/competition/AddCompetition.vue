<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12 ">
                <h1 class="title">添加竞赛</h1>
                
                <form @submit.prevent="submitNewCompetition">
                    <div class="field">
                        <label>竞赛名称</label>
                        <div class="control">
                            <input type="text" name="CompetitionName" class="input" v-model="CompetitionName">
                        </div>
                    </div>
                    <div class="field">
                        <label>轮次</label>
                        <div class="control">
                            <input type="text" name=" CompetitionRount" class="input" v-model="CompetitionRount">
                        </div>
                    </div>
                    <div class="field">
                        <label>每轮时长</label>
                        <div class="control">
                            <input type="text" name=" CompetitionRounttime" class="input" v-model="CompetitionRounttime">
                        </div>
                    </div>
                    <div class="field">
                        <label>开始时间</label>
                        <div class="control">
                            <input type="datetime-local" name="CompetitionStarttime" class="input" v-model="CompetitionStarttime">
                        </div>
                    </div>
                    <div class="field">
                        <label>flag格式</label>
                        <div class="control">
                            <input type="text" name="CompetitionFlagformat" class="input" v-model="CompetitionFlagformat">
                        </div>
                    </div>
                   
                        
                        <div class="field">
                            <div class="control">
                                <button class="button is-success">提交</button>
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
        name: 'AddCompetition',
        data(){
            return{
                CompetitionName:'',
                CompetitionRount:12,
                CompetitionRounttime:15,
                CompetitionStarttime:'',
                CompetitionFlagformat:'flag',
            }
        },
        methods:{
            async submitNewCompetition(){
                this.$store.commit('setIsLoading', true)

                const competition = {
                    name: this.CompetitionName,
                    starttime:new Date(this.CompetitionStarttime).toISOString(),
                    rounttime:this.CompetitionRounttime,
                    rountnumber:this.CompetitionRount,
                    flagformat:this.CompetitionFlagformat,


                }

                await axios
                    .post('/api/v1/competitions/', competition)
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
                
                    this.$router.push('/competition')

                this.$store.commit('setIsLoading', false)
            }
        }
            
        }
    
</script>