<template>
  <div id="UserProfileView">
    {{userProfile.data.username}}의 프로필 <br>
    팔로잉 수: {{userProfile.data.followings.length}}명 <br>
    팔로워 수: {{userProfile.data.followers.length}}명 <br>

    내가 쓴 게시글 
    <br>
    {{userProfile.data.articles}}
    <br>

    내가 쓴 댓글
    <br>
    {{userProfile.data.comments}}
    <br>

    내가 좋아한 게시글
    <br>
    {{userProfile.data.like_articles}}
    <br>

    내가 좋아한 댓글
    <br>
    {{userProfile.data.like_comments}}

  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
export default {
  name: 'UserProfileView',
  methods: {
    ...mapActions(['getUserProfile'])
  },
  computed: {
    ...mapGetters(['userProfile', 'currentUser'])
  },
  created(){
    // 최종 과제에서는 username을 object로 넘겨줌.
    // 하지만 그렇게 해야 될 이유가 없는 거 같아 username만 넘겨줘보는 걸로
    const username = this.$route.params.username
    console.log('created', username)
    this.getUserProfile(username)
  }
}
</script>

<style>

</style>
