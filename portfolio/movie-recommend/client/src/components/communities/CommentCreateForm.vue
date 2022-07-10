<template>
  <div id="CommentCreateView">
    <b-form @submit.prevent="pushcc">
      <b-form-input v-model="commentContent" type="text" placeholder="댓글을 입력해주세요."></b-form-input>
      <b-button type="submit">댓글 등록</b-button>
    </b-form>    
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentCreateView',
  data(){
    return {
      commentContent: '',
    }
  },
  methods:{
    ...mapActions(['commentCreate']),
    pushcc(){
      const payload = {
        articlePk: this.article.pk,
        content: this.commentContent,
      }
      this.commentCreate(payload)
      this.commentContent = ''
    }
  },
  computed:{
    ...mapGetters(['article'])
  },
}
</script>

<style>

#CommentCreateView{
  width: 100%;
}

#CommentCreateView input{
  width: 93%;
  margin: 0;
  display: inline-block;
}

#CommentCreateView button{
  align-self: flex-end;
}

</style>