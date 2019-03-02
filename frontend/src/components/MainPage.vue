<template>
<div>
    <discount-area class="main-block"> </discount-area>
    <cycling-graph-area class="main-block"></cycling-graph-area>
    <display-average-area class="main-block"></display-average-area>
</div>
</template>

<script>
import DiscountArea from '@/components/MainPageComponents/DiscountArea'
import DisplayAverageArea from '@/components/MainPageComponents/DisplayAverageArea'
import CyclingGraphArea from '@/components/MainPageComponents/CyclingGraphArea'

export default {
    name:'MainPage',
    components:{DiscountArea, DisplayAverageArea, CyclingGraphArea},
    data(){
        return{

        }
    }

}
</script>

<style scoped>
    .main-block{
        margin-top: 10px;
        padding:10px;
        background-color:#fff;
        box-shadow: #eeeeee 0px 2px 5px;
        width:100%;
        text-align:center;
    }
</style>
