<template>
<div>
  <div id="app">
    <nav-bar id="nav-bar"></nav-bar>
    <div class="body">
      <router-view/>
    </div>
  </div>
</div>
</template>

<script>
  import NavBar from '@/components/home/NavBar.vue'

  import { mapActions } from 'vuex'

  export default {
    name: 'App',
    components: { NavBar },
    methods: {
      ...mapActions(['getCurrentUser', 'movieListHomeViewGet', 'movieListHomeViewGet2', 'movieListHomeViewGet3'])
    },
    created() {
      this.movieListHomeViewGet()
      this.movieListHomeViewGet2()
      this.movieListHomeViewGet3()
      this.getCurrentUser()

    }
  }
</script>

<style>

html,body {
  width: 100%;
  height: 85vh;
}

#app {
  width: 100%;
  height: 100%;
  display:flex;
  flex-direction:column;
  justify-content: center;
  align-items:center;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;

}

#nav-bar {
  position: sticky;
  z-index:1;
  width: 100%;
  top: 0;
}

/* body style */

.body {
  /* margin-top: 10vh; */
  width: 100%;
  height: 110vh;
  padding: 50px;
  /* background-color: #122333; */

  /* 어두운 테마 */
  background-color: #F9F7F7;
  /* 밝은 테마 */
  /* background-color: #F9F7F7; */

  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  /* align-items: center; */
}

/* footer style */
/*
footer{
  position: sticky;
  bottom: 0;
  width: 100%;
  padding: 10px;
  background-color: #dcdfdd;
  color:#2c3e50;
  font-weight: bold;
  display:flex;
  flex-direction:column;
  justify-content: center;
  align-items:center;
  }
*/

</style>
