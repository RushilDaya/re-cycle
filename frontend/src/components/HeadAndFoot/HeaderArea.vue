<template>
<div id="outer-nav">
    <div id="nav-bar">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#">Re-cycle</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <a class="nav-link" @click="goMainScreen()"> Main Screen</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" @click="goSocialScreen()">Social</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" @click="goDiscountScreen()" >Buy</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" @click="goProfileScreen()">Profile</a>
                </li>
                </ul>
            </div>
            </nav>
    </div>
</div>
</template>

<script>
export default {
    name:'HeaderArea',
    data(){
        return{

        }
    },
    methods:{
        goMainScreen(){
            this.$router.push('/')
        },
        goSocialScreen(){
            this.$router.push('/social')
        },
        goDiscountScreen(){
            this.$router.push('/discount')
        },
        goProfileScreen(){
            this.$router.push('/profile')
        }   
    }

}
</script>

<style scoped>
</style>
