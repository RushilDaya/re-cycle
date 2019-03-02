<template>
<div id="outer-nav">
    <div id="nav-bar">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
                    <a class="navbar-brand" href="#"><img src ="./logo/logo_letters_black.png" alt = "Logo" style = "width:120px; height:auto;"></a>
        </nav>
    </div>
</div>
</template>

<script>
export default {
    name:'HeaderArea',
    data(){
        return{}
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
