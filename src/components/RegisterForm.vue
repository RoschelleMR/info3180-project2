<template>
    <div class="container">
        <div class="form-box">
            <h3 class="header-text">Register</h3>
            <form @submit.prevent = "submitForm" id = "NewPostForm">
                <div class = "formInfo">
                    <div class="form-group mb-3">
                        <label for="username" class="form-label">Username</label>
                        <input type="text" name="username" class="formcontrol" />
                    </div>

                    <div class="form-group mb-3">
                        <label for="password" class="form-label">Password</label>
                        <input type="text" name="password" class="formcontrol" />
                    </div>

                    <div class="form-group mb-3">
                        <label for="firstName" class="form-label">Firstname</label>
                        <input type="text" name="firstName" class="formcontrol" />
                    </div>

                    <div class="form-group mb-3">
                        <label for="lastName" class="form-label">Lastname</label>
                        <input type="text" name="lastName" class="formcontrol" />
                    </div>

                    <div class="form-group mb-3">
                        <label for="email" class="form-label">Email</label>
                        <input type="text" name="email" class="formcontrol" />
                    </div>

                    <div class="form-group mb-3">
                        <label for="location" class="form-label">Location</label>
                        <input type="text" name="location" class="formcontrol" />
                    </div>

                    <div class="form-group mb-3">
                        <label for="biography" class="form-label">Biography</label>
                        <textarea name="biography" class="formcontrol" ></textarea>
                    </div>

                    <div class="form-group mb-3">
                        <label for="photo" class="form-label">Photo</label>
                        <input type="file" id="photo" name="photo" class="formcontrol" accept=".jpg,.png" />
                    </div>

                    <button type ="register">Register</button>
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
    function register(){
        let RegisterForm = document.querySelector("#RegisterForm")
        let formData = new FormData(movieForm)
        fetch("/api/v1/....", {
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
.header-text{
    font-weight: bold;
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


    

