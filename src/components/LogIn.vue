<template>
    <div>
      <h1 id="txtTitle">Porfavor identifiquese</h1>
    </div>
    <div id="botonera">
      <div id="izquierda">
        <h1 id="txtTitleAdministrador">Administrador</h1>
        <input type="text" placeholder="Usuario" id="txtAdmin">
        <input type="password" id="pswAdmin" placeholder="Contraseña">
        <input type="submit" value="Entrar" id="btnAdmin">
      </div>
      <div id="derecha">
        <h1 id="txtTitleVendedor">Vendedor</h1>
        <input type="text" id="txtVendedor" placeholder="Usuario">
        <input type="password" id="pswVendedor" placeholder="Contraseña">
        <input type="submit" value="Entrar" id="btnVendedor">
      </div>
    </div>
</template>

<script>
  export default {
  name: 'LogIn'
}  
</script>
<style>
  #txtTitle {
    width: 100%;
    text-align: center;
    margin-top: 20px;
    margin-bottom: 20px;
  }

  #botonera {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 24px;
    gap: 20%;
  }

  #izquierda {
    border: none;
    width: 35%;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  #derecha {
    border: none;
    width: 35%;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  #txtTitleAdministrador {
    text-align: center;
  }

  #txtAdmin {
    border-radius: 7px;
    padding: 8px;
    margin: 30px 0px 70px 0px;
    width: 100%;
    border-color: #D9AB83;
  }

  #pswAdmin {
    border-radius: 7px;
    padding: 8px;
    margin: 10px 0px 40px 0px;
    width: 100%;
    border: #D9AB83 0,5px;
    border-color: #D9AB83;
    }

  #btnAdmin {
    width: 30%;
    align-self: flex-end;
    justify-self: flex-end;
    background-color: #83D98C;
    border-radius: 4px;
    border: rgb(6, 100, 6)  solid 1px;
    padding: 3px;
  }

</style>
