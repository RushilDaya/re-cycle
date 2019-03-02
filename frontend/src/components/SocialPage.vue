<template>
<div id="social">
    <div class="card-item">
 	    <h5 style="text-align:center"> Social rankings </h5>
    </div>
    <div>
        <b-card class="card-item" no-body>
            <b-tabs card>
                <b-tab  title="Individual" active>
                    <table  class="table">
                            <thead>
                                <tr><th class="left">Name</th><th class="right">CO2 saved (kg)</th></tr>
                            </thead>
                            <tbody>
                                <tr v-for="(row,index) in users" :key="index">
                                    <td class="left">
                                        {{row.name}}
                                    </td>
                                    <td class="right">
                                        {{(0.1*row.totalkm).toFixed(2)}}
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                </b-tab>
                <b-tab title="Company">
                    <table class="table">
                            <thead>
                                <tr><th class="left">Company</th><th class="right">CO2 saved (kg pp)</th></tr>
                            </thead>
                            <tbody>
                                <tr v-for="(row, index) in companies"  :key="index">
                                    <td class="left">
                                        {{row.name}}
                                    </td>
                                    <td class="right">
                                        {{(0.1*row.totalkm).toFixed(2)}}
                                    </td>
                                </tr>
                        </tbody>
                    </table>
                </b-tab>
                <b-tab title="City">
                    <table class="table">
                            <thead>
                                <tr><th class="left">City</th><th class="right">CO2 saved (kg pp)</th></tr>
                            </thead>
                            <tbody>
                                <tr v-for="(row, index) in cities" :key="index">
                                    <td class="left">
                                        {{row.name}}
                                    </td>
                                    <td class="right">
                                        {{(0.1*row.totalkm).toFixed(2)}}
                                    </td>
                                </tr>
                        </tbody>
                    </table>
                </b-tab>
            </b-tabs>
        </b-card>
    </div>
</div>
</template>

<script>

    export default {
    name:'SocialPage',
    
    data() {
        return {
            users:[],
            cities:[],
            companies:[]
        }
    },
    mounted(){
            this.$http.get(this.FLASK_URL+'/api/topfive/users')
            .then(response => {
                this.users = this.mySort(response.data)
            })
            this.$http.get(this.FLASK_URL+'/api/topfive/cities')
            .then(response => {
                this.cities = this.mySort(response.data)
            })
            this.$http.get(this.FLASK_URL+'/api/topfive/companies')
            .then(response => {
                this.companies = this.mySort(response.data)
            })
    },
    methods:{
        mySort(myArray){
            console.log(myArray)
            return myArray.sort(function(a,b) {
                return b.totalkm - a.totalkm
            })
        }
    }
    }
</script>

<style scoped>
.card-item{
        margin-top: 10px;
		margin-bottom:10px;
        padding:10px;
        background-color:#fff;
        box-shadow: #eeeeee 0px 2px 5px;
        width:100%;
}
#social{
	    max-width:800px;
        margin:auto;
}
    .left{
        text-align:left;
    }
    .right{
        text-align:right;
        color:rgb(80,220,100);
    }

</style>
