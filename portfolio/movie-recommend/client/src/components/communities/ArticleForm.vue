<template>
  <div id="ArticleForm">
    <h1 id="article-form-title-create" v-if="action == '작성'"> 게시글 작성하기 <b-icon icon="pencil-fill"></b-icon></h1> 
    <h1 id="article-form-title-update" v-else-if="action == '수정'"> 게시글 수정하기 <b-icon icon="pencil-fill"></b-icon></h1> 
    <hr style="color: #112D4E;">
    <br>

    <h4 id="article-form-title-text">제목</h4> 
    <b-form id="article-form" @submit.prevent="postArticle(action)">
      <b-form-input  v-model="formArticle.title" id="article-form-title" placeholder="제목을 입력해주세요."></b-form-input>
      <br>

      <h4 id="article-form-content-text">내용</h4>
      <b-form-textarea v-model="formArticle.content" id="article-form-content" placeholder="내용을 입력해주세요." rows="6" max-rows="6"></b-form-textarea>
      <br>
      <b-button id="article-form-submit-button" type="submit" class="m-3">{{action}}</b-button>

      <router-link :to="{ name:'community'}">
        <b-button v-if="action == '작성'" id="article-form-cancel-button">취소</b-button>
      </router-link>

      <router-link :to="{ name:'article', params:{articlePk:article.pk} }">
        <b-button v-if="action == '수정'" id="article-form-cancel-button">취소</b-button>
      </router-link>
    </b-form>

    

  </div>
</template>

<script>
// 0520
// articleform에서 update할 때, 처음에는 제목과 본문에 제대로 수정되기 전의 내용이 들어오지만, 한번만 새로고침하면 바로 placeholder가 들어온다.
// vuex store의 state의 article에는 제대로 저장되어 있는데 왜 안들어올까

import { mapActions, mapGetters } from 'vuex'
export default {
  name:'ArticleForm',
  props:{article:Object, action:String},
  data(){
    return {
      formArticle: {
        title: this.article.title,
        content: this.article.content,
      }
    }
  },
  methods:{
    ...mapActions(['articleCreate', 'articleUpdate']),
    postArticle(action){
      if (action==='작성'){
        console.log(this.formArticle)
        this.articleCreate(this.formArticle)
      } else if (action==='수정'){
        const updatedArticle = {
          pk: this.article.pk,
          ...this.formArticle
        }
        console.log('여기까지오나?', updatedArticle)
        this.articleUpdate(updatedArticle)
      }
    }
  },
  computed:{
    ...mapGetters(['articleAndCommentError'])
  },
  created(){
    console.log('articleform',this.article.title)
  }
}
</script>

<style scoped>
#article-form-title, #article-form-content {
  width: 100%;
}

#article-form-title-create, #article-form-title-update{
  text-align: start;
  color: #112D4E;
}

#article-form-title-text, #article-form-content-text{
  text-align: start;
  color: #112D4E;
}

#article-form-submit-button {
  width:100px; height:50px;
  background-color: #3282B8;

}

#article-form-cancel-button{
  width:100px; height:50px;
  background-color: #B83232;
}
</style>
