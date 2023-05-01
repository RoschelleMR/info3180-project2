<script setup>
import { ref, onMounted, defineProps } from 'vue';
import { useRouter } from "vue-router";

const props = defineProps(['post'])
let csrf_token = ref("")
let router = useRouter();
let loggedUser = ref('')
let user = ref({
    'username': '',
    'profile_photo': ''
})
let fetchResponse = ref("")
let postLiked = ref(false)

function getCsrfToken() {
    fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
    csrf_token.value = data.csrf_token;
    })
}

async function fetchUserDetails(userid) {
    try {
        const response = await fetch(`/api/v1/users/${userid}`);
        if (response.ok) {
            const data = await response.json();
            user.value = data
        } else {
            return Promise.reject('Something was wrong with fetch request!');
        }
    } catch (error) {
        console.log(error);
    }
}

async function fetchLoggedInUser(){
    try {
        const response = await fetch(`/api/v1/currentuser`);
        if(response.ok) {
            const data = await response.json();
            if(data.hasOwnProperty('message')) {
                loggedUser.value = data["message"];

                props.post.likes.forEach(like => {
                    if(like.user_id == loggedUser.value){
                        postLiked.value = true
                    }
                });
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

function likePost(){
    fetch(`/api/v1/posts/${props.post.id}/like`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token.value
        }
    })
    .then(response => {
        if(response.ok){return response.json()}
        else{return Promise.reject('Something was wrong with fetch request!')}
    })
    .then(data => {
        console.log(data);
        props.post.likes.push(loggedUser.value)
        postLiked.value = true
    })
    .catch(error => {
        console.log(error);
    })
}

function redirectToProfile(){
    router.push({path : `/user/${props.post.user_id}`});
}

onMounted(async () => {
    await getCsrfToken()
    await fetchUserDetails(props.post.user_id)
    await fetchLoggedInUser()
})

</script>

<template>
<div class="post">
    <header class="post-header">
        <img @click="redirectToProfile" :src="user.profile_photo" :alt="`Profile Photo of ${user.username}`" id="pfp">

        <h3>{{ user.username }}</h3>
    </header>
    <img :src="post.photo" class="postImg" alt="">
    <section class="caption">{{ post.caption }}</section>
    <section class="footer">
        <div>
            <button v-if="!postLiked" @click="likePost" class="btn bg-primary text-light">Like</button>
            <button v-if="postLiked" class="btn bg-success text-light">Liked</button>
            {{ post.likes.length }} Likes
        </div>
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
    width: 50px;
    border-radius: 50%;
    object-fit:cover;
    cursor: pointer;
}
.post-header{
    display: flex;
    align-items: center;
    padding: 10px 15px;
}
h3{
    font-size: 20px;
    margin: 0;
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
    align-items: center;
    padding: 5px 15px 20px 15px;
    font-weight: bold;
}
.footer .btn{
    margin-right: 10px;
}
</style>