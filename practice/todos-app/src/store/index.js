import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins:[
    createPersistedState()
  ],
  state: {
    todos: [],
    importantTodos: [],
  },
  getters: {
    totalTodosCount(state){
      return state.todos.length
    },
    importantTodosCount(state){
      return state.importantTodos.filter(todo => {
        return todo.isCompleted
      }).length
    },
    completedTodosCount(state){
      return state.todos.filter(todo => {
        return todo.isCompleted
      }).length
    },
    uncompletedTodosCount(state){
      return state.todos.filter(todo => {
        return !todo.isCompleted
      }).length
    },
  },
  mutations: {
    CREATE_TODO(state, newTodo){
      if (newTodo.isImportant) {
        state.importantTodos.push(newTodo)
      }
      state.todos.push(newTodo)
      console.log('importantTodos',state.todos, state.importantTodos)
    },
    DELETE_TODO(state, todoItem){
      const index = state.todos.indexOf(todoItem)
      const importantIndex = state.importantTodos.indexOf(todoItem)
      state.todos.splice(index, 1)
      state.importantTodos.splice(importantIndex, 1)
    },
    DONE_TODO(state, todoItem){
      state.todos = state.todos.filter(todo => {
        if (todo === todoItem) {
          todo.isCompleted = !todo.isCompleted
        }
        return todo
      })

      state.importantTodos = state.importantTodos.filter(todo => {
        if (todo === todoItem) {
          todo.isCompleted = !todo.isCompleted
        }
        return todo
      })
    },
    UPDATE_TODO(state, updatedItem){
      state.todos.forEach((todo)=>{
        if (todo.createdDate === updatedItem.createdDate) {
          const index = state.todos.indexOf(todo)
          state.todos[index] = updatedItem
        }
      })
    },

    IMPORTANT_TODO(state, todoItem){
      state.importantTodos.push(todoItem)
    },
    CLEAN_TODO(state){
      state.todos = []
    }
  },
  actions: {
    createTodo(context, newTodo){
      context.commit('CREATE_TODO', newTodo)
    },
    deleteTodo(context, todoItem){
      context.commit('DELETE_TODO', todoItem)
    },
    doneTodo(context, todoItem){
      context.commit('DONE_TODO', todoItem)
    },
    cleanTodo(context){
      if (confirm('저장되어 있는 할 일들이 모두 삭제됩니다. 정말로 삭제하시겠습니까?')) {
        context.commit('CLEAN_TODO')
      }
    },
    updateTodo(context, updatedItem){
      context.commit('UPDATE_TODO', updatedItem)
    }
  },
  modules: {
  }
})
