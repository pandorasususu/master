<template>
  <div id="ArticleView">
    <div id="ArticleViewTop">
      <span id="article-view-top-title">{{article.title}}</span>
      <span id="article-view-top-date">작성일: {{createdDate}}ㅤ | ㅤ수정일: {{updatedDate}}</span>
      <router-link :to="{ name: 'profile', params: goToUserPRofile }">
        <b-button id="user-button" variant="light"><b-icon icon="person-fill"></b-icon> {{article.user.username}}</b-button>  
      </router-link>
    </div>
    <hr>

    <div id="ArticleViewMiddle">
      <p>{{article.content}}</p>
    </div>
    <hr>

    <div id="article-view-middle-buttons">
      <b-button id="like-button" v-if="!isAuthor" @click="articleLike(article.pk)">{{isLikedButton}}  {{article.like_users.length}}</b-button>
      
      <router-link v-if="isAuthor" :to="{ name:'ArticleUpdate', params:{articlePk} }">
        <b-button id="article-view-update-button" class="m-3">수정하기 <b-icon icon="pencil-square"></b-icon></b-button>
      </router-link>

      <b-button v-if="isAuthor" variant="danger" id="article-view-delete-button" type="submit" @click="articleDelete(articlePk)">삭제하기 <b-icon icon="trash"></b-icon></b-button>

      <router-link :to="{ name: 'community' }">
        <b-button id="article-view-back-button" class="m-3">글 목록 <b-icon icon="list-task"></b-icon></b-button>
        </router-link>
    </div>
    <hr>
    <div id="ArticleViewBottom">
      <article-and-comment-error-list v-if="articleAndCommentError"> </article-and-comment-error-list>
      <comment-list v-for="comment in article.comments" :key="comment.pk" :comment="comment"></comment-list>
      <br>
      <comment-create-form></comment-create-form>
    </div>
    
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import CommentList from '@/components/communities/CommentList.vue'
import CommentCreateForm from '@/components/communities/CommentCreateForm.vue'
import ArticleAndCommentErrorList from '@/components/communities/ArticleAndCommentErrorList.vue'

export default {
  name: 'ArticleView',
  components: {CommentList, CommentCreateForm, ArticleAndCommentErrorList},
  data(){
    return {
      articlePk: this.$route.params.articlePk,
    }
  },
  computed:{
    ...mapGetters(['article', 'isAuthor', 'articleAndCommentError', 'currentUser']),
    goToUserPRofile(){
      return {username: this.article.user.username}
    },
    createdDate(){
      const dateText = this.article.created_at
      const year = dateText.split('T')[0].substring(0,4)
      const month = dateText.split('T')[0].substring(5,7)
      const day = dateText.split('T')[0].substring(8,10)
      const hour = dateText.split('T')[1].substring(0,2)
      const minute = dateText.split('T')[1].substring(3,5)
      const second = dateText.split('T')[1].substring(6,8)
      return `${year}. ${month}. ${day} ${hour}: ${minute}: ${second}`
    },
    updatedDate(){
      const dateText = this.article.updated_at
      const year = dateText.split('T')[0].substring(0,4)
      const month = dateText.split('T')[0].substring(5,7)
      const day = dateText.split('T')[0].substring(8,10)
      const hour = dateText.split('T')[1].substring(0,2)
      const minute = dateText.split('T')[1].substring(3,5)
      const second = dateText.split('T')[1].substring(6,8)
      return `${year}. ${month}. ${day} ${hour}: ${minute}: ${second}`
    },
    isLikedButton(){
      if(this.article.like_users.find(e => e.pk === this.currentUser.pk)){
        return '❤️'
      } else{ 
        return '🤍'
      }
    }
  },
  methods:{
    ...mapActions(['articleGet', 'articleDelete', 'articleLike']),
  },
  created(){
    this.articleGet(this.articlePk)
  }
}
</script>

<style>

#ArticleView {
  width: 100%;
  display: flex;  
  flex-direction: column;
  justify-content:space-between;
  font-size: 20px;
  color: #112D4E;
}

#ArticleViewTop {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

#article-view-top-title{
  font-size:40px;
  font-weight:bold;
}

#article-view-top-date{
  font-size: 15px;
}

#ArticleViewMiddle{
  height: 300px;
  width: 100%;
  padding: 10px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-top: 10px;
  margin-bottom: 10px;
  background-color: #F9F7F7;
}

#like-button{
  background-color:transparent;
  color: black;
}

#article-view-update-button{
  width:120px; height:50px;
  background-color: #3282B8;
}

#article-view-delete-button{
  width:120px; height:50px;
  background-color: #B83232;
}

#article-view-back-button{
  width:120px; height:50px;
  background-color: #5fb832;
}

#article-view-middle-buttons{
  width: 100%;
  margin-top: 10px;
  margin-bottom: 10px;
}

#ArticleViewBottom {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;  
  margin-top: 10px;
  margin-bottom: 10px;
}

#ArticleViewBottom a{
  align-self: flex-end;
}

#CommentList {
  width: 100%;
  text-align:start;
  margin-top: 5px;
  margin-bottom: 5px;  
}
</style>

