<template>
    <div class="container">
        <div class="form-box">
        <h3 class="header-text">New Post</h3>

        <form @submit.prevent = "createPost" id = "NewPostForm">
            <div class = "photoCaption">
                <div class = "form-group mb-3">
                    <label for="photo" class="form-label">Photo</label>
                    <input type = "file" id = "img" name = "photo" class = "formcontrol" accept = ".jpg, .png"/>
                </div>
                <div class = "form-group mb-3">
                    <label for="caption" class="form-label">Caption</label>
                    <textarea name="caption" class="formcontrol" ></textarea>
                </div>
                <button>Submit</button>
            </div>
        </form>
    </div>
    </div>
    
    
</template>

<script setup>

    import { ref, onMounted } from "vue";
    let csrf_token = ref("")
    let fetchResponseType = ref("")
    let fetchResponse = ref("")
    let loggedUser = ref('')
    
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
                if(data.hasOwnProperty('message')) {
                    loggedUser.value = data["message"];
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


    onMounted(() => {
        getCsrfToken()
        fetchLoggedInUser()
    })

    function createPost(){
        let PostForm = document.querySelector("#NewPostForm")
        let formData = new FormData(PostForm)
        fetch(`/api/v1/users/${loggedUser.value}/posts`, {
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
            fetchResponse.value = data
            if(data.hasOwnProperty('errors')) {
                fetchResponseType.value = "danger"
            } else {
                fetchResponseType.value = "success"
            }
        })
        .catch(function (error) {
            console.log(error);
        });
    }
</script>
            
<style>
*{
    -moz-box-sizing: border-box; 
    -webkit-box-sizing: border-box; 
    box-sizing: border-box; 
}
.container{
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 50px;
    }
.form-box{
    max-width: 500px;
    width: 100%;
}
form{
    display: flex;
    flex-direction: column;
    justify-content: center;
    background-color: white;
    padding: 50px;
    box-shadow: 2px 2px 8px rgb(88, 88, 88);
}
.form-group{
    display: flex;
    margin-bottom: 15px;
    flex-direction: column;
}
.form-label{
    font-weight: bold;
}
button{
    background-color: rgb(7, 202, 43);
    color: white;
    font-weight: bold;
    border: none;
    border-radius: 5px;
    width: 100%;
    margin-top: 10px;
    padding: 6px;
}
button:hover{
    background-color: rgb(4, 220, 44);
    color: white;
    transition: all 0.8s;
}

</style>