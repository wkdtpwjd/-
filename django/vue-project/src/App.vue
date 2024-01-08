<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div>  
    <header>


      <div class="wrapper">

        <nav>
          <RouterLink to="/">Home</RouterLink>
          <RouterLink to="/login">Login</RouterLink>
          <RouterLink to="/signup">SignUp</RouterLink>
        </nav>
      </div>
    </header>
    
    <RouterView />
    
    
  </div>
  
</template>

<style scoped>

</style>
