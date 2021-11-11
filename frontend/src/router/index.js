import Vue from 'vue'
import Router from 'vue-router'
import Container from '@/components/Container'
import Login from '../components/Login'
import Register from '../components/Register'
import Plan from '../components/Plan'

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
      path: '/plan',
      component: Plan,
    },
  ]
})
