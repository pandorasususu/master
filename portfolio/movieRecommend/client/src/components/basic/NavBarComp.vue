<template>
  <div id="NavBarComp" class="flex-col justify-start align-middle">
    <!-- 세로방향, 상단 끝쪽에 몰려있도록, 가로 기준으로는 중앙정렬 -->
    <!-- 기본적으로 보이지 않으나 왼쪽에 마우스가 갈 시 보이고, 왼쪽 부분에서 더블 클릭 발생할 시 고정되어서 보임 -->

    <!-- 로그인 했을 때의 메뉴 -->
    <ul id="userMenu" v-if="isLoggedIn">
      <!-- 유저가 등록한 프로필 사진 -->
      <!-- 유저 이름 -->
      <!-- 로그아웃, 내 프로필 -->
      <ul>
        <li @click.prevent="logOut">LogOut</li>
      </ul>
      <li>Main</li>
      <li>Community</li>
    </ul>

    <!-- 로그인 하지 않았을 때의 메뉴 -->
    <div id="guestMenu" v-else>
      <router-link to="/login">Login</router-link>
      <router-link to="/signup">SignUp</router-link>
    </div>
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'

export default {
  name:'NavBarComp',
  computed:{
    ...mapGetters(['isLoggedIn'])
  },
  methods: {
    ...mapActions(['logOut'])
  },
}
</script>

<style>

</style>