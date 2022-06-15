<template>
  <div id="ArticleUpdateView">
    <article-and-comment-error-list v-if="articleAndCommentError"> </article-and-comment-error-list>
    <article-form v-if="isArticle" :article="article" action="수정"></article-form>
  </div>
</template>

<script>
import ArticleForm from '@/components/communities/ArticleForm.vue'
import ArticleAndCommentErrorList from '@/components/communities/ArticleAndCommentErrorList.vue'
import {mapGetters, mapActions} from 'vuex'

export default {
  name:'ArticleUpdateView',
  components: { ArticleForm, ArticleAndCommentErrorList },
  computed:{
    ...mapGetters(['article', 'isArticle', 'articleAndCommentError'])
  },
  methods:{
    ...mapActions(['articleGet'])
  },
  created(){
    this.articleGet(this.$route.params.articlePk)
    console.log('articleupdateviewcreated',this.article.title)
  },
}
</script>

<style scoped>
#ArticleUpdateView {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content:flex-start;
}
</style>
