<template>
<div id="outer-nav">
    <div id="nav-bar">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
                <a class="navbar-brand" href="#"></a>
	            <div class="icon-bar">
	            	<a @click="goMainScreen()"><img src ="./logo/logo_icon_black.png" alt = "Logo" style = "width:30px; height:auto; "></a>
	  				<a @click="goSocialScreen()"><i class="fa fa-users" style = "padding-left: 2em;"></i></a>
					<a @click="goDiscountScreen()"><i class="fa fa-ticket" style = "padding-left: 2em;"></i></a>
					<a @click="goProfileScreen()"><i class="fa fa-user-circle-o" style = "padding-left: 2em;"></i></a>
				</div>
				<a class="navbar-brand" href="#"></a>           
        </nav>
    </div>
</div>
</template>

<script>
export default {
    name:'FooterArea',
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

<style>

</style>
