<template>
  <div id="TodoForm">
    <input id="todoInput" type="text" placeholder="오늘 해야 할 일을 입력하세요." v-model="inputTitle" @keyup.enter="createTodo">
    중요<input id="importantCheckbox" type="checkbox" v-model="importantCheck" @keyup.enter="checkboxCreate">

  </div>
</template>

<script>

export default {
  name: 'todoForm',
  data(){
    return{
      newTodo:{},
      inputTitle: '',
      importantCheck: false,
    }
  },
  methods: {
    createTodo() {
      const newTodo = {
        title: this.inputTitle,
        isCompleted: false,
        isImportant: this.importantCheck,
        createdDate: new Date().getTime(),
        updatedDate: new Date().getTime(),
      }
      if (!newTodo.title){
        confirm('할 일을 입력해주세요.')
      } else{
        this.$store.dispatch('createTodo', newTodo)
        this.inputTitle = ''
        this.importantCheck =  false
      }
    },
    checkboxCreate(){
      this.importantCheck=!this.importantCheck
      this.createTodo()
    },
  },
  }

</script>

<style>
#todoInput{
  border:0px;
  padding:0px;
  width: 300px;
  height: 30px
}

#importantCheckbox{
  margin:0px;
  border:0px;
  padding:0px;
}
</style>