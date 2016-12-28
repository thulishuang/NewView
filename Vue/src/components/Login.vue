<template>
  <el-form :model="ruleForm2" :rules="rules2" ref="ruleForm2" label-position="left" label-width="0px" class="demo-ruleForm card-box loginform">
	<h3 class="title">登录</h3>
	<el-form-item prop="account">
	  <el-input type="text" v-model="ruleForm2.account" auto-complete="off" placeholder="账号"></el-input>
	</el-form-item>
	<el-form-item prop="checkPass">
	  <el-input type="password" v-model="ruleForm2.checkPass" auto-complete="off" placeholder="密码"></el-input>
	</el-form-item>
	<el-form-item style="width:100%;">
	  <el-button type="primary" style="width:100%;" @click.native.prevent="handleSubmit2">登录</el-button>
	</el-form-item>
  </el-form>
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
		ruleForm2: {
		  account: '',
		  checkPass: ''
		},
		rules2: {
		  account: [
			{ required: true, message: '请输入账号', trigger: 'blur' },
		  ],
		  checkPass: [
			{ required: true, message: '请输入密码', trigger: 'blur' },
		  ]
		},
	  };
	},
	methods: {
	  handleReset2() {
		this.$refs.ruleForm2.resetFields();
	  },
	  handleSubmit2(ev) {
		var _this = this;
		$.post("/api/account/login",
			{
			  username:_this.ruleForm2['account'],
			  password:_this.ruleForm2['checkPass'],
			},
			function(data,status){
			  if (data['error_code'] == 0) {
				_this.$router.replace('/roomlist');
			  }
			  else {
				_this.$confirm('用户名或密码错误', '提示', {
				  //type: 'warning'
				}).then(() => {
				  _this.$router.replace('/login');
				  _this.ruleForm2['account'] = ''
				  _this.ruleForm2['checkPass'] = ''
				}).catch(() => {
					  
				});
				return false;
			  }              
			});
	  }
	}
  }
</script>

<style scoped>
  .card-box {
	padding: 20px;
	/*box-shadow: 0 0px 8px 0 rgba(0, 0, 0, 0.06), 0 1px 0px 0 rgba(0, 0, 0, 0.02);*/
	-webkit-border-radius: 5px;
	border-radius: 5px;
	-moz-border-radius: 5px;
	background-clip: padding-box;
	margin-bottom: 20px;
	background-color: #F9FAFC;
	margin: 120px auto;
	width: 400px;
	border: 2px solid #8492A6;
  }
  
  .title {
	margin: 0px auto 40px auto;
	text-align: center;
	color: #505458;
  }
  
  .loginform {
	width: 350px;
	padding: 35px 35px 15px 35px;
  }
</style>