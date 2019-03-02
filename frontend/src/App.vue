<template>
  <div id="app">
    <header-area> </header-area>
    <router-view/>
    <footer-area class="footer"> </footer-area>
  </div>
</template>

<script>
import HeaderArea from '@/components/HeadAndFoot/HeaderArea'
import FooterArea from '@/components/HeadAndFoot/FooterArea'
export default {
  name: 'App',
  components:{HeaderArea, FooterArea}
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin-bottom: 40px;
}

.footer {
    position: fixed; 
    bottom: 0;
    left: 0;
    right: 0;
    height: 50px;
    display: inline-block;
}

</style>
