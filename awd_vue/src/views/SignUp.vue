<template>
<div>
<div>
            <section class="hero is-black is-small pb-6">
                <div class="hero-body container is-max-desktop">
                  <p class="title  ">
                    {{ $t("register.Title") }}
                  </p>
                </div>
              </section>
        </div>
    <div class="container is-max-desktop pr-6 pl-6">
        <div class="notification has-background-dark has-text-white">
            <section class="section">    
                <form  @submit.prevent="submitForm">
                    <div class="field">
                      <div class="control">
                        <h4 class="title is-4">{{$t('register.Username')}}</h4>
                        <input class="input is-medium is-rounded" name="username" v-model="username"/>
                      </div>
                    </div>
                    <div class="field">
                      <div class="control">
                        <h4 class="title is-4">{{$t('register.Emali')}}</h4>
                        <input class="input is-medium is-rounded" name="password" type="email" v-model="email"/>
                      </div>
                    </div>
                    <div class="field">
                      <div class="control">
                        <h4 class="title is-4">{{$t('register.Password')}}</h4>
                        <input class="input is-medium is-rounded" name="password" type="password" v-model="password1"/>
                      </div>
                    </div>
                    <div class="field">
                      <div class="control">
                        <h4 class="title is-4">{{$t('register.TwoPassword')}}</h4>
                        <input class="input is-medium is-rounded" name="password" type="password" v-model="password2"/>
                      </div>
                    </div>
                    <br />
                    
                    <button class="button is-block  is-primary is-medium is-rounded is-pulled-right" type="submit">
                        {{ $t("register.Submit") }}
                    </button>
                    
                  </form>
            
              </section>
        </div>
    </div>
</div>
</template>


<script>
import axios from 'axios'

export default {
    name:'SignUp',
    data(){
        return{
            username:'',
            email:'',
            password1:'',
            password2:'',
            errors:[]
        }
    },
    methods:{
        async submitForm(){
            this.errors=[]
           
                if (this.username === '') {
                    this.errors.push('The username is missing')
                }

                if (this.password1 === '') {
                    this.errors.push('The password is too short')
                }

                if (this.password1 !== this.password2) {
                    this.errors.push('The password are not matching')
                }

                if (!this.errors.length) {
                
                    const formData = {
                        username: this.username,
                        email:this.email,
                        password: this.password1
                    }

                    await axios
                        .post('/api/v1/users/', formData)
                        .then(response => {
                            toast({
                                message: 'Account was created, please log in',
                                type: 'is-success',
                                dismissible: true,
                                pauseOnHover: true,
                                duration: 2000,
                                position: 'bottom-right',
                            })

                            this.$router.push('/login')
                        })
                        .catch(error => {
                            if (error.response) {
                                for (const property in error.response.data) {
                                    this.errors.push(`${property}: ${error.response.data[property]}`)
                                }
                            } else if (error.message) {
                                this.errors.push('Something went wrong. Please try again!')
                            }
                        })
                     
                }
            
        }
    }
}
</script>