<template>

    <div v-if = "logoutStatus == 'success'" class="alert alert-success">
      <p>Successfully Logged Out</p>
    </div>

    <div class="card">
        <h3>
            Are you sure you want to logout out?
        </h3>
        <button @click="logout" class="button">Logout</button>
    </div>
    
</template>

<script setup>


  import { ref, onMounted } from "vue"; onMounted(() => {  
        getCsrfToken();   
    }); 

    let logoutStatus = ref("");  
    let csrf_token = ref("");

     
    let token = localStorage.getItem('token')
    
    let test_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEsImlhdCI6MTY4MjQyMjI1OSwiZXhwIjoxNjgyNDIzMTU5fQ.6K7KNYlr9T4GkNpY2SYJg1j4F9YOVNtXSWrsxiyPdo4"
    console.log(test_token)

    function getCsrfToken() {     
        fetch('/api/v1/csrf-token')       
        .then((response) => response.json())       
        .then((data) => {         
            console.log(data);         
            csrf_token.value = data.csrf_token;       
        })   
    } 

    function logout() {     
        
        localStorage.setItem('isLogin', false );

        fetch("/api/v1/auth/logout", {     
            method: 'POST',
            headers: {             
                'X-CSRFToken': csrf_token.value,
                'Authorization': "Bearer " + token     
                }  
            })    
        .then((response) => 
            response.json())  

        .then((data) => {         
            console.log(data); 
            if (data.hasOwnProperty('success')){
              logoutStatus.value = "success";  
            }        
                
        })   
    }

     
</script>

<style>

</style>