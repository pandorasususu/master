<template>
    <Transition name="modal">
    <div v-if="show" class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal-header">
            <slot name="header">할 일 수정하기</slot>
          </div>

          <div class="modal-body">
            <slot name="body">
              할 일: 
              <input v-model="updateTitle" type="text" :placeholder="todo.title">
              <br>
              완료:
              <input type="checkbox" v-model="updateIsCompleted">
              <br>
              중요:
              <input type="checkbox" v-model="updateIsImportant">
            </slot>
          </div>

          <div class="modal-footer">
            <slot name="footer">
              &nbsp;
              <button
                class="modal-default-button"
                @click="updateTodo">
                수정하기
              </button>
            </slot>
          </div>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script>

export default {
  name: 'UpdateFormModal',
  props:{
    todo:Object,
    show:Boolean,
  },
  data(){
    return{
      updateTitle: this.todo.title,
      updateIsCompleted: this.todo.isCompleted,
      updateIsImportant: this.todo.isImportant,
      updatedDate: new Date().getTime(),
    }
  },
  methods:{
    updateTodo(){
      const updatedItem = {
        title: this.updateTitle,
        isCompleted: this.updateIsCompleted,
        isImportant: this.updateIsImportant,
        createdDate: this.todo.createdDate,
        updatedDate: this.updatedDate,
      }
      this.$store.dispatch('updateTodo', updatedItem)
      this.$emit('close')
    }
  }
}
</script>

<style>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
  opacity: 1;
  color: black;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 300px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}
</style>