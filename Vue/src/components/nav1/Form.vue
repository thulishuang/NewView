<template>
	<section>
		<!--列表-->
		<template>
			<el-table :data="tableData" highlight-current-row v-loading="listLoading" style="width: 100%;">
				<el-table-column prop="num" width="50" label="ID">
				</el-table-column>
				<el-table-column prop="title" label="房间名" width="180">
				</el-table-column>
				<el-table-column prop="description" label="房间简介" width="260" :formatter="formatSex">
				</el-table-column>
				<el-table-column prop="interviewer_name" label="面试官" width="100">
				</el-table-column>
				<el-table-column prop="state" label="状态" width="100">
				</el-table-column>
				<el-table-column inline-template :context="_self" label="操作" width="387">
					<span>
					<el-button type="text" size="small" @click="handleInviteInterviewer(row)">邀请面试官</el-button>
					<el-button type="text" size="small" @click="handleEdit(row)">编辑</el-button>
					<el-button type="text" size="small" @click="handleDel(row)">关闭房间</el-button>
          <el-button type="text" size="small" @click="handleOpen(row)">开启房间</el-button>
				</span>
				</el-table-column>
			</el-table>
		</template>

		<!--编辑界面-->
		<el-dialog :title="editFormTtile" v-model="editFormVisible" :close-on-click-modal="false">
			<el-form :model="editForm" label-width="90px" :rules="editFormRules" ref="editForm">
				<el-form-item label="房间名" prop="title">
					<el-input v-model="editForm.title" auto-complete="off"></el-input>
				</el-form-item>
				<el-form-item label="房间介绍" prop="description">
					<el-input type="textarea" v-model="editForm.description"></el-input>
				</el-form-item>
        <el-form-item label="面试官" prop="interviewer_name">
          <el-input type="textarea" v-model="editForm.interviewer_name"></el-input>
        </el-form-item>
        <el-form-item label="面试官邮箱" prop="interviewer_email">
          <el-input type="textarea" v-model="editForm.interviewer_email"></el-input>
        </el-form-item>
			</el-form>
			<div slot="footer" class="dialog-footer">
				<el-button @click.native="editFormVisible = false">取消</el-button>
				<el-button type="primary" @click.native="editSubmit" :loading="editLoading">{{btnEditText}}</el-button>
			</div>
		</el-dialog>
	</section>
</template>

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
					num:0,
					title: '',
					description: '',
          interviewer_name:'',
          interviewer_email:'',
					state: ''
				},
				editLoading:false,
				btnEditText:'提 交',
				editFormRules:{
					name:[
						{ required: true, message: '请输入姓名', trigger: 'blur' }
					]
				},
        tableData:[],
				listLoading:false
     		}
    },
    created: function(){
      var _this = this;
      $.get("/api/account/detail/room_list",{},
        function(data,status){
          _this.tableData = data['roomlist'];
          for(var i = 0; i < _this.tableData.length; i++){
            if (_this.tableData[i].state == false) {
              _this.tableData[i].state = '关闭';
            }
            else {
              _this.tableData[i].state = '开启';
            }
          }
      });
    },
    // ready: function(){
    //   var _this = this;
    //   $.get("/api/account/detail/room_list",{},
    //     function(data,status){
    //       _this.tableData = data['roomlist'];
    //       for(var i = 0; i < _this.tableData.length; i++){
    //         if (_this.tableData[i].state == false) {
    //           _this.tableData[i].state = '关闭';
    //         }
    //         else {
    //           _this.tableData[i].state = '开启';
    //         }
    //       }
    //   });
    // },
    methods: {
			//显示编辑界面
			handleEdit:function(row){
				this.editFormVisible=true;
				this.editFormTtile='编辑';
				this.editForm.num=row.num;
				this.editForm.title=row.title;
				this.editForm.description=row.description;
				this.editForm.interviewer_name=row.interviewer_name;
        this.editForm.interviewer_email=row.interviewer_email;
				this.editForm.state=row.state;
			},
			//邀请面试官
			handleInviteInterviewer:function(row){
        var _this = this;
        _this.$confirm('确认邀请吗？','提示',{}).then(()=>{
          _this.editLoading=true;
          NProgress.start();
          _this.btnEditText='邀请中';
          $.post("/api/account/detail/room_list/invite_interviewer",
            {
              email:row.interviewer_email,
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
      handleOpen:function(row) {
        var _this = this;
        _this.$confirm('确认开启吗？','提示',{}).then(()=>{
          _this.editLoading=true;
          NProgress.start();
          _this.btnEditText='开启中';
          $.post("/api/account/detail/room_list/open",
            {
              roomnum:row.num,
            },
            function(data,status){
              if (data['error_code'] == 0) {
                _this.$router.replace('/roomlist');
                _this.editLoading=false;
                NProgress.done();
                _this.btnEditText='提 交';
                _this.$notify({
                  title: '成功',
                  message: '开启成功',
                  type: 'success'
                });
                _this.editFormVisible = false;
              }
              else {
                _this.$notify({
                  title: '失败',
                  message: '开启失败',
                  type: 'fail'
                });
                return false;
              }              
            });
        }).catch(() => {
          
        });
      },
      handleDel:function(row) {
        var _this = this;
        _this.$confirm('确认关闭吗？','提示',{}).then(()=>{
          _this.editLoading=true;
          NProgress.start();
          _this.btnEditText='关闭中';
          $.post("/api/account/detail/room_list/close",
            {
              roomnum:row.num,
            },
            function(data,status){
              if (data['error_code'] == 0) {
                _this.$router.replace('/roomlist');
                _this.editLoading=false;
                NProgress.done();
                _this.btnEditText='提 交';
                _this.$notify({
                  title: '成功',
                  message: '关闭成功',
                  type: 'success'
                });
                _this.editFormVisible = false;
              }
              else {
                _this.$notify({
                  title: '失败',
                  message: '关闭失败',
                  type: 'fail'
                });
                return false;
              }              
            });
        }).catch(() => {
          
        });
      },
			//编辑 or 新增
			editSubmit:function(){
				var _this=this;
				_this.$refs.editForm.validate((valid)=>{
					if(valid){
						_this.$confirm('确认提交吗？','提示',{}).then(()=>{
							_this.editLoading=true;
							NProgress.start();
							_this.btnEditText='提交中';
              $.post("/api/account/detail/room_list",
                {
                  roomnum:_this.editForm.num,
                  title:_this.editForm.title,
                  description:_this.editForm.description,
                },
                function(data,status){
                  if (data['error_code'] == 0) {
                    _this.$router.replace('/roomlist');
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

			}
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