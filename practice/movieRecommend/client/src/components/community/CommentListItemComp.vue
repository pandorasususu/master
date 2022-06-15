<template>
  <div id="CommentListItemComp">
    <router-link :to="{ name:'profile', params: { username: comment.user.username } }">
      {{comment.user.username}}
    </router-link>
    <br>

    <span v-if="!isEditing">
    {{comment.content}} {{comment.updated_at}}
    </span>

    <span v-if="isEditing">
      
    </span>

    <span v-if="currentUser.username === comment.user.username && !isEditing">
      <button @click="SwitchIsEditing">수정</button>
      <button @click="deleteComment(commentInfo)">삭제</button>
    </span>
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'

export default {
name: 'CommentListItemComp',
props: {comment: Object},
data(){
  return {
    isEditing: false,
    commentInfo: {
      articlePk: this.comment.article,
      commentPk: this.comment.pk,
      content: this.comment.content
    }
  }
},
computed:{
  ...mapGetters(['currentUser'])
},
method:{
  ...mapActions(['updateComment', 'deleteComment']),
  SwitchIsEditing(){
    this.isEditing = !this.isEditing
  },
  submitUpdate(){
    this.updateComment(this.commentinfo)
    this.isEditing = false
  }
}
}
</script>

<style>

</style>