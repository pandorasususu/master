<template>
  <div id="app">
    <nav-bar>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav-bar>
    <router-view/>
  </div>
</template>

<script>
import NavBar from '@/components/basic/NavBar.vue'

export default {
  name:'app',
  component: {
    NavBar
  }
  
}

<style>

</style>
