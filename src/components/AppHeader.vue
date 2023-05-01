<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark fixed-top">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">Photogram</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <RouterLink to="/" class="nav-link active">Home</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink v-if="isLoggedIn == 'true'" class="nav-link" to="/explore">Explore</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink v-if="isLoggedIn == 'true'" class="nav-link" to="/myprofile">My Profile</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink v-if="isLoggedIn == 'false'" class="nav-link" to="/register">Register</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink v-if="isLoggedIn == 'false'" class="nav-link" to="/login">Login</RouterLink>
              <RouterLink v-else class="nav-link" to="/logout">Logout</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>

import { RouterLink } from "vue-router";

  let isLoggedIn = localStorage.getItem('isLogin');

</script>

<style>
  .navbar{

    background-color: rgba(41, 136, 251, 0.949);
  }

</style>