<template>
  <div id="app">
    <router-view v-if="isRouterAlive" />
    <Footer></Footer>
  </div>
</template>

<script>
import { MP } from '../map.js'    //引入上面创建的map.js文件

  import Footer from '@/components/Footer.vue'

  export default {
    name: "App",
    provide(){
    return{
      reload:this.reload
    }
  },
  data(){
    return{
      isRouterAlive:true,
      ak: "nGv0mHXo2BGuNmN4s7nazQSSBnZs4PGQ",
    }
  },
  async mounted(){
      await MP(this.ak);
  },
    components: {
      Footer,
    },
    methods:{
       reload (){
       this.isRouterAlive = false
       this.$nextTick(function(){
          this.isRouterAlive = true
       })
    }
    }
  };
</script>

<style>

</style>
