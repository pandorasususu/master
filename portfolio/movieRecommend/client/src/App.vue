<template>
  <div id="app" class="flex flex-row">
    <nav-bar-comp></nav-bar-comp>
    <router-view/>
  </div>
</template>

<script>
  import NavBarComp from '@/components/basic/NavBarComp.vue'

  export default {
    name:'app',
    components: { NavBarComp },
    
  }
</script>

<style scoped>

</style>