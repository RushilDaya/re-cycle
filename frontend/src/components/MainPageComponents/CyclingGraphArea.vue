<template>
    <div>
        <bar-chart :chart-data="datacollection" :options="options"></bar-chart>
    </div>
</template>

<script>
import BarChart from './BarChart.js';
export default {
    name:'CyclingGraphArea',
    components:{BarChart},
    data(){
        return{
            datacollection: null,
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
    mounted(){
     this.fillData()
    },
    methods:{
      fillData () {
        this.datacollection = {
          labels: ['monday', 'tuesday','wednesday', 'thursday', 'friday','saturaday','sunday'],
          datasets: [
            {
              label: 'Daily Cycle (KM)',
              backgroundColor: 'rgb(80,220,100)',
              data: [7, 5, 9, 8, 8,2,1]
            }
          ]
        }
      }
    }
}
</script>

<style>

</style>