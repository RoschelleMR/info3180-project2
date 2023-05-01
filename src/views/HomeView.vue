<script setup>
import { ref } from "vue";
import {useRouter} from "vue-router";
const router = useRouter()



</script>

<template>
    <div class="homecontainer">

      <div class="card">
        <img src="@/assets/home-img.jpg" alt=""/>
      </div>

      <div class="card info">
        <div class="title">
          <h3 >Photogram</h3>
        </div>
        <hr>
        <div class="card-body">
          <p>Share photos of your favourite moments with friends, family and the world</p>
          <div class="button-box">
            <button @click="$router.push('/register')" class="btn register">Register</button>
            <button @click="$router.push('/login')" class="btn btn-primary login">Login</button>
          </div>
        </div>
      </div>

    </div>
</template>

<style>
  .homecontainer{
    display: flex;
    column-gap: 8px;
    align-content: center;
    justify-content: center;
  }

  .title{
    text-align: center;
  }

  h3{
    font-weight: bold;
  }

  .info{
    padding: 25px;
  }

  .button-box{
    display: flex;
    justify-content: center;
    column-gap: 5px;
  }

  .register{
    background-color: rgb(7, 202, 43);
        color: white;
        font-weight: bold;

        border: none;
        border-radius: 10px;

        width: 100%;
        margin-top: 10px;
        padding: 6px;
  }

  .register:hover{
    background-color: rgb(4, 220, 44);
    color: white;
    transition: all 0.8s;
  }

  .login{

    font-weight: bold;

    width: 100%;
    margin-top: 10px;
    padding: 6px;

  }
</style>