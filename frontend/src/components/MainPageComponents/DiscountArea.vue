<template>
    <div>
        <h5> you have <i id="amount">{{points}}</i> points 
            <button  type="button" class="btn" @click="goDiscountScreen()"> spend <i 	class="fa fa-arrow-circle-right" /> </button>
        </h5>
    </div>
</template>

<script>
export default {
    name:'DiscountArea',
    data(){
        return{
            points: 50
        }
    },
    methods:{
        goDiscountScreen(){
            this.$router.push('/discount')
        }
    }
}
</script>

<style scoped>
    #amount{
        color:rgb(80,220,100);
        font-style:normal;
    }
    .btn{
        margin-left:30px;
        background-color:rgb(80,220,100);
        color:white;
    }
</style>