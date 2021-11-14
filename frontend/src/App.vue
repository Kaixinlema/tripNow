<template>
  <div id="app">
    <router-view v-if="isRouterAlive" />
    <Footer></Footer>
  </div>
</template>

<script>
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
      isRouterAlive:true
    }
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
