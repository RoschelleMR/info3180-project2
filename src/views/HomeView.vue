<script setup>
import { ref } from "vue";

let message = ref("Photogram")
let subtext = ref("Share photos of your favourite moments with friends, family and the world.")

</script>

<template>
    <div class="container">
      <div class="photodiv">
      <img alt="Quote" class="quote" src="@/assets/Quote.jpg" width="170" height="200" />
      </div>
      <div class="text-container">
        <!-- <img alt="Quote" class="quote" src="@/assets/Quote.jpg" width="170" height="200" /> -->
        <h1>{{ message }}</h1>
        <p>{{ subtext }}</p>
        <button class="register">Register</button>
        <button class="login">Login</button>
      </div>
    </div>
</template>

<style>
/* Add any component specific styles here */
  h1 {
    justify-items: center;
  }

  button {
    color: white;
    border: none;
    border-radius: 5%;
    padding: 1%;
    padding-left: 2%;
    padding-right: 2%;
    margin: 0.5em;
  }

  button.register {
    background-color: rgb(65, 255, 7);
  }

  button.login {
    background-color: rgb(33, 182, 241);
  }

  .container {
    display: flex;
    justify-content: center;
    column-gap: 20px;
    margin: 5em;
  }

  .text-container {
    align-self: center;
  }

</style>