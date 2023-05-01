<script setup>
import { ref, onMounted, defineProps } from 'vue';
import { useRouter } from "vue-router";

const props = defineProps(['post'])
let router = useRouter();
let user = ref({
    'username': '',
    'profile_photo': ''
})

async function fetchUserDetails(userid) {
    try {
        const response = await fetch(`/api/v1/users/${userid}`);
        if (response.ok) {
            const data = await response.json();
            user.value = data
            console.log(data)
        } else {
            return Promise.reject('Something was wrong with fetch request!');
        }
    } catch (error) {
        console.log(error);
    }
}

function redirectToProfile(){
    router.push({path : `/user/${props.post.user_id}`});
}

onMounted(async () => {
    await fetchUserDetails(props.post.user_id)
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
        <div><button class="btn bg-primary text-light">Like</button>{{ post.likes.length }} Likes</div>
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
    padding: 5px 15px 20px 15px;
    font-weight: bold;
}
.footer .btn{
    margin-right: 10px;
}
</style>