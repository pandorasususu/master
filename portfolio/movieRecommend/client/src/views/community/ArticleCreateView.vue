<template>
  <div id="ArticleFormView">
    <h1>새 게시글 작성</h1>
    <article-form-view :article="article" action="create"></article-form-view>
  </div>
</template>

<script>
import ArticleFormComp from '@/components/community/ArticleFormComp.vue'

export default {
name:'ArticleFormView',
components: {ArticleFormComp},
data(){
  return {
    action:{
      pk: null,
      title: '',
      content: '',
    }
  }
}
}
</script>

<style>

</style>