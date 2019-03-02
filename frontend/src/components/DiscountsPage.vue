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
		    	<strong>
		    		<a :href="dis.url" >
						<button  type="button" class="btn" style="font-size: 25px" > {{ dis.userdiscount.toFixed(1) }}% <div style="font-size:15px">  rate reduction</div> 
						</button></a>
		    	</strong>
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
        	discount:[]
        }
    },
    mounted(){
        this.$http.get(this.FLASK_URL+'/api/discount/'+this.LOGGED_IN_USER)
            .then(response => {
                this.discount = response.data
            })        
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
