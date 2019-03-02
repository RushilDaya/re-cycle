<template>
    <div>
        <h4> 
            your daily cycling average is {{average}} km
        </h4>
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
