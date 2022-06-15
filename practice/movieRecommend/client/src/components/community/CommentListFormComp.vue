<template>
  <div id="CommentListFormCom">
    <form @submit.prevent="">
      제목
      <br>
      <input type="text">
      <br>
      본문
      <br>
      <input type="text">
    </form>
  </div>
</template>

<script>
export default {
name: 'CommentListFormCom',
data(){
  return{
    article: {
      pk: null,
      title: '',
      
    }
  }
}
}
</script>

<style>

</style>