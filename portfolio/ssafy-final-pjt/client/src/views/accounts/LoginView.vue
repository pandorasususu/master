<template>
  <div id="LoginView">
    <h2>로그인</h2>
    <hr>
    <account-error-list v-if="authError"></account-error-list>
    <br>
    <form @submit.prevent="login(credentials)">
      <div>
        <label for="loginform-username">이름ㅤ</label> 
        <input type="text" v-model="credentials.username" id="loginform-username" class="mb-3">
        <label for="loginform-password">비밀번호ㅤ</label> 
        <input type="password" v-model="credentials.password" id="loginform-password" class="mb-5">
        <button id="login-button">로그인</button>
      </div>
    </form>
    <br>
    계정이 없으신가요?ㅤ
    <router-link :to="{ name: 'signup' }" style="color: #F21170">회원가입</router-link>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import AccountErrorList from '@/components/accounts/AccountErrorList.vue'

export default {
  name : 'LoginView',
  components: { AccountErrorList },
  data : function(){
    return {
      credentials:{
        username : '',
        password : '',
      }
    }
  },
  methods : {
    ...mapActions(['login'])
  },
  computed:{
    ...mapGetters(['authError'])
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap');

#LoginView{
  align-content: center;
  width: 300px;
  height: 480px;
  border: 1px solid; 
  padding:30px; 
  background-color:white; 
  color:black;
  margin:0 auto;
  border-radius: 20px;
  font-family: 'Gowun Dodum', sans-serif;
}

#loginform-username, #loginform-password{
  background-color: #F7F7F7;
  border-radius: 3px;
  border-width: 1px;
  width: 100%;
}

#login-button{
  background-color: #F21170;
  width: 100%;
  height: 50px;
  color: white;
  border-width: 0px;
  border-radius: 5px;
}
</style>