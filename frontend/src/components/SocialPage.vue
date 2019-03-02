<template>
<div class="social">
    <h1>Weekly Rankings</h1>
    <div>
        <b-card no-body>
            <b-tabs pills card>
                <b-tab title="Individual" active>
                    <table class="table">
                            <thead>
                                <tr><th>#</th><th>Name</th><th>CO2 Prevented</th></tr>
                            </thead>
                            <tbody>
                                <tr v-for="(row,index) in users" :key="index">
                                    <td>
                                        {{ index +1 }}
                                    </td>
                                    <td>
                                        {{row.name}}
                                    </td>
                                    <td>
                                        {{row.totalkm}}
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                </b-tab>
                <b-tab title="Company">
                    <table class="table">
                            <thead>
                                <tr><th>#</th><th>Company</th><th class>CO2 Prevented</th></tr>
                            </thead>
                            <tbody>
                                <tr v-for="(row, index) in companies"  :key="index">
                                    <td>
                                        {{ index +1 }}
                                    </td>
                                    <td>
                                        {{row.name}}
                                    </td>
                                    <td>
                                        {{row.totalkm}}
                                    </td>
                                </tr>
                        </tbody>
                    </table>
                </b-tab>
                <b-tab title="City">
                    <table class="table">
                            <thead>
                                <tr><th>#</th><th>City</th><th>CO2 Prevented</th></tr>
                            </thead>
                            <tbody>
                                <tr v-for="(row, index) in cities" :key="index">
                                    <td>
                                        {{ index +1 }}
                                    </td>
                                    <td>
                                        {{row.name}}
                                    </td>
                                    <td>
                                        {{row.totalkm}}
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

<style>

</style>
