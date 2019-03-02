<template>
    <div>
        <div id="img-holder">
            <img src="../assets/man-profile-svgrepo-com.svg" /> 
        </div>
    </div>
</template>

<script>
export default {
    name:'ProfilePage',
    data(){
        return{
            name:'',
            company:'',
            age:'',
            gender:''
        }
    }

}
</script>

<style scoped>
    #img-holder{
        margin:30px;
        max-width:400px;
        text-align:center;
    }
</style>
