<template>

    <div class="exploreSidebar">
        <button onclick="addPost()">New Post</button>
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

    import { ref, onMounted } from "vue"; onMounted(() => {     
        getCsrfToken(); 
        getPosts();
    });

    import {useRouter} from "vue-router";
    const router = useRouter()

    let csrf_token = ref("");  
    let posts = ref([]);



    function getCsrfToken() {     
        fetch('/api/v1/csrf-token')       
        .then((response) => response.json())       
        .then((data) => {         
            console.log(data);         
            csrf_token.value = data.csrf_token;       
        })   
    }

    const getPosts = () => {

        fetch("/api/v1/posts", {
            headers: {             
                'X-CSRFToken': csrf_token.value         
                }
        })
        .then(function (response) {         
            return response.json();     
        })     

        .then(function (data){
            posts.value = data.posts
        })

    }

    function addPost() {
        // 
    }



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
        background-color: blue;
        border-radius: 2%;
    }

</style>