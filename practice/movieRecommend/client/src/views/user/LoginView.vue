<template>
  <div id="LoginView">

    <user-error-list v-if="authError"></user-error-list>
    <div id="LoginBox" class="flex flex-col justify-center align-middle">
      Login
      <form @submit.prevent="logIn(LogInInfo)" class="flex flex-col justify-center align-middle">
      이름: <input type="text" v-model="LogInInfo.username">
      비밀번호: <input type="password" v-model="LogInInfo.password">
      <button type="submit">로그인</button>
      </form>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import UserErrorList from '@/components/error/UserErrorList.vue'

export default {
  name:'LoginView',
  components: {UserErrorList},
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
    ...mapGetters(['authError'])
  },
}
</script>

<style>

</style>