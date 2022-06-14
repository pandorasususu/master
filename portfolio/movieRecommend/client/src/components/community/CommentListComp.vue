<template>
  <div id="CommentListComp">
    <h3>댓글 목록</h3>
    <comment-list-item-comp
    v-for="comment in comments"
    :comment="comment"
    :key="comment.pk">
    </comment-list-item-comp>

    <comment-list-form-comp></comment-list-form-comp>
  </div>
</template>

<script>
import CommentListItemComp from '@/components/community/CommentListItemComp.vue'
import CommentListFormComp from '@/components/community/CommentListFormComp.vue'

export default {
name:'CommentListComp',
components: {CommentListItemComp, CommentListFormComp},
props: {
  comments:Array
}
}
</script>

<style>

</style>