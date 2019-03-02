<template>
    <div id="help-area">
        <div class="card"> 
            <h3>
                What are credits?
            </h3>
            <hr>
            <p>
                This is your available mobility budget, this money can be
                used to purchase reduced rate travel tickets through any of our partner companies
            </p>

        </div> 
        <div class="card"> 
            <h3>
                What is your Cycling Score?
            </h3>
            <hr>
            <p>
                Your cycling score is based on the average distance you cycle in a week. This score is used to generate
                further reduce the cost of travel tickets you purchase through any of our partner companies
            </p>
        </div>
    </div>
</template>

<script>
export default {
    name:'Help'

}
</script>

<style scoped>
 #help-area{
        max-width:800px;
        margin:auto;
 }
 .card{
        margin-top: 10px;
        padding:10px;
        background-color:#fff;
        box-shadow: #eeeeee 0px 2px 5px;
        width:100%;
 }
</style>
