import Vue from 'vue'
import App from './App'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
import VueRouter from 'vue-router'
import store from './vuex/store'
import Vuex from 'vuex'
import NProgress from 'nprogress'//页面顶部进度条
import 'nprogress/nprogress.css'

import Login from './components/Login.vue'
import Home from './components/Home.vue'
import Main from './components/Main.vue'
import Table from './components/nav1/Table.vue'
import Form from './components/nav1/Form.vue'
import Page3 from './components/nav1/Page3.vue'
import Page4 from './components/nav2/Page4.vue'
import Page5 from './components/nav2/Page5.vue'
import Page6 from './components/nav3/Page6.vue'

Vue.use(ElementUI)
Vue.use(VueRouter)
Vue.use(Vuex)

const routes = [
  {
    path: '/login',
    component: Login,
    hidden: true//不显示在导航中
  },
  //{ path: '/main', component: Main },

  {
    path: '/',
    component: Home,
    name: '',
    iconCls: 'el-icon-message',//图标样式class
    leaf:true,
    children: [
      //{ path: '/main', component: Main },
      { path: '/table', component: Form, name: '房间' },
    ]
  },
  {
    path: '/',
    component: Home,
    name: '导航二',
    iconCls: 'fa fa-id-card-o',
    leaf:true,
    children: [
      { path: '/page4', component: Table, name: '候选人' },
    ]
  },
  {
    path: '/',
    component: Home,
    name: '',
    iconCls: 'fa fa-line-chart',
    leaf: true,//只有一个节点
    children: [
      { path: '/page6', component: Page6, name: '服务' }
    ]
  }
]

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  NProgress.start();
  next()
})

router.afterEach(transition => {
  NProgress.done();
});

new Vue({
  el: '#app',
  template: '<App/>',
  router,
  store,
  components: { App }
  //render: h => h(Login)
}).$mount('#app')

router.replace('/login')


