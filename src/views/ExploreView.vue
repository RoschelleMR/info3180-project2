<script setup>

    import { ref, onMounted } from "vue";
    import { useRoute, useRouter } from "vue-router";
    import Post from '../components/Post.vue';

    let route = useRoute();
    let router = useRouter();
    let loggedUser = ref('')
    let posts = ref([])
    let token = localStorage.getItem('token')
    let auth = 'Bearer ' + token


    async function fetchLoggedInUser(){
        try {
            const response = await fetch(`/api/v1/currentuser`);
            if(response.ok) {
                const data = await response.json();
                if(data.hasOwnProperty('message')) {
                    loggedUser.value = data["message"];
                }
                if(loggedUser.value === ''){
                    console.log(`User: ${loggedUser.value}`);
                    router.push({path : '/login'});
                }
            } else {
                return Promise.reject('Something was wrong with fetch request!');
            }
        } catch (error) {
            console.log(error);
        }
    }
    
    async function fetchPosts(){
        try {
            const response = await fetch(`/api/v1/posts`);
            if(response.ok) {
                const data = await response.json();
                posts.value = data["posts"];
            } else {
                return Promise.reject('Something was wrong with fetch request!');
            }
        } catch (error) {
            console.log(error);
        }
    }

    function redirectToNewPost(){
        router.push({path : `/newform`});
    }

    onMounted(async () => {
        await fetchLoggedInUser()
        await fetchPosts()
    })

</script>

<template>
<div class="container">
    <button @click="redirectToNewPost" class="btn bg-primary text-light">New Post</button>
    <Post v-for="post in posts" :post="post"/>
</div>

</template>

<style>
    .btn{
        max-width: 200px;
    }
</style>