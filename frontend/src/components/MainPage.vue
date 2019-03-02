<template>
<div id="main-page">
    <discount-area :budget="userData.budget" :cycling_score="userData.discount_diff" class="main-block"> </discount-area>
    <cycling-graph-area :data='cyclingHistory' class="main-block"></cycling-graph-area>
    <display-average-area :average="averageCycle" class="main-block"></display-average-area>
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
            cyclingHistory:{},
            userData:{
                budget:0
            }
        }
    },
    computed:{
        averageCycle(){
            try{
                var a = (this.userData.total_kms/this.cyclingHistory.kms.length).toFixed(1)
                return a
            }
            catch(err){
                return 0
            }
        }
    },
    mounted(){
        this.$http.get(this.FLASK_URL+'/api/user/km/'+this.LOGGED_IN_USER)
            .then(response => {
                this.cyclingHistory = response.data
            })
        this.$http.get(this.FLASK_URL+'/api/user/'+this.LOGGED_IN_USER)
            .then(response =>{
                this.userData = response.data
            })
    }

}
</script>

<style scoped>
    #main-page{
        max-width:800px;
        margin:auto;
    }
    .main-block{
        margin-top: 10px;
        padding:10px;
        background-color:#fff;
        box-shadow: #eeeeee 0px 2px 5px;
        width:100%;
        text-align:center;
    }
</style>
