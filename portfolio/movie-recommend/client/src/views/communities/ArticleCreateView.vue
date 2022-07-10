<template>
  <div id="ArticleCreateView">
    <article-and-comment-error-list v-if="articleAndCommentError"> </article-and-comment-error-list>
    <article-form :article="article" action="작성"></article-form>
  </div>
</template>

<script>
import ArticleForm from '@/components/communities/ArticleForm.vue'
import ArticleAndCommentErrorList from '@/components/communities/ArticleAndCommentErrorList.vue'
import {mapGetters} from 'vuex'

export default {
  name: 'ArticleCreateView',
  components: { ArticleForm, ArticleAndCommentErrorList },
  data(){
    return {
      article: {
        title: '', 
        content: '',
      }
    }
  },
  computed:{
    ...mapGetters(['articleAndCommentError'])
  }
}
</script>

<style scoped>
#ArticleCreateView {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content:flex-start;
}


</style>
