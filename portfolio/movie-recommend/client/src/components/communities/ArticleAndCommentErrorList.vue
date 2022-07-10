<template>
  <div id="ArticleAndCommentErrorList">
    <p v-for="(errors, field) in articleAndCommentError" :key="field">
      <ul>
        <li v-for="(error, idx) in errors" :key="idx">
          {{error}}
        </li>
      </ul>
    </p>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  name:'ArticleAndCommentErrorList',
  computed:{
    ...mapGetters(['articleAndCommentError'])
  }
}
</script>

<style>

</style>