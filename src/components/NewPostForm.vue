<template>
    <form @submit.prevent = "submitForm" id = "NewPostForm">
        <h1>New Post</h1>
        <div class = "photoCaption">
            <div class = "photo">
                <label for="photo" class="form-label">Photo</label>
                <input type = "file" id = "img" name = "img" class = "formcontrol" accept = ".jpg, .png"/>
            </div>
            <div class = "caption">
                <label for="caption" class="form-label">Caption</label>
                <textarea name="caption" class="formcontrol" ></textarea>
            </div>
            <button>Submit</button>
        </div>
    </form>
</template>

<script setup>

    import { ref, onMounted } from "vue";
    let csrf_token = ref("")
    let fetchResponseType = ref("")
    let fetchResponse = ref("")
    
    function getCsrfToken() {
        fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
        console.log(data);
        csrf_token.value = data.csrf_token;
        })
    }
    onMounted(() => {
        getCsrfToken()
    })
    function createPost(){
        let PostForm = document.querySelector("#PostForm")
        let formData = new FormData(PostForm)
        fetch("/api/v1/users/<user_id>/posts", {
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
        })
        .catch(function (error) {
            console.log(error);

             if(data.hasOwnProperty('errors')) {
                fetchResponseType.value = "danger"
            } else {
                fetchResponseType.value = "success"
            }
        });
    }
</script>
            
<style>
*{
    -moz-box-sizing: border-box; 
    -webkit-box-sizing: border-box; 
    box-sizing: border-box; 
}

form{
    display: flex;
    justify-content: center;
    align-items: center;
}

label{
    display: block;
    font-size: 22px;
    margin-bottom: 13px;
}

.photoCaption{
    background-color: white;
    border-color: gray;
    box-shadow: 0px 0px 2px 2px gray;
}

button{
    
}
</style>