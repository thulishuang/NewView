
import Vue from 'vue'
import App from './App'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
import VueRouter from 'vue-router'
import store from './vuex/store'
import Vuex from 'vuex'
import NProgress from 'nprogress'//页面顶部进度条
import 'nprogress/nprogress.css'
import $ from 'jquery'

import Login from './components/Login.vue'
import Home from './components/Home.vue'
import Table from './components/nav1/Table.vue'
import Form from './components/nav1/Form.vue'
import Page1 from './components/nav2/Page1.vue'


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
    name: '',
    iconCls: 'el-icon-message',//图标样式class
    leaf:true,
    children: [
      { path: '/roomlist', component: Form, name: '房间' },
    ]
  },
  {
    path: '/',
    component: Home,
    name: '导航二',
    iconCls: 'fa fa-id-card-o',
    leaf:true,
    children: [
      { path: '/interviewee', component: Table, name: '候选人' },
    ]
  },
  {
    path: '/',
    component: Home,
    name: '',
    iconCls: 'fa fa-line-chart',
    leaf: true,//只有一个节点
    children: [
      { path: '/page1', component: Page1, name: '服务' }
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

$.get("/api/account/login",{},
    function(data,status){
      if (data['error_code'] == 0) {
        router.replace('/roomlist');
        console.log(data['error_code']);
      }
      else {
        router.replace('/login')
      }              
    });


