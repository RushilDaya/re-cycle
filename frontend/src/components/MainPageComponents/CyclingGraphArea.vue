<template>
    <div style="max-width:500px">
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
              backgroundColor: '#f87979',
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