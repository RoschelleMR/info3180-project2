<template>
    <form @submit.prevent = "submitLogin" id = "loginForm">
        <h1>Login</h1>
        <div class = "loginInfo">
            <div class = "username">
                <label for="username" class="form-label">Username</label>
                <input type = "text"  id = "username" name="username" class="formcontrol"></input>
            </div>
            <div class = "password">
                <label for="password" class="form-label">Password</label>
                <input type = "password"  id = "pw" name="pw" class="formcontrol"></input>
            </div>
            <button>Login</button>
        </div>
    </form>
</template>
