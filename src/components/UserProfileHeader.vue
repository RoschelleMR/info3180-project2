<script setup>
import { defineProps } from 'vue';
const props = defineProps(['userDetails', 'followers', 'posts', 'canFollow'])

</script>

<template>
<div class="container profile p-3">
    <div class="row">
        <div class="pfp col-lg-2 col-md-3 col-sm-12 text-center">
            <img :src="userDetails.profile_photo" :alt="`Picture of ${userDetails.firstname} ${userDetails.lastname}`">
        </div>
        <div class="userInfo col-lg-6 col-md-9 col-sm-12">
            <h1>{{ userDetails.firstname }} {{ userDetails.lastname }}</h1>
            <p>{{ userDetails.location }}</p>
            <p>Member since, {{ userDetails.joined_on }}</p>
            <br>
            <p class="bio">{{ userDetails.biography }}</p>
        </div>
        <div class="col-lg-4 col-md-12 col-sm-12 text-center d-flex align-items-center ">
            <div class="stats container">
                <div class="row">
                    <div class="col-6">
                        <h3 class="stat">{{ posts.length }}</h3>
                        <h4 class="stat-name">Posts</h4> 
                    </div>
                    <div class="col-6">
                        <h3 class="stat">{{ followers.length }}</h3>
                        <h4 class="stat-name">Followers</h4>
                    </div>
                </div>
                <div class="controls mx-auto col-lg-10 col-md-5 col-5">
                    <button v-if="canFollow" class="follow-btn btn bg-primary text-light">Follow</button> <!--DO NOT DISPLAY IF YOU ARE THIS USER-->
                </div>
            </div>
            
        </div>
    </div>
</div>
</template>
  
<style>
/* Add any component specific styles here */
.profile{
    background-color: white;
    box-shadow: 0 2px 5px rgb(0, 0, 0, 0.4);
    margin-bottom: 30px;
}

.pfp img{
    aspect-ratio: 1 / 1;
    width: 100%;
    object-fit:cover;
}

p{
    margin: 0;
}
.bio{
    margin-bottom: 15px;
}

.stat{
    margin-bottom: 5px;
}
.stat-name{
    color: rgb(139, 139, 139);
    font-size: 17px;
    font-weight: bold;
}
.follow-btn{
    width: 100%;
}

@media screen and (max-width: 768px){
    .profile{
        background: none;
        box-shadow: none;
    }
    .userInfo{
        text-align: center;
    }
    .pfp img{
        width: 150px;
    }
}


</style>