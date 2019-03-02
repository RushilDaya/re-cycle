<template>
<div style="background-color:#FFFFFF;">
<center>
<table style="width:100%" class="table">
	<thead class="thead-dark">
		<th scope="col"></th>
      	<th scope="col"> Discount </th>
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
		    		<a v-bind:href="dis.url" style="font-size: 20px; color: green" ><center> {{ dis.userdiscount }}% </center> </a>
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
        	discount:[
	        	{name: 'blablacar',
	        	userdiscount: 21.23,
	        	img: 'https://blog.blablacar.es/wp-content/uploads/2018/01/BBC_horizontal_positive_1002x274%20(1).png',
	        	url: 'https://www.blablacar.com/'},
	        	{name: 'uber',
	        	userdiscount: 23.45,
	        	img: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSxCihfF8hj92MbylUESP6yfSAOrH8nK57V2S_1FcCYh6YGyJE',
	        	url: 'https://www.uber.com/be/en/'},
	        	{name: 'velo',
	        	userdiscount: 17.89,
	        	img: 'https://www.velo.be/sites/all/themes/velo/images/transparant.png',
	        	url: 'https://www.velo.be/nl'}
        	]
        }
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
