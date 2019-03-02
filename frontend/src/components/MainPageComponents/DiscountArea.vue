<template>
    <div>
            <table style="width:100%">
                <tr>
                    <td class="left" style="font-size:15px">Credits <i class="fa fa-question-circle" style="color:rgb(80,220,100)"/> </td>
                    <td class="right"> &euro; {{budget.toFixed(2)}}</td>
                </tr>
                <tr>
                    <td class="left" style="font-size:15px">Cycling Score <i class="fa fa-question-circle" style="color:rgb(80,220,100)"/> </td>
                    <td class="right"> {{cycling_score}} </td>
                </tr>
                <tr>
                    <td></td>
                </tr>
                <tr>
                    <td></td>
                </tr>
                <tr >
                    <td> </td>
                    <td class="right"><button  type="button" class="btn" @click="goDiscountScreen()"> Buy mobility services <i 	class="fa fa-arrow-circle-right" /> </button></td>
                </tr>
            </table>
    </div>
</template>

<script>
export default {
    name:'DiscountArea',
    props:['budget','cycling_score'],
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
    .left{
        text-align:left;
    }
    .right{
        text-align:right;
        color:rgb(80,220,100);
    }
    tr{
        font-size:20px;
    }
</style>