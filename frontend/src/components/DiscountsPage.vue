<template>
<div style="background-color:#FFFFFF;">
<center>
<table style="width:100%" class="table">
	<thead class="thead-dark">
		<th scope="col"></th>
      	<th scope="col"> <center> Discount </center>
		</th>
    </thead>
 	<tbody>
		  <tr v-for="dis in discount">
		    <td>
		    	<center>
		    	<img v-bind:src="dis.img" width=auto height="80" alt="">
		    	</center>
		    </td>
		    <td style="text-align: center; vertical-align: middle;">
		    	<strong>
		    		<a :href="dis.url" style="font-size: 20px; color: green" ><center> {{ dis.userdiscount }}% </center> </a>
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



<style>


.gap-10 {
				width:100%;
				height:10px;
			}

.button1 {
		  width:100%;
		  background-color: white;
		  color: black;
		  border: 4px solid #4CAF50; /* Green */
}

</style>
