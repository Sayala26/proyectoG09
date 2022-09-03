<template>
  <div id="header">
    <h1 class="hola">Bienvenido al sistema de inventario de</h1>
    <h2 class="hola">"A la brasa"</h2>
  </div>
</template>

<script>
export default {
  name: 'HeaderApp'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
  * {
    margin: 0px;
    padding: 0px;
    box-sizing: border-box;
  }
  .hola {
    color: rgb(255, 255, 255);
  }
  #header {
    background-color: #533908;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 20px;
  }
</style>
