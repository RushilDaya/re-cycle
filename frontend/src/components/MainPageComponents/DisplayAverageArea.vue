<template>
    <div>
        <h5> 
            your daily average is {{average}} km
        </h5>
    </div>
</template>

<script>
export default {
    name:'DisplayAverageArea',
    props:['average'],
    data(){
        return {}
    }
}
</script>

<style>

</style>
