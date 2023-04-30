<template>

    <div class="container">
        <div className="logout-box">
            <div className="logout-header">
                <h3>Logout</h3>
                <div v-if = "logoutStatus == 'success'" class="alert alert-success">
                    <p>Successfully Logged Out</p>
                </div>
            </div>

            <div class="message-box">
                <p>Are you sure you want to logout out?</p>
                <button @click="logout" class="btn btn-primary">Logout</button>
            </div>
        </div>
        
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

    .container{
        display: flex;
        flex-direction: column;
        /* flex-wrap: wrap; */
        
        padding: 50px;
        
        align-items: center;
        
    }

    .logout-box{
        max-width: 500px;
        width: 100%;
    }

    .message-box{
        display: flex;
        flex-direction: column;

        justify-content: center;
        text-align: center;

        

        background-color: white;
        padding: 50px;

        box-shadow: 2px 2px 8px rgb(88, 88, 88);
    }

    .logout-header{
        margin-bottom: 15px;
    }

    h3, .message-box p{
        font-weight: bold;
    }

</style>