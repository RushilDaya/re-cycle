<template>
    <div>
        <h5> available credits: <i id="amount">{{budget}}</i>  
            <button  type="button" class="btn" @click="goDiscountScreen()"> buy <i 	class="fa fa-arrow-circle-right" /> </button>
        </h5>
    </div>
</template>

<script>
export default {
    name:'DiscountArea',
    props:['budget'],
    data(){
        return{}
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