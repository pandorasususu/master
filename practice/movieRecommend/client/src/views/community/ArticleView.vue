<template>
  <div id="ArticleView">
    제목: {{article.title}}
    <br>
    작성자: {{article.user.username}}
    <br>
    작성일: {{article.created_at}}
    수정일: {{article.updated_at}}
    <br><br><hr><br><br>
    내용
    <br>
    {{article.content}}

    <hr><br>
    <comment-list-comp :comments="article.comments"></comment-list-comp>

  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import CommentListComp from '@/components/community/CommentListComp.vue'

export default {
name:'ArticleView',
components: {CommentListComp},
methods: {
  ...mapActions('setArticle'),
},
computed:{
  ...mapGetters('article')
},
created(){
  this.setArticle(this.$route.params.articlePk)
}
}
</script>

<style>

</style>