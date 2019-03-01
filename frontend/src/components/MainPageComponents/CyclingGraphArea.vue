<template>
    <div>
        <h1> {{test}} </h1>
    </div>
</template>

<script>
export default {
    name:'CyclingGraphArea',
    data(){
        return{
            test:''
        }
    },
    mounted(){
        // this.$http.get(this.FLASK_URL)
        //     .then(response => this.test = response.data)
    }
}
</script>

<style>

</style>