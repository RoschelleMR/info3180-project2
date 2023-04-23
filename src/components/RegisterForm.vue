<template>
    <form @submit.prevent = "submitForm" id = "NewPostForm">
        <h1>Register</h1>
        <div class = "formInfo">
            <div class="form-group mb-3">
                label for="username" class="form-label">Username</label>
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

</template>

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

.formInfo{
    background-color: white;
    border-color: gray;
    box-shadow: 0px 0px 2px 2px gray;
}
 button{
    
 }


    

