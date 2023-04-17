<template>
    <form @submit.prevent = "submitForm" id = "NewPostForm">
        <h1>New Post</h1>
        <div class = "photoCaption"
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
            
