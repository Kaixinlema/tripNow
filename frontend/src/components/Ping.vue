<template>

  <div>

    <p>{{ msg }}</p>
  </div>
</template>
 
<script>
import axios from 'axios';
 
export default {
  name: '',
  data() {
    return {
      msg: [],
      isLoading: true,
    };
  },

  methods: {
    getMessage() {
      const path = 'http://localhost:5000/users';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
          console.log(this.msg)
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
   
  },
  created() {
    this.getMessage();
  },
};
</script>
<style>
.fade-enter,
.fade-leave-active {
  opacity: 0;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
</style>