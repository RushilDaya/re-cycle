<template>
<div class="social">
    <h1>Weekly Rankings</h1>
    <div>
        <b-card no-body>
            <b-tabs pills card>
                <b-tab title="Individual Rankings" active></b-tab>
                    
                <b-tab title="Group Rankings"></b-tab>
            </b-tabs>
        </b-card>
    </div>
</div>
</template>

<script>
    export default {
    name:'SocialPage',
    data(){
        return{
            
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
  align-items: 50px;
}
</style>
