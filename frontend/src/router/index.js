import Vue from 'vue'
import Router from 'vue-router'
import Container from '@/components/Container'
import Login from '../components/Login'
import Register from '../components/Register'
import Ping from '../components/Ping.vue';

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: Container,
      meta: {
        title: 'System'
      }
    },
    {
      path: '/login',
      component: Login,
      meta: {
        title: 'System'
      }
    },
    {
      path: '/register',
      component: Register,
      meta: {
        title: 'System'
      }
    },
    {
      path: '/ping', 
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/ping_xyz',
      name: 'Ping',
      component: Ping,
    },
  ]
})
