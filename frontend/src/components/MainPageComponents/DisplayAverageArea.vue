<template>
    <div>
        <h5> 
             you cycled an average of {{average}} km/day in the past {{num_days}} days
        </h5>
    </div>
</template>

<script>
export default {
    name:'DisplayAverageArea',
    data(){
        return {
            average: 10.5,
            num_days: 7
        }
    }
}
</script>

<style>

</style>
