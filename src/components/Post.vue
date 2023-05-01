<script setup>
import { ref, onMounted, defineProps } from 'vue';

const props = defineProps(['post'])


</script>

<template>
<div class="post">
    <header>
        <img src="#" alt="Profile Photo of " id="pfp">
        <h3>Username</h3>
    </header>
    <img :src="post.photo" class="postImg" alt="">
    <section class="caption">{{ post.caption }}</section>
    <section class="footer">
        <div>{{ post.likes.length }}</div>
        <div>{{ post.created_on }}</div>
    </section>
</div>
</template>

<style>
.post{
    background-color: white;
    width: 500px;
    min-height: 450px;
    margin: 15px;
}
#pfp{
    aspect-ratio: 1 / 1;
    width: 75px;
    border-radius: 50%;
    object-fit:cover;
}
header{
    display: flex;
    padding: 5px 15px;
}
h3{
    font-size: 20px;
    margin-left: 10px;
}
.postImg{
    aspect-ratio: 1/1;
    width: 100%;
    object-fit: cover;

    transition: 0.3s;
}
.caption{
    margin-bottom: 20px;
    padding: 10px 15px;
}
.footer{
    display: flex;
    justify-content: space-between;
    padding: 5px 15px;
}
</style>