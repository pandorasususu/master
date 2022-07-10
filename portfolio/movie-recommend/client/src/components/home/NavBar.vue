<template>
  <div id="NavBar">
    
  <b-navbar toggleable="lg">
    <router-link to="/">
        <div class="mx-3">
          <img id="navicon" src="../../assets/movie.png" width="100" height="90" class="m-3 d-inline-block align-center justify-content-center" alt="logo">
        </div>
      </router-link>
    <b-navbar-brand class="navstart">
      
    </b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav class="navend">
        <router-link to="/">HOME</router-link>
        <router-link :to="{ name: 'movies' }">MOVIES</router-link>
        <router-link to="/community">COMMUNITY</router-link>
        <router-link v-if="!isLoggedIn" to="/login">LOGIN</router-link> 
        <router-link v-if="isLoggedIn && username " :to="{ name: 'profile', params: {username} }">MYPAGE</router-link> 
        <div v-if="isLoggedIn" @click="logout">LOGOUT</div> 
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>

  </div>
</template>

<script>
import { mapGetters, mapActions} from 'vuex'

export default {
  name: 'NavBar',
  methods: {
    ...mapActions(['logout'])
  },
  computed:{
    ...mapGetters(['isLoggedIn', 'currentUser']),
    username(){
      return this.currentUser.username
    }
  },
}
</script>

<style>
.navbar {
  position: sticky;
  top: 0;
  height: 8vh;
  width: 100%;
  display:flex;
  flex-direction:row;
  justify-content: space-between;
  align-items:center;
  background-color: #3F72AF;
}

.navbar-collapse{
  background-color: #dcdfdd;
}

.navstart{
  height:80%;
  width:50%;
  display: flex;
  flex-direction: row;
  justify-content: baseline;
  align-items: center;
  margin-left: 70px;
}

.navbar-brand a div{
  color: #bac6cb;
}

.navstart a {
  text-decoration: none;
}

.navicon{
  height:30%;
  width:30%;
}

.navbar-nav a, .navbar-nav div {
  margin-left: 70px;
  text-decoration: none;
  font-size: 20px;
  font-weight: bold;
  color: #DBE2EF;
}

.navend{
  background-color: #3F72AF;
  display: flex;
  justify-self: end;
  padding: 0;
}

.navbar-nav{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: flex-end;
  margin-right: 10px;
}

.navbar-toggler{
  margin-right: 70px;
}

.navbar-collapse{
  background-color: #3F72AF;
  display: flex;
  justify-content: flex-end;
  margin-right: 70px;
}

nav a:hover{
  color: #e8c171;
  transition:all.5s;
}

nav div a.router-link-exact-active {
  color: #e8c171;
  border-bottom: 3px solid;
}
</style>