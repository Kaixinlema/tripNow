import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

import Router from 'vue-router'
import Container from '@/components/Container'
import Login from '../components/Login'
import Register from '../components/Register'
import Ping from '../components/Ping'
import Plan from '../components/Plan'
import Choice from '../components/Choice'
import Result from '../components/Result'
Vue.use(Router)

export default new Router({
  mode: 'history',
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
      name: 'plan',
      path: '/plan',
      component: Plan,
    },
    {
      name: 'choice',
      path: '/choice',
      component: Choice,
    },
    {
      path: '/result',
      component: Result,
    },
    {
      path: '/try',
      component: Try,
    },
  ]
})
