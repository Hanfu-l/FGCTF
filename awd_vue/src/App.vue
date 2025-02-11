<template>

  <Navbar />
  <router-view/>

</template>
<script>
  import axios from 'axios'

import Navbar from '@/components/layout/Navbar'
import Footer from '@/components/layout/Footer'

export default {
    name: 'App',
    components: {
        Navbar,
     
    },
    beforeCreate() {
        this.$store.commit('initializeStore')

        if (this.$store.state.token) {
            axios.defaults.headers.common['Authorization'] = "Token " + this.$store.state.token
        } else {
            axios.defaults.headers.common['Authorization'] = ""
        }
    },
}
</script>

<style lang="scss">

@import '../node_modules/bulma';
</style>
