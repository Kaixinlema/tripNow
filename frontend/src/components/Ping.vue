<template>
  <div>
    <p>name is: {{ name }}</p>

  </div>
</template>
 
<script>
import axios from 'axios';
 
export default {
  name: 'Ping',
  data: {
          id: '1',
          name: '',
        },
        watch : {
          my(v) {
            this.name = this.getName();
          }
  },
  methods: {
    getName() {
      const path = '/accounts';
      axios.get(path, {
        crossDomain: true,
        contentType: "application/json",
         params: {
            account: this.id,//接口配置参数（相当于url?id=xxxx）
          },
        }
        )
        .then((res) => {
          console.log(res.data['name']);
          this.msg = res.data['name'];
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
};
</script>
