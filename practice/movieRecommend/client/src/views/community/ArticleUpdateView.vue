<template>
  <div id="ArticleUpdateView">
    <h1>게시글 수정</h1>
    <article-form-view v-if="isArticle" :article="article" action="update"></article-form-view>

  </div>
</template>

<script>
import ArticleFormView from '@/components/community/ArticleFormComp.vue'
import {mapActions, mapGetters} from 'vuex'

export default {
name: 'ArticleUpdateView',
components: {ArticleFormView},
methods: {
  ...mapActions(['setArticle'])
},
computed:{
  ...mapGetters(['article', 'isArticle'])
},
created(){
  this.setArticle(this.$route.params.articlePk)
}
}
</script>

<style>

</style>