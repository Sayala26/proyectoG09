<template>
  <div class = "app">
    <HeaderApp />
    <LogIn />
  </div>
</template>

<script>
import HeaderApp from './components/Header.vue'
import LogIn from './components/LogIn.vue'

export default {
  name: 'App',
  components: {
    HeaderApp, 
    LogIn
  }
}
</script>

<style>
* {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
}
</style>
