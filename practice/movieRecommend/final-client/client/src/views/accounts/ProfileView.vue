<template>
  <div id="main">
    <div id="Profile-basic" class="mb-5">
      <img id="profileicon" src="../../assets/profile2.png" width="100" height="100" alt="profilelogo" class="m-3">
      <h1 align="center">{{userProfile.username}}</h1>
      <br>
      <!-- <h5 align="center"><b-icon icon="envelope"></b-icon> {{userProfile.email}}</h5> -->
      <!-- <b-button v-if="userProfile.username == currentUser.username" @click="userDelete(userProfile.username)">회원탈퇴</b-button> -->
      <h5  id="follow"><b-icon icon="people"></b-icon> 팔로워 {{followers}} ㅤ|ㅤ <b-icon icon="people"></b-icon> 팔로잉 {{followings}}</h5>
      <!-- 내가 아닌 타유저 팔로우 기능 -->
      <b-button variant="primary" v-if="userProfile.username != currentUser.username" @click="userFollow" class="mt-2">
        {{followButton}}
      </b-button>
    </div>
    <hr style="color: black; margin: 0px;">

    <!-- 내가 쓴 게시글 -->
    <div id="Profile-main">
      <div style="background-color: #DBE2EF; text-align: left; font-size: 20px;">작성한 게시글 {{ userArticleList.length }} ㅤ|ㅤ 작성한 댓글 {{ userCommentList.length }} </div>
      <hr style="color: black; margin: 0px;">
      <br>
      <br>
      <div id="profile-article">
        <h5 v-if="userProfile.username == currentUser.username" style="float: left;">내가 작성한 게시글 🖊️</h5>
        <h5 v-else style="float: left;">{{userProfile.username}}가 작성한 게시글 🖊️ </h5>
        <template v-if="userArticleList == []">
          아직 작성한 게시글이 없습니다.
        </template>
        <template v-else> 
          <b-table id="profile-article-table" 
          :per-page="perPage" 
          :total-rows="articleRows"
          :current-page="currentArticlePage"
          :fields="articleField"
          hover
          @row-clicked="articleOnRowClicked"
          primary-key="pk"
          :items="userArticleList"
          style="text-align:center;">
          </b-table>
          <!-- <b-pagination align="center"
            v-model="currentArticlePage"
            :total-rows="articleRows"
            :per-page="perPage"
            aria-controls="profile-article-table">
          </b-pagination> -->
        </template>
      </div>

      <br>
      <hr>
      <br>

      <!-- 내가 쓴 댓글 -->
      <div id="profile-comment">
        <h5 v-if="userProfile.username == currentUser.username" style="float: left;">내가 작성한 댓글 💬</h5>
        <h5 v-else style="float: left;">{{userProfile.username}}가 작성한 댓글 💬</h5>
        <br>
        <template v-if="userCommentList"> 
          <b-table id="profile-comment-table" 
            :fields="commentFields"
            :per-page="perPage" 
            :total-rows="commentRows"
            :current-page="currentCommentPage"
            hover 
            @row-clicked="commentOnRowClicked"
            primary-key="pk"
            :items="userCommentList">
          </b-table>
          <!-- <b-pagination
            v-model="currentCommentPage"
            :total-rows="commentRows"
            :per-page="perPage"
            aria-controls="profile-comment-table"
            align="center">
          </b-pagination> -->
        </template>
        <template v-if="!userCommentList">
          아직 작성한 댓글이 없습니다.
        </template>
      </div>
      <br>
    </div>

    <hr style="color: black;">
    <br>
    
    <!-- 내가 추천한 게시글 -->
    <div id="profile-like">
      <h5 v-if="userProfile.username == currentUser.username" style="float: left; color: black;">내가 추천한 게시글 😊</h5>
      <h5 v-else style="float: left; color: black;">{{userProfile.username}}가 추천한 게시글 😊 </h5>
      <br>
      <template v-if="userLikeArticleList"> 
        <b-table id="profile-like-table" 
          :fields="articleLikeFields"
          :per-page="perPage"
          hover
          :total-rows="likeArticleRows"
          :current-page="currentLikeArticlePage"
          @row-clicked="articleLikeOnRowClicked"
          :items="userLikeArticleList">
        </b-table>
        <!-- <b-pagination
          v-model="currentLikeArticlePage"
          :total-rows="likeArticleRows"
          :per-page="perPage"
          aria-controls="profile-like-article-table"
          align="center">
        </b-pagination> -->
      </template>

        <template v-if="!userLikeArticleList">
          아직 추천한 게시글이 없습니다.
        </template>
    </div>
      

    


    <!-- 내가 추천한 댓글 -->
    <!-- <div id="profile-like-comment-list">
    <p v-if="userProfile.username == currentUser.username">내가 추천한 댓글 </p>
    <p v-else>{{userProfile.username}}가 추천한 댓글 </p>

    <template v-if="userLikeCommentList"> 
      <b-table id="profile-like-comment-table" 
      :per-page="perPage" 
      :total-rows="likeCommentRows"
      :current-page="currentLikeCommentPage"
      striped 
      hover 
      :items="userLikeCommentList">
      </b-table>
      <b-pagination
      v-model="currentLikeCommentPage"
      :total-rows="likeCommentRows"
      :per-page="perPage"
      aria-controls="profile-like-comment-table">
      </b-pagination>
    </template>

    <template v-if="!userLikeCommentList">
      {{userLikeCommentList}}
      아직 추천한 댓글이 없습니다.
    </template>
    </div> -->
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'

export default {
  name: 'ProfileView',
  data(){
    return {
      currentArticlePage: 1,
      currentCommentPage: 1,
      currentLikeArticlePage: 1,
      currentLikeCommentPage: 1,
      perPage: 5,
      articleField: [
        {key: 'pk', thClass: 'd-none', tdClass: 'd-none'},
        {key: 'title',label: '제목'},
        {key: 'content', thClass: 'd-none', tdClass: 'd-none'},
      ],
      commentFields: [
        {key: 'pk', thClass: 'd-none', tdClass: 'd-none'},
        {key: 'content', label:'내용'},
        {key: 'article', thClass: 'd-none', tdClass: 'd-none'}
      ],
      articleLikeFields: [
        {key: 'pk', thClass: 'd-none', tdClass: 'd-none'},
        {key: 'title', label:'제목'},
        {key: 'content', thClass: 'd-none', tdClass: 'd-none'},
      ],
    }
  },
  methods: {
    ...mapActions(['getUserProfile', 'userFollow', 'userDelete']),
    articleOnRowClicked(item){
      this.$router.push({ name: 'article', params: { articlePk: item.pk } })
    },
    commentOnRowClicked(item){
      this.$router.push({ name: 'article', params: { articlePk: item.article } })
    },
    articleLikeOnRowClicked(item){
      this.$router.push({ name: 'article', params: { articlePk: item.pk } })
    },
  },
  computed:{
    ...mapGetters(['userProfile', 'currentUser']),
    followers(){
      return this.userProfile.followers ? this.userProfile.followers.length : 0
    },
    followings(){
      return this.userProfile.followings ? this.userProfile.followings.length : 0
    },
    followButton(){
      if(this.userProfile.followers.find(e => e === this.currentUser.pk)){
        return '팔로우 취소'
      } else {
        return ' 팔로우'
      }
    },

    userArticleList(){
      return this.userProfile.articles
    },
    userCommentList(){
      return this.userProfile.comments
    },
    userLikeArticleList(){
      return this.userProfile.like_articles
    },
    userLikeCommentList(){
      return this.userProfile.like_comments
    },

    articleRows() {
      return this.userArticleList.length
    },
    commentRows(){
      return this.userCommentList.length
    },
    likeArticleRows() {
      return this.userLikeArticleList.length
    },
    likeCommentRows(){
      return this.userLikeCommentList.length
    },
  },
  created(){
    const username = {username: this.$route.params.username} 
    this.getUserProfile(username)
  }

}
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap');

#main{
  font-family: 'Gowun Dodum', sans-serif;
}

#Profile-basic{
  border: 1px solid; 
  padding:30px; 
  background-color:#F9F7F7;
  color:black; 
  padding:none;
  border-radius: 10px;
}
#Profile-basic, #Profile-main{
  color: black;
}

#profile-article-table, #profile-comment-table, #profile-like-table{
  background-color: #F9F7F7;
  color: #112D4E;
  border: 1px solid;
  border: 1px solid #112D4E;
  border-color: #112D4E;
}
</style>