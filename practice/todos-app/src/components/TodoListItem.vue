<template>
    <div class="TodoListItem" :class="{'is-completed': todo.isCompleted, 'is-important': todo.isImportant, 
    'important-completed': todo.isCompleted && todo.isImportant}">
      <div id="itemInner" @click="doneTodo(todo)">
        <span >{{todo.title}}&nbsp;&nbsp; </span>       
        <button id="deleteButton" @click="deleteTodo(todo)">X </button>
      </div>
      <span @click="oepnUpdateForm">&nbsp;&nbsp;[수정]</span>
      <Teleport to="body">
        <!-- use the modal component, pass in the prop -->
        <update-form-modal :show="doUpdate" @close="doUpdate = false" :todo="todo">
          <template #header>
            <h3>할 일 수정하기</h3>
          </template>
        </update-form-modal>
    </Teleport>
    </div>
</template>

<script>
import {mapActions} from 'vuex'
import UpdateFormModal from './UpdateFormModal.vue'

export default {
  name: 'TodoListItem',
  components:{
    UpdateFormModal
  },
  data(){
    return {
      doUpdate: false,
    }
  },
  props:{
    todo: Object,
  },
  methods: {
    ...mapActions(['deleteTodo', 'doneTodo']),
    oepnUpdateForm(){
      this.doUpdate = !this.doUpdate
    }
  },
}
</script>

<style scoped>
.TodoListItem{
  box-sizing: border-box;
  display: flex;
  flex-direction: row; 
  align-items: center;
  justify-content: center; 
  height: 50px;
  width:100%;
  margin-top: 10px;
  border: thick double;
  border-color: black;
  background-color: #EDE8E2;
}

#itemInner{
  display: flex;
  flex-direction: row; 
  align-items: center;


}

#deleteButton{
  height: 50%;
  background-color: black;
  color: white;
}

.is-completed{
  text-decoration: line-through;
}

.is-important{
  /* opacity: 0.7; */
  background-color: #352CF5;
  color: white;
}

.important-completed{
  opacity: 1;
  background-color: #EDE8E2;
  color:black;
}

ul{
  width:100%;
  padding:0px;

}

li{
  list-style: none;
}
</style>