<template>
    <div class="exploreSidebar">
        <button>New Post</button>
    </div>

    <div class="exploreMainBar">
        <!-- Other Users' Posts -->
        <div v-for="post in posts" :key="post.id">
            <img :src="post.image_url" alt="Photagram Post">
            <p>{{ post.caption }}</p>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import { ref } from "vue";

    export default {
    data() {
        return {
        posts: [],
        };
    },
    mounted() {
        axios.get('/api/v1/users/<user_id>/posts')
        .then(response => {
            this.posts = response.data;
        })
        .catch(error => {
            console.log(error);
        });
    },
    };
</script>

<style>
    .posts {
        display: flex;
        flex-wrap: wrap;
    }

    .posts div {
        margin: 10px;
        text-align: center;
    }

    button {
        color: blue;
        border-radius: 20%;
    }
</style>