<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <strong>BeatStore</strong>
        </router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <div v-if="isUserLoggedIn">
                <router-link to="/account" class="button is-info mr-3">
                  <span class="mr-2"><i class="fa-solid fa-user"></i></span>
                  <span>My account</span>
                </router-link>
                <router-link to="/logout" class="button is-danger mr-3">
                  <span class="icon"><i class="fa-solid fa-right-from-bracket"></i></span>
                  <span>Log out</span>
                </router-link>
              </div>
              <div v-else>
                <router-link to="/sign-up" class="button is-info mr-3">
                  <span class="icon"><i class="fa-regular fa-id-card"></i></span>
                  <span>Sign up</span>
                </router-link>
                <router-link to="/log-in" class="button is-info mr-3">
                  <span class="icon"><i class="fa-solid fa-right-to-bracket"></i></span>
                  <span>Log in</span>
                </router-link>
              </div>
              
              <router-link to="/cart" class="button is-success">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart {{ cartTotalLength }}</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading}">
      <div class="lds-dual-ring"></div>
    </div>

    <section class="section">
      <router-view/>
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2023</p>
      <p class="has-text-centered">Created by <a href="https://github.com/ChrissO2">Krzysztof Otręba</a></p>
    </footer>
  </div>
  
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: [],
      }
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token
    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
    this.auth = this.$store.state.isAuthenticated
  },
  computed: {
    cartTotalLength() {
      return this.$store.state.cart.items.length
    },
    isUserLoggedIn() {
      return this.$store.state.isAuthenticated
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}

</style>
