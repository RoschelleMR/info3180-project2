<template>

    <form @submit.prevent="loginUser" id='loginForm' class="row g-3"> 

        <div v-if = "response_type == 'success'" class="alert alert-success">
            <p>Successfully Logged In</p>
        </div>

        <div v-if = "response_type == 'error'" class="alert alert-danger">
            <ul>
                <li v-for="error in response.errors">
                    {{ error }}
                </li>
            </ul>
        </div>

        <div class="col-12">
            <label for="username" class="form-label">Username</label>
            <input type="text" name="username" class="formcontrol" />
        </div>

        <div class="col-12">
            <label for="password" class="form-label">Password</label>
            <input type="text" name="password" class="formcontrol " />
        </div>


        <div>
            <input type="submit" value="Login">
        </div>


    </form>

</template>

<script setup>

    import { ref, onMounted } from "vue"; onMounted(() => {     
        getCsrfToken(); 
    }); 

    let csrf_token = ref("");  
    let response = ref([]);
    let response_type = ref("");

    function getCsrfToken() {     
        fetch('/api/v1/csrf-token')       
        .then((response) => response.json())       
        .then((data) => {         
            console.log(data);         
            csrf_token.value = data.csrf_token;       
        })   
    }

    const loginUser = () =>{

        let loginForm = document.getElementById('loginForm'); 
        let form_data = new FormData(loginForm);

        fetch("/api/v1/auth/login", {     
            method: 'POST', 
            body: form_data,
            headers: {             
                'X-CSRFToken': csrf_token.value         
                }  
            })     
            .then(function (response) {         
                return response.json();     
            })     
            .then(function (data) {         
        
                console.log(data);

                if(data.hasOwnProperty('errors')){
                    response.value = data;
                    response_type.value = 'error';
                }   
                else{
                    response_type.value = 'success';

                    localStorage.setItem( 'token', JSON.stringify(data.token) );
                }  
            })     
            .catch(function (error) {         
                console.log(error, 'Error');     
            });
    }

</script>