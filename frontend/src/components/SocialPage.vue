<template>
<div class="social">
    <h1>Weekly Rankings</h1>
    <div>
        <b-card no-body>
            <b-tabs pills card>
                <b-tab title="Individual" active>
                    <table class="table table-hover">
                            <thead>
                                <tr><th>#</th><th>Name</th><th>CO2 Prevented</th><th>Company</th><th>City</th></tr>
                            </thead>
                            <tbody>
                                <tr v-for="(row,index) in rows" :key="index">
                                    <td>
                                        {{ index +1 }}
                                    </td>
                                    <td>
                                        {{row.name}}
                                    </td>
                                    <td>
                                        {{row.co2}}
                                    </td>
                                    <td>
                                        {{row.company}}
                                    </td>
                                    <td>
                                        {{row.city}}
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                </b-tab>
                <b-tab title="Company">
                    <table class="table table-hover">
                            <thead>
                                <tr><th>#</th><th>Company</th><th class>CO2 Prevented</th><th>City</th></tr>
                            </thead>
                            <tbody>
                                <tr v-for="(row, index) in rows"  :key="index">
                                    <td>
                                        {{ index +1 }}
                                    </td>
                                    <td>
                                        {{row.company}}
                                    </td>
                                    <td>
                                        {{row.co2}}
                                    </td>
                                    <td>
                                        {{row.city}}
                                    </td>
                                </tr>
                        </tbody>
                    </table>
                </b-tab>
                <b-tab title="City">
                    <table class="table table-hover">
                            <thead>
                                <tr><th>#</th><th>City</th><th>CO2 Prevented</th></tr>
                            </thead>
                            <tbody>
                                <tr v-for="(row, index) in rows" :key="index">
                                    <td>
                                        {{ index +1 }}
                                    </td>
                                    <td>
                                        {{row.city}}
                                    </td>
                                    <td>
                                        {{row.co2}}
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
            rows: []
                }
    },
    mounted() {
        var rows = [
                { name: "Murilo Cunha", co2: 100000, company: 'Brazil', city: "Sao Paulo" },
                { name: "Rushil Daya", co2: 10000, company: 'Mothaland', city: "Johaa" },
                { name: "Massi Picano", co2: 1000, company: 'Cataluna', city: "Barcelona" },
                { name: "Nachito", co2: 100, company: 'The enemy', city: "Merengue" },
                { name: "Mr. Rocketo", co2: 10, company: 'Cern', city: "Hydron Colider" },
                ]
        this.rows = this.sort(rows)
    },
    methods:{
        sort(rows) {
            return rows
        }

    }
    }
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Montserrat:400,700');
h1 {
  font-family: 'Montserrat', sans-serif;
  display: grid;
  grid-template-rows: auto;
  justify-items: center;
  align-items: 100%;
}
</style>
<!--<li v-for="(name, co2, city) in item":key="index">{{name.item, co2.item, city.item}}