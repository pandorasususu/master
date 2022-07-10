<template>
  <div id="CommentList">
    <template v-if="!isUpdating"> 
      <div class="bubble mb-3"> 
        <p class="m-3">{{comment.content}}</p>         
      </div>
    </template>
    <div>
      <h5><b-icon icon="person-fill"></b-icon> {{comment.user.username}}</h5>
    </div>
    
    

      <template v-if="comment.user.username == currentUser.username" >
        <template v-if="isUpdating">
          <b-form-input v-model="commentContent" type='text'></b-form-input>
          <b-button @click="pushUpdate" variant="link" id="comment-button">등록</b-button>
          | 
          <b-button @click="quitUpdate" variant="link" id="comment-button">취소</b-button>
        </template>

        <template v-if="!isUpdating"> 
          <b-button @click="startUpdate" variant="link" id="comment-button">수정</b-button>
          | 
          <b-button @click="pushDelete" variant="link" id="comment-button">삭제</b-button>
        </template>
      </template>

    
    
    <br>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'

export default {
  name: 'CommentList',
  props:{
    comment: Object
  },
  data(){
    return{
      commentContent: this.comment.content,
      isUpdating: false
    }
  },
  methods:{
    ...mapActions(['commentUpdate', 'commentDelete']),
    pushDelete(){
      const payloadDelete = {
        articlePk: this.article.pk,
        commentPk: this.comment.pk
      }
      this.commentDelete(payloadDelete)
      console.log(payloadDelete)
    },
    pushUpdate(){
      const payloadUpdate = {
        articlePk: this.article.pk,
        commentPk: this.comment.pk,
        content: this.commentContent,
      }
      this.commentUpdate(payloadUpdate)
      this.isUpdating = !this.isUpdating
    },
    startUpdate(){
      this.isUpdating = true
    },
    quitUpdate(){
      this.isUpdating = false
    }
  },
  computed:{
    ...mapGetters(['currentUser', 'article']),
  }
}
</script>

<style>
.bubble
{
position: relative;
width: 500px;
height: 50px;
padding: 0px;
background: #e2dfdf;
-webkit-border-radius: 10px;
-moz-border-radius: 10px;
border-radius: 10px;
text-align: left;
}

.bubble:after
{
content: '';
position: absolute;
border-style: solid;
border-width: 15px 15px 0;
border-color: #e2dfdf transparent;
display: block;
width: 0;
z-index: 1;
bottom: -15px;
left: 12px;
}

#comment-button{
  padding: 0px;
}
</style>