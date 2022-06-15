<template>
  <div id="SignUpView">
    <h2>회원가입</h2>
    <hr>
    <account-error-list v-if="authError"></account-error-list>
    <br>
    <form @submit.prevent="signUp(credentials)">
      <label for="signupform-username">이름ㅤ</label> 
      <input type="text" id="signupform-username" v-model="credentials.username" class="mb-3">
      <label for="signupform-password1">비밀번호ㅤ</label> 
      <input type="password" id="signupform-password1" v-model="credentials.password1" class="mb-3">
      <label for="signupform-password2">비밀 번호 확인ㅤ</label> 
      <input type="password" id="signupform-password2" v-model="credentials.password2" class="mb-5">
      <button id="signup-button">회원가입</button>
    </form>
    <br>
    이미 가입하셨나요?ㅤ
    <router-link :to="{ name: 'login' }" style="color: #F21170">로그인</router-link>
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'
import AccountErrorList from '@/components/accounts/AccountErrorList.vue'

export default {
  name:'SignUpView',
  components: { AccountErrorList },
  data(){
    return {
      credentials: {
        username: '',
        password1: '',
        password2: ''
      }
    }
  },
  computed:{
    ...mapGetters(['authError', 'isLoggedIn'])
  },
  methods:{
    ...mapActions(['signUp']),
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap');

#SignUpView{
  align-content: center;
  width: 300px;
  height: 480px;
  border: 1px solid; 
  padding:30px; 
  background-color: white; 
  color:black;
  margin:0 auto;
  border-radius: 20px;
  font-family: 'Gowun Dodum', sans-serif;
}

#signupform-username, #signupform-password1, #signupform-password2{
  background-color: #F7F7F7;
  border-radius: 3px;
  border-width: 1px;
  width: 100%;
}

#signup-button{
  background-color: #F21170;
  width: 100%;
  height: 50px;
  color: white;
  border-width: 0px;
  border-radius: 5px;
}

</style>