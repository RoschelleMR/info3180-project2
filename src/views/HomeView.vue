<script setup>
import { ref } from "vue";

let message = ref("Photogram")
let subtext = ref("Share photos of your favourite moments with friends, family and the world.")

</script>

<template>
    <div class="container">
      <div class="text-center">
        <img alt="Vue logo" class="logo" src="@/assets/Quote.jpg" width="125" height="125" />
        <h1>{{ message }}</h1>
        <p>{{ subtext }}</p>
        <button>Register</button>
        <br>
        <button>Login</button>
      </div>
    </div>
</template>

<style>
/* Add any component specific styles here */
</style>