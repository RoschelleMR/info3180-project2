<script setup>
import { defineProps } from 'vue';
const props = defineProps(['posts'])

</script>

<template>
<div class="feed container text-center">
    <div class="imgBox" v-for="post in posts" :key="post.id">
        <img :src="post.photo" :alt="post.caption">
    </div>
</div>
</template>

<style>
.feed{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
}

.feed img{
    aspect-ratio: 1/1;
    width: 90%;
    object-fit: cover;

    transition: 0.3s;
}
.feed img:hover{
    opacity: 0.85;
}

@media screen and (max-width: 351px){
    .feed{
        grid-template-columns: repeat(1, 1fr);
    }
}

@media screen and (max-width: 768px){
    .feed img{
        width: 100%;
    }
}
</style>