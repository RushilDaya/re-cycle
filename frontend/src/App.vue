<template>
  <div id="app">
    <header-area> </header-area>
    <router-view/>
    <footer-area> </footer-area>
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
}
</style>
