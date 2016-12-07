import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
import App from './App.vue'
import VueRouter from 'vue-router'
import store from './vuex/store'
import Vuex from 'vuex'

import Login from './conponents/Login.vue'
import HR from './conponents/HR.vue'
import Candidate from './conponents/Candidate.vue'
import Room from './conponents/Room.vue'
import Resiger from './conponents/Resiger.vue'

Vue.use(ElementUI)
Vue.use(VueRouter)
Vue.use(Vuex)

const routes = [
  {
    path: '/login',
    component: Login,
    hidden: true//不显示在导航中
  },
  {
    path: '/',
    component: Home,
    name: '导航一',
    iconCls: 'el-icon-message',//图标样式class
    children: [
      //{ path: '/main', component: Main },
      { path: '/hr', component: HR, name: 'HR' },
      { path: '/candidate', component: Candidate, name: 'Candidate' },
      { path: '/room', component: Room, name: 'Room' },
    ]
  },
  // {
  //   path: '/',
  //   component: Home,
  //   name: '',
  //   iconCls: 'fa fa-line-chart',
  //   leaf: true,//只有一个节点
  //   children: [
  //     { path: '/page6', component: Page6, name: '导航三' }
  //   ]
  // }
]

const router = new VueRouter({
	routes
})

new Vue({
  el: '#app',
  template: '<App/>',
  router,
  store,
  // h = h(App)
  components: { App }
}).$mount('#app')

router.replace('/login')