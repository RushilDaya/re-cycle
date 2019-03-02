<template>
    <div id="profile-area">
        <div id="img-holder">
            <img src="../assets/man-profile-svgrepo-com.svg" /> 
        </div>
        <div id="data-holder">
            <table style="width:100%">
            <tr>
                <td class="left">Name</td>
                <td class="right">{{name}}</td>
            </tr>
             <tr>
                <td class="left">Age</td>
                <td class="right">{{age}}</td>
            </tr>
            <tr>
                <td class="left">City</td>
                <td class="right">{{city}}</td>
            </tr>
            <tr>
                <td class="left">Company</td>
                <td class="right">{{company}}</td>
            </tr>
            </table>
        </div>
    </div>
</template>

<script>
export default {
    name:'ProfilePage',
    data(){
        return{
            name:'',
            company:'',
            city:'',
            age:0
        }
    },
    mounted(){
        this.$http.get(this.FLASK_URL+'/api/user/'+this.LOGGED_IN_USER)
            .then(response => {
                this.name = response.data.name,
                this.company = response.data.company,
                this.age = response.data.age,
                this.city = response.data.city
            })
    }

}
</script>

<style scoped>
    #profile-area{
        width: 80%;
        max-width:300px;
        margin:auto;
    }
    #img-holder{
        margin:5%;
        text-align:center;
        box-shadow :#eeeeee 0px 2px 5px;
    }
    #data-holder{
        margin:5%;
        padding:5%;
        box-shadow :#eeeeee 0px 2px 5px;
    }
    .left{
        text-align:left;
    }
    .right{
        text-align:right;
        color:rgb(80,220,100);
    }
</style>
