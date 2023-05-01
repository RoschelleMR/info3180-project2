<script setup>

    import { ref, onMounted } from "vue";
    import { useRoute, useRouter } from "vue-router";
    import UserProfileHeader from '../components/UserProfileHeader.vue';
    import UserPhotos from '../components/UserPhotos.vue';

    let route = useRoute();
    let router = useRouter();
    let id = ref('')
    let userDetails = ref({})
    let posts = ref([])
    let followers = ref([])

    let token = localStorage.getItem('token')
    let auth = 'Bearer ' + token

    async function fetchLoggedInUser(){
        try {
            const response = await fetch(`/api/v1/currentuser`);
            if(response.ok) {
                const data = await response.json();
                console.log(data);
                if(data.hasOwnProperty('message')) {
                    console.log(`User: ${data["message"]}`);
                    id.value = data["message"];
                }
                if(id.value === ''){
                    console.log(`User: ${id.value}`);
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
        console.log(`Fetching Posts for User ${id.value}`);
        try {
            const response = await fetch(`/api/v1/users/${id.value}/posts`);
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

    async function fetchUserDetails() {
        try {
            const response = await fetch(`/api/v1/users/${id.value}`);
            if (response.ok) {
                const data = await response.json();
                userDetails.value = data;
            } else {
                return Promise.reject('Something was wrong with fetch request!');
            }
        } catch (error) {
            console.log(error);
        }
    }

    async function fetchFollowers() {
        try {
            const response = await fetch(`/api/v1/users/${id.value}/follow`, 
            {   method: 'GET', 
                headers:{
                    'Authorization': auth,
                }
            });
            if (response.ok) {
                const data = await response.json();
                followers.value = data["followers"];
                console.log('Followers:')
                console.log(data)
            } else {
                return Promise.reject('Something was wrong with fetch request!');
            }
        } catch (error) {
            console.log(error);
        }
    }



    function hasUserDetails() {
        return userDetails.hasOwnProperty("username"); //Checks if data is set in userDetails
    }

    onMounted(async () => {
        await fetchLoggedInUser()
        await fetchUserDetails()
        await fetchFollowers()
        await fetchPosts()
    })

    //DISPLAY MESSAGE IF THE USER DOESN'T EXIST
</script>

<template>
    <UserProfileHeader v-if="hasUserDetails" :userDetails="userDetails" :followers="followers" :posts="posts" :canFollow="false"/>
    <UserPhotos v-if="posts" :posts="posts"/>
</template>

<style>

</style>