<template>
<div>
    <discount-area> </discount-area>
    <display-average-area></display-average-area>
    <cycling-graph-area></cycling-graph-area>
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

<style>

</style>
