<template>
  <div id="LoginView">
    <div id="LoginBox" class="flex flex-col justify-center align-middle">
      Login
      <form @subimt.prevent="logIn(LogInInfo)" class="flex flex-col justify-center align-middle">
      username: <input type="text" v-model="LogInInfo.username">
      password: <input type="text" v-model="LogInInfo.password">
      <button type="submit">로그인</button>
      </form>
    </div>
  </div>
</template>

<script>
import {mapActions} from 'vuex'

export default {
  name:'LoginView',
  data(){
    return{
      LogInInfo: {
        username: '',
        password: '',
      }
    }
  },
  methods:{
    ...mapActions(['logIn']),
  },
  computed:{

  },
}
</script>

<style>

</style>