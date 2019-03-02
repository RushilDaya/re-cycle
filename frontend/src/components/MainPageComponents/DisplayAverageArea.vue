<template>
    <div>
        <h1> You Averaged {{average}} KMs in last {{num_days}} days </h1>
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
