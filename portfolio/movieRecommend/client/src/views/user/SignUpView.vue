<template>
  <div id="SignUpView">

    <user-error-list v-if="authError"></user-error-list>

    <div id="SignUpBox" class="flex flex-col justify-center align-middle">
      SignUp
      <form @submit.prevent="signUp(signUpInfo)" class="flex flex-col justify-center align-middle">
      이름: <input type="text" v-model="signUpInfo.username">
      비밀번호: <input type="password" v-model="signUpInfo.password1">
      비밀번호 확인: <input type="password" v-model="signUpInfo.password2">
      <button type="submit">회원가입</button>
      </form>
    </div>

  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import UserErrorList from '@/components/error/UserErrorList.vue'

export default {
  name:'SignUpView',
  components: {UserErrorList},
  data(){
    return{
      signUpInfo: {
        username: '',
        password1: '',
        password2: '',
      }
    }
  },
  methods:{
    ...mapActions(['signUp']),
  },
  computed:{
    ...mapGetters(['authError'])
  },
}
</script>

<style>

</style>