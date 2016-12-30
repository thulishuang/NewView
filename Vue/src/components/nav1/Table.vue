<template>
	<section>
		<!--工具条-->
		<el-col :span="24" class="toolbar">
			<el-form :inline="true" :model="formInline" class="demo-form-inline">
				<el-form-item>
					<el-button @click="handleAdd">新增</el-button>
				</el-form-item>
			</el-form>
		</el-col>

		<!--列表-->
		<template>
			<el-table :data="tableData" highlight-current-row v-loading="listLoading" style="width: 100%;">
				<el-table-column prop="num" label="ID" width="50">
				</el-table-column>
				<el-table-column prop="username" label="姓名" width="100">
				</el-table-column>
				<el-table-column prop="email" label="邮箱" width="150" :formatter="formatSex">
				</el-table-column>
				<el-table-column prop="telephone" label="手机号码" width="150">
				</el-table-column>
				<el-table-column prop="address" label="地址" width="180">
				</el-table-column>
				<el-table-column prop="roomnum" label="面试房间" width="100">
				</el-table-column>
				<el-table-column prop="state" label="状态">
				</el-table-column>
				<el-table-column inline-template :context="_self" label="操作" width="260">
					<span>
					<el-button type="text" size="small" @click="handleEdit(row)">编辑</el-button>
					<el-button type="text" size="small" @click="handleDel(row)">删除</el-button>
					<el-button type="text" size="small" @click="handleInvite(row)">邀请面试</el-button>
					<el-button type="text" size="small" @click="handleView(row)">查看面试报告</el-button>
				</span>
				</el-table-column>
			</el-table>
		</template>

		<!--编辑界面-->
		<el-dialog :title="editFormTtile" v-model="editFormVisible" :close-on-click-modal="false">
			<el-form :model="editForm" label-width="80px" :rules="editFormRules" ref="editForm">
				<el-form-item label="姓名" prop="username">
					<el-input v-model="editForm.name" auto-complete="off"></el-input>
				</el-form-item>
				<el-form-item label="邮箱">
					<el-input type="textarea" v-model="editForm.mail"></el-input>
				</el-form-item>
				<el-form-item label="手机号码">
					<el-input type="textarea" v-model="editForm.phonenumber"></el-input>
				</el-form-item>
				<el-form-item label="地址">
					<el-input type="textarea" v-model="editForm.addr"></el-input>
				</el-form-item>
				<el-form-item label="面试房间">
				  <el-col :span="12" class="tac">
				    <el-autocomplete
				      class="inline-input"
				      v-model="state1"
				      :fetch-suggestions="querySearch"
				      placeholder="请输入内容"
				      @select="handleSelect"
				    ></el-autocomplete>
				  </el-col>
				</el-form-item>
			</el-form>
			<div slot="footer" class="dialog-footer">
				<el-button @click.native="editFormVisible = false">取消</el-button>
				<el-button type="primary" @click.native="editSubmit" :loading="editLoading">{{btnEditText}}</el-button>
			</div>
		</el-dialog>
	</section>
</template>
<script src="//unpkg.com/vue/dist/vue.js"></script>
<script src="//unpkg.com/element-ui/lib/index.js"></script>
<script>
	import $ from 'jquery'
	import NProgress from 'nprogress'//页面顶部进度条
	import 'nprogress/nprogress.css'
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
      	rooms: [],
        state1: '',
				formInline: {
					user: ''
				},
				pickerOptions0: {
					disabledDate(time) {
						return time.getTime() < Date.now() - 8.64e7;
					}
				},
				value1:'',
				editFormVisible:false,//编辑界面显是否显示
				editFormTtile:'编辑',//编辑界面标题
				//编辑界面数据
				editForm: {
					id:0,
					room:'',
					name: '',
					mail: '',
					phonenumber:'',
					addr: '',
					state: '',
					roomnum: ''
				},
				editLoading:false,
				btnEditText:'提 交',
				editFormRules:{
					name:[
						{ required: true, message: '请输入姓名', trigger: 'blur' }
					]
				},
				tableData: [],
				listLoading:false
     		}
    },
    created: function(){
      var _this = this;
      $.get("/api/account/detail/interviewee_list",{},
        function(data,status){
          _this.tableData = data['interviewee_list'];
          for(var i = 0; i < _this.tableData.length; i++){
          	if (_this.tableData[i].state == false) {
          		_this.tableData[i].state = '未邀请';
          	}
          	else {
          		_this.tableData[i].state = '已邀请';
          	}
          }
      });
    },
    // update: function(){
    //   var _this = this;
    //   $.get("/api/account/detail/interviewee_list",{},
    //     function(data,status){
    //       _this.tableData = data['interviewee_list'];
    //       for(var i = 0; i < _this.tableData.length; i++){
    //       	if (_this.tableData[i].state == false) {
    //       		_this.tableData[i].state = '未邀请';
    //       	}
    //       	else {
    //       		_this.tableData[i].state = '已邀请';
    //       	}
    //       }
    //   });
    // },
    methods: {
    	querySearch(queryString, cb) {
        var rooms = this.rooms;
        var results = queryString ? rooms.filter(this.createFilter(queryString)) : rooms;
        // 调用 callback 返回建议列表的数据
        cb(results);
      },
      createFilter(queryString) {
        return (room) => {
          return (room.value.indexOf(queryString.toLowerCase()) === 0);
        };
      },
      loadAll() {
      	var _this = this;
      	var rooms = [];
      	var tmproom = {value:"ss",id: 1};
      	var tmp;
      	$.get("/api/account/detail/room_list",{},
      	  function(data,status){
      	    tmp = data['roomlist'];
      	    for(var i = 0; i < tmp.length; i++){
      	      tmproom.value = "房间" + tmp[i].num + ": " + tmp[i].title;
      	      tmproom.id = tmp[i].num;
      	      rooms[i] = tmproom;
      	    }
      	});
        return rooms;
      },
      handleSelect(item) {
        console.log(item);
        this.editForm.roomnum = item.id;
      },
			//删除记录
			handleDel:function(row){
        var _this = this;
        _this.$confirm('确认删除吗？','提示',{}).then(()=>{
          _this.editLoading=true;
          NProgress.start();
          _this.btnEditText='删除中';
          $.post("/api/account/detail/interviewee_list/delete",
            {
              data:row.num,
            },
            function(data,status){
              if (data['error_code'] == 0) {
                _this.$router.replace('/interviewee');
                _this.editLoading=false;
                NProgress.done();
                _this.btnEditText='提 交';
                _this.$notify({
                  title: '成功',
                  message: '删除成功',
                  type: 'success'
                });
                _this.editFormVisible = false;
              }
              else {
                _this.$notify({
                  title: '失败',
                  message: '删除失败',
                  type: 'fail'
                });
                return false;
              }              
            });
        }).catch(() => {
          
        });
			},
			handleInvite:function(row) {
				var _this = this;
				_this.$confirm('确认邀请吗？','提示',{}).then(()=>{
				  _this.editLoading=true;
				  NProgress.start();
				  _this.btnEditText='邀请中';
				  $.post("/api/account/detail/interviewee_list/send_mail",
				    {
				      userid:row.num,
				      roomid:row.roomnum
				    },
				    function(data,status){
				      if (data['error_code'] == 0) {
				        _this.$router.replace('/interviewee');
				        _this.editLoading=false;
				        NProgress.done();
				        _this.btnEditText='提 交';
				        _this.$notify({
				          title: '成功',
				          message: '邮件发送成功',
				          type: 'success'
				        });
				        _this.editFormVisible = false;
				      }
				      else {
				        _this.$notify({
				          title: '失败',
				          message: '邮件发送失败',
				          type: 'fail'
				        });
				        return false;
				      }              
				    });
				}).catch(() => {
				  
				});
			},

			//查看面试报告
			handleView:function(row){
				//TODO
			},
			//显示编辑界面
			handleEdit:function(row){
				this.editFormVisible = true;
				this.editFormTtile = '编辑';
				this.editForm.id = row.num;
				this.editForm.name = row.username;
				this.editForm.mail = row.email;
				this.editForm.phonenumber = row.telephone;
				this.editForm.addr = row.address;
				this.editForm.state = row.state;
				this.editForm.roomnum = row.roomnum;
			},
			//编辑 or 新增
			editSubmit:function(){
				var _this=this;
				console.log(this.editForm);
				_this.$refs.editForm.validate((valid)=>{
					if(valid){
						_this.$confirm('确认提交吗？','提示',{}).then(()=>{
							_this.editLoading=true;
							NProgress.start();
							_this.btnEditText='提交中';
              $.post("/api/account/detail/interviewee_list",
                {
                	num:_this.editForm.id,
                  username:_this.editForm.name,
                  email:_this.editForm.mail,
                  telephone:_this.editForm.phonenumber,
                  address:_this.editForm.addr,
                  state:_this.editForm.state,
                  roomnum:_this.editForm.roomnum,
                },
                function(data,status){
                  if (data['error_code'] == 0) {
                    _this.$router.replace('/interviewee');
                    _this.editLoading=false;
                    NProgress.done();
                    _this.btnEditText='提 交';
                    _this.$notify({
                      title: '成功',
                      message: '提交成功',
                      type: 'success'
                    });
                    _this.editFormVisible = false;
                  }
                  else {
                    _this.$notify({
                      title: '失败',
                      message: '提交失败',
                      type: 'fail'
                    });
                    return false;
                  }              
                });
						}).catch(() => {
              
            });												
					}
				});
			},
			//显示新增界面
			handleAdd:function(){
				var _this=this;

				this.editFormVisible=true;
				this.editFormTtile='新增';
				this.editForm.id=0;
				this.editForm.name='';
				this.editForm.mail='';
				this.editForm.phonenumber='';
				this.editForm.addr='';
				this.editForm.state='';
				this.editForm.roomnum='';
			}
    },
    mounted() {
      this.rooms = this.loadAll();
    }
  }
</script>

<style scoped>
	.toolbar .el-form-item {
		margin-bottom: 10px;
	}
	
	.toolbar {
		background: #fff;
		padding: 10px 10px 0px 10px;
	}
</style>