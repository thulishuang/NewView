<template>
	<el-row class="panel">
		<el-col :span="24" class="panel-top">
			<el-col :span="20" style="font-size:26px;">
				<img src="../assets/logo4.png" class="logo"> 
				<span>New<i style="color:#20a0ff">View</i></span>
			</el-col>
			<el-col :span="4">
				<el-tooltip class="item tip-logout" effect="dark" content="退出" placement="bottom" style="padding:0px;">
					<!-- <i class="logout" v-on:click="logout"></i> -->
					<i class="fa fa-sign-out" aria-hidden="true" v-on:click="logout"></i>
				</el-tooltip>
			</el-col>
		</el-col>
		<el-col :span="24" class="panel-center">
			<aside style="width:230px;">
				<el-menu style="border-top: 1px solid #475669;" default-active="/table" class="el-menu-vertical-demo" @open="handleopen"
					@close="handleclose" @select="handleselect" theme="dark" unique-opened router>
					<template v-for="(item,index) in $router.options.routes" v-if="!item.hidden">
						<el-submenu :index="index+''" v-if="!item.leaf">
							<template slot="title"><i :class="item.iconCls"></i>{{item.name}}</template>
							<el-menu-item v-for="child in item.children" :index="child.path">{{child.name}}</el-menu-item>
						</el-submenu>
						<el-menu-item v-if="item.leaf&&item.children.length>0" :index="item.children[0].path"><i :class="item.iconCls"></i>{{item.children[0].name}}</el-menu-item>
					</template>
				</el-menu>
			</aside>
			<section class="panel-c-c">
				<div class="grid-content bg-purple-light">
					<el-col :span="24" style="margin-bottom:15px;">
					</el-col>
					<el-col :span="24" style="background-color:#fff;box-sizing: border-box;">
						<transition name="fade">
							<router-view></router-view>
						</transition>
					</el-col>
				</div>
			</section>
		</el-col>
	</el-row>
</template>

<script>
	import $ from 'jquery'
	function csrfSafeMethod(method) {  
	  // these HTTP methods do not require CSRF protection  
	  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));  
	}  
	function sameOrigin(url) {  
	  // test that a given url is a same-origin URL  
	  // url could be relative or scheme relative or absolute  
	  var host = document.location.host; // host + port  
	  var protocol = document.location.protocol;  
	  var sr_origin = '//' + host;  
	  var origin = protocol + sr_origin;  
	  // Allow absolute or scheme relative URLs to same origin  
	  return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||  
	    (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||  
	    // or any other URL that isn't scheme relative or absolute i.e relative.  
	    !(/^(\/\/|http:|https:).*/.test(url));  
	}  
	function getCookie(name) {  
	  var cookieValue = null;  
	  if (document.cookie && document.cookie != '') {  
	    var cookies = document.cookie.split(';');  
	    for (var i = 0; i < cookies.length; i++) {  
	      var cookie = $.trim(cookies[i]);  
	      // Does this cookie string begin with the name we want?  
	      if (cookie.substring(0, name.length + 1) == (name + '=')) {  
	        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));  
	        break;  
	      }  
	    }  
	  }  
	  return cookieValue;  
	}   
	var csrftoken = getCookie('csrftoken');  
	$.ajaxSetup({  
	    beforeSend: function(xhr, settings) {  
	        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {  
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);  
	        }  
	    }  
	});
	export default {
		data() {
			return {
			currentPathName:'Table',
			currentPathNameParent:'导航一',
				form: {
					name: '',
					region: '',
					date1: '',
					date2: '',
					delivery: false,
					type: [],
					resource: '',
					desc: ''
				}
			}
		},
	watch: {
		'$route' (to, from) {//监听路由改变
			this.currentPathName=to.name;
			this.currentPathNameParent=to.matched[0].name;
		}
	},
		methods: {
			onSubmit() {
				// console.log('submit!');
			},
			handleopen(){
				//console.log('handleopen');
			},
			handleclose(){
				//console.log('handleclose');
			},
			handleselect:function(a,b){
			},
			//退出登录
			logout:function(){
				var _this=this;
				this.$confirm('确认退出吗?', '提示', {
					//type: 'warning'
				}).then(() => {
					$.post("/api/account/logout",{},
							function(data,status){
								if (data['error_code'] == 0) {
									_this.$router.replace('/login');
								}
								else {
									_this.$confirm('登出错误', '提示', {
										//type: 'warning'
									}).then(() => {

									}).catch(() => {
												
									});
									return false;
								}              
							});
				}).catch(() => {
					
				});

				
			}
		}
	}
</script>

<style scoped>
	.fade-enter-active,
	.fade-leave-active {
		transition: opacity .5s
	}
	
	.fade-enter,
	.fade-leave-active {
		opacity: 0
	}
	
	.panel {
		position: absolute;
		top: 0px;
		bottom: 0px;
		width: 100%;
	}
	
	.panel-top {
		height: 60px;
		line-height: 60px;
		background: #1F2D3D;
		color: #c0ccda;
	}
	
	.panel-center {
		background: #324057;
		position: absolute;
		top: 60px;
		bottom: 0px;
		overflow: hidden;
	}
	
	.panel-c-c {
		background: #f1f2f7;
		position: absolute;
		right: 0px;
		top: 0px;
		bottom: 0px;
		left: 230px;
		overflow-y: scroll;
		padding: 20px;
	}
	

	
	.logo {
		width: 40px;
		float: left;
		margin: 10px 10px 10px 18px;
	}
	
	.tip-logout {
		float: right;
		margin-right: 20px;
		padding-top: 5px;
		cursor: pointer;
	}
	
	.admin {
		color: #c0ccda;
		text-align: center;
	}
</style>