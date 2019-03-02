<template>
    <div>
        <bar-chart :chart-data="datacollection" :options="options"></bar-chart>
    </div>
</template>

<script>
import BarChart from './BarChart.js';
export default {
    name:'CyclingGraphArea',
    props:['data'],
    components:{BarChart},
    data(){
        return{
            options:{
                title:{
                    display: true,
                    text: 'Your Cycling History (in KM)'
                },
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero:true
                        }
                    }]
                },
                legend:{
                    display:false
                }
            }
        }
    },
    computed:{
        datacollection(){
            return {
                        labels: this.data.dates,
                        datasets: [
                            {
                            label: 'Daily Cycle (KM)',
                            backgroundColor: 'rgb(80,220,100)',
                            data: this.data.kms
                            }
                        ]
                    }
        }
    }
}
</script>

<style>

</style>