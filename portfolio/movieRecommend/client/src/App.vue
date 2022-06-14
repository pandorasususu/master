<template>
  <div id="app" class="flex flex-row">
    <nav-bar-comp></nav-bar-comp>
    <router-view/>
  </div>
</template>

<script>
import NavBarComp from '@/components/basic/NavBarComp.vue'
import {mapActions} from 'vuex'
export default {
  name:'app',
  components: { NavBarComp },
  methods: {
    ...mapActions(['getCurrentUser'])
  },
  created(){
    this.getCurrentUser()
  }
}
</script>

<style scoped>

</style>