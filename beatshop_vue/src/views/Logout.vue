<template>
    <div>
      <h1>Logging out...</h1>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    name: 'Logout',
    mounted() {
      this.logout();
    },
    methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")

            this.$store.commit('removeToken')

            this.$router.push('/')
        },
    }
  }
  </script>
  