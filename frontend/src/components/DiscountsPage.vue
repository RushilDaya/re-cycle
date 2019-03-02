<template>
<div id="discounts-page">
<center>
<div class="card-item">
 	<h5>	Purchase  </h5>
</div>
<table style="width:100%" class="table">
 	<tbody>
		  <tr v-for="dis in discount" class="card-item">
		    <td class="left">
		    	<img v-bind:src="dis.img" width=auto height="80" alt="">
		    </td>
		    <td class="right" style="vertical-align: middle;">
                <strong v-if="showMore.filter(e=> e.name===dis.name)[0].state">
                    <p>
                        {{dis.tax}}% fixed tax reduction + {{0.01*dis.company_rate*dis.user_rate}}% cycle score reduction
                    </p>
                </strong>
		    	<strong v-else>
		    		<a :href="dis.url" >
						<button  type="button" class="btn" style="font-size: 25px">
                             {{ (dis.tax + 0.01*dis.company_rate*dis.user_rate).toFixed(1) }}% <div style="font-size:15px">  rate reduction
                                </div> 
						</button>
                    </a>
		    	</strong>
                <div> <i style ="color:rgb(80,220,100)" class="fa fa-exchange" @click='toggleState(dis.name)' /> </div>
			</td>
		  </tr>
	</tbody>
</table> 
</center>



<div class="gap-10"></div>


</div>
</template>

<script>
export default {
    name:'DiscountsPage',
    data(){
        return{
            discount:[],
            showMore:[]
        }
    },
    mounted(){
        this.$http.get(this.FLASK_URL+'/api/discount/'+this.LOGGED_IN_USER)
            .then(response => {
                this.discount = response.data;
                this.showMore = this.discount.map(e => e.name).map(e  =>({ name:e,state:false}))
            })        
    },
    methods:{
        toggleState(name){
            console.log(name)
            var index = this.showMore.map(e => e.name).indexOf(name)
            console.log(index)
            this.showMore[index].state = !this.showMore[index].state
        }
    }



}
</script>



<style scoped>
#discounts-page{
	    max-width:800px;
        margin:auto;
}
.card-item{
        margin-top: 10px;
		margin-bottom:10px;
        padding:10px;
        background-color:#fff;
        box-shadow: #eeeeee 0px 2px 5px;
        width:100%;
}

.left{
	padding-left:30px;
}
.right{
	text-align:right;
	padding-right:30px;
}

    .btn{
        margin-left:30px;
        background-color:rgb(80,220,100);
        color:white;
    }

</style>
