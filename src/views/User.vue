<script setup>

    import { ref, onMounted } from "vue";
    import { useRoute, useRouter } from "vue-router";
    import UserProfileHeader from '../components/UserProfileHeader.vue';
    import UserPhotos from '../components/UserPhotos.vue';

    let route = useRoute();
    let router = useRouter();
    let loggedUser = ref('')
    let id = ref('')
    let userDetails = ref({})
    let posts = ref([])
    let followers = ref([])
    let isFollowed = ref()

    id.value = route.params.id

    let csrf_token = ref("")
    let token = localStorage.getItem('token')
    let auth = 'Bearer ' + token

    function getCsrfToken() {
        fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
        console.log(data);
        csrf_token.value = data.csrf_token;
        })
    }

    async function fetchLoggedInUser(){
        try {
            const response = await fetch(`/api/v1/currentuser`);
            if(response.ok) {
                const data = await response.json();
                console.log(data);
                if(data.hasOwnProperty('message')) {
                    console.log(`User: ${data["message"]}`);
                    loggedUser.value = data["message"];

                    //If the user is trying to view their own page, then redirect to /myprofile route
                    if(loggedUser.value == id.value){
                        router.push({path : '/myprofile'});
                    }
                }
                if(loggedUser.value === ''){
                    //If user is not logged in then redirect to login page
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

                if(followers.value.includes(loggedUser.value)){
                    isFollowed.value = true
                }
                else{
                    isFollowed.value = false
                }

                console.log('Followers:')
                console.log(data)

            } else {
                return Promise.reject('Something was wrong with fetch request!');
            }
        } catch (error) {
            console.log(error);
        }
    }

    function follow() {
        let formData = new FormData()
        formData.append('target_id', id)
        formData.append('user_id', loggedUser.id)

        fetch(`/api/v1/users/${userDetails.value.id}/follow`, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': csrf_token.value
            }
        })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            console.log(data);
            isFollowed.value = true
            followers.value.push(loggedUser)
        })
        .catch(function (error) {
            console.log(error);
        });
    }

    function hasUserDetails() {
        return userDetails.hasOwnProperty("username"); //Checks if data is set in userDetails
    }

    onMounted(async () => {
        await getCsrfToken()
        await fetchLoggedInUser()
        await fetchUserDetails()
        await fetchFollowers()
        await fetchPosts()
    })

</script>

<template>
    <UserProfileHeader 
        v-if="hasUserDetails" 
        :userDetails="userDetails" 
        :followers="followers" 
        :follow="follow" 
        :posts="posts" 
        :canFollow="true" 
        :isFollowed="isFollowed"
    />
    <UserPhotos v-if="posts" :posts="posts"/>
</template>

<style>

</style>