<script setup>

    import { ref, onMounted } from "vue";
    import { useRoute } from "vue-router";
    import UserProfileHeader from '../components/UserProfileHeader.vue';
    import UserPhotos from '../components/UserPhotos.vue';

    let route = useRoute();
    let id = ref('')
    let userDetails = ref({})
    let posts = ref([])
    let followers = ref()

    function fetchLoggedInUser(){
        fetch(`/api/v1/currentuser`)
        .then(response => {
            if(response.ok){return response.json()}
            else{return Promise.reject('Something was wrong with fetch request!')}
        })
        .then(data => {
            console.log(data)
            if(data.hasOwnProperty('message')) {
                id.value = data["message"]
            }
        })
        .catch(error => {
            console.log(error);
        })
    }

    function fetchPosts(){
        fetch(`/api/v1/users/${id.value}/posts`)
        .then(response => {
            if(response.ok){return response.json()}
            else{return Promise.reject('Something was wrong with fetch request!')}
        })
        .then(data => {
            posts.value = data["posts"]
        })
        .catch(error => {
            console.log(error);
        })
    }
    
    // function fetchUserDetails(){
    //     fetch(`api/v1/users/${id}`)
    //     .then(response => {
    //         if(response.ok){return response.json()}
    //         else{return Promise.reject('Something was wrong with fetch request!')}
    //     })
    //     .then(data => {
    //         userDetails.value = data
    //     })
    //     .catch(error => {
    //         console.log(error);
    //     })
    // }

    // function fetchFollowers(){
    //     fetch(`/api/v1/users/${id}/follow`)
    //     .then(response => {
    //         if(response.ok){return response.json()}
    //         else{return Promise.reject('Something was wrong with fetch request!')}
    //     })
    //     .then(data => {
    //         followers.value = data["followers"]
    //     })
    //     .catch(error => {
    //         console.log(error);
    //     })
    // }

    function hasUserDetails() {
        return userDetails.hasOwnProperty("username"); //Checks if data is set in userDetails
    }

    onMounted(() => {
        fetchLoggedInUser()
        if(id.value == ''){
            router.push({path : '/explore'})
        }
        // fetchUserDetails()
        // fetchFollowers()
        fetchPosts()
    })

    //DISPLAY MESSAGE IF THE USER DOESN'T EXIST
</script>

<template>
    <!-- <UserProfileHeader v-if="hasUserDetails" :userDetails="userDetails" :followers="followers"/> -->
    <UserPhotos v-if="posts" :posts="posts"/>
</template>

<style>

</style>