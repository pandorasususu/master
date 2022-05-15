<template>
  <div id="app">
    <button id="cleanTodoButton" @click="cleanTodo">전체 삭제</button>
    <br><br><br>
    <div id="topDiv">
      <h1>Todo List: {{totalTodosCount}}</h1>
      <p>Completed Todos: {{completedTodosCount}}</p>
      <p>Uncompleted Todos: {{uncompletedTodosCount}}</p>
      <p>Important Todos: {{importantTodosCount}}</p>
    </div>
    <br>
    <todo-form></todo-form> 
    <br>
    <todo-list></todo-list>
  </div>

</template>

<script>
import TodoForm from './components/TodoForm.vue'
import TodoList from './components/TodoList.vue'
import {mapGetters, mapActions} from 'vuex'

export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList
  },
  computed: {
    ...mapGetters(['totalTodosCount', 'completedTodosCount', 'uncompletedTodosCount', 'importantTodosCount'])
  },
  methods:{
    ...mapActions(['cleanTodo'])
  }
}
</script>

<style>
body{
  background-color: #AEDAEB;
  display: flex;
  flex-direction: row; 
  align-items: center;
  justify-content: center; 
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#topDiv{
  margin:0px;
  padding: 10px;
  width: 400px;
  background-color: #EDE8E2;
  border: thick double;
  border-color: black;

}

#cleanTodoButton{
  padding: 10px;
  width: 100%;
  opacity: 0.7;
  background-color: red;
  color: white;
  height: 50px;
  border: thick double;
  border-color: black;
  top: 100px;
}
</style>
