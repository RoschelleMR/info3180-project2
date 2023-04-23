<template>
    <form @submit.prevent = "submitForm" id = "NewPostForm">
        <h1>New Post</h1>
        <div class = "photoCaption">
            <div class = "photo">
                <label for="photo" class="form-label">Photo</label>
                <input type = "file" id = "img" name = "img" class = "formcontrol" accept = ".jpg, .png"/>
            </div>
            <div class = "caption"
                <label for="caption" class="form-label">Caption</label>
                <textarea name="caption" class="formcontrol" ></textarea>
            </div>
            <button>Submit</button>
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

.photoCaption{
    background-color: white;
    border-color: gray;
    box-shadow: 0px 0px 2px 2px gray;
}

button{
    
}