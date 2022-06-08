<template>
  <div id="NavBarComp" class="flex-col justify-start align-middle">
    <!-- 세로방향, 상단 끝쪽에 몰려있도록, 가로 기준으로는 중앙정렬 -->
    <!-- 기본적으로 보이지 않으나 왼쪽에 마우스가 갈 시 보이고, 왼쪽 부분에서 더블 클릭 발생할 시 고정되어서 보임 -->
    <!-- 로그인 하지 않았을 때의 메뉴 -->
    <ul id="guestMenu">
      <li>Login</li>
    </ul>

    <!-- 로그인 했을 때의 메뉴 -->
    <ul id="userMenu">
      <!-- 유저가 등록한 프로필 사진 -->
      <!-- 유저 이름 -->
      <!-- 로그아웃, 내 프로필 -->
      <li>Main</li>
      <li>Community</li>
    </ul>

  </div>
</template>

<script>
export default {
  name:'NavBarComp',
  
}
</script>

<style>

</style>