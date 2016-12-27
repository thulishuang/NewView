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
				<el-table-column type="index" width="50">
				</el-table-column>
				<el-table-column prop="name" label="姓名" width="180">
				</el-table-column>
				<el-table-column prop="mail" label="邮箱" width="180" :formatter="formatSex">
				</el-table-column>
				<el-table-column prop="phonenumber" label="手机号码" width="180">
				</el-table-column>
				<el-table-column prop="addr" label="地址" width="200">
				</el-table-column>
				<el-table-column prop="room" label="房间号" width="100">
				</el-table-column>
				<el-table-column prop="state" label="状态">
				</el-table-column>
				<el-table-column inline-template :context="_self" label="操作" width="200">
					<span>
					<el-button type="text" size="small" @click="handleEdit(row)">编辑</el-button>
					<el-button type="text" size="small" @click="handleDel(row)">删除</el-button>
					<el-button type="text" size="small" @click="handleView(row)">查看面试报告</el-button>
				</span>
				</el-table-column>
			</el-table>
		</template>

		<!--编辑界面-->
		<el-dialog :title="editFormTtile" v-model="editFormVisible" :close-on-click-modal="false">
			<el-form :model="editForm" label-width="80px" :rules="editFormRules" ref="editForm">
				<el-form-item label="姓名" prop="name">
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
				<el-form-item label="房间号">
					<el-input type="textarea" v-model="editForm.room"></el-input>
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
	$.get("/api/account/detail/interviewee_list",{},
	        function(data,status){
	          console.log(status)
	          this.tableData = data['interviewee_list'];
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
					id:0,
					room:'',
					name: '',
					mail: '',
					phonenumber:'',
					addr: '',
					state: ''
				},
				editLoading:false,
				btnEditText:'提 交',
				editFormRules:{
					name:[
						{ required: true, message: '请输入姓名', trigger: 'blur' }
					]
				},
				tableData: [{
					id:1000,
					name: 'ayashinta',
					mail: 'ayashinta@gmail.com',
					phonenumber: '184********',
					addr:'北京清华大学',
					room:'sss',
					state:'未邀请'
				}, {
					id:1001,
					name: 'ayashinta',
					mail: 'ayashinta@gmail.com',
					phonenumber: '184********',
					addr:'北京清华大学',
					state:'未邀请'
				}, {
					id:1002,
					name: 'ayashinta',
					mail: 'ayashinta@gmail.com',
					phonenumber: '184********',
					addr:'北京清华大学',
					state:'未邀请'
				}, {
					id:1003,
					name: 'ayashinta',
					mail: 'ayashinta@gmail.com',
					phonenumber: '184********',
					addr:'北京清华大学',
					state:'未邀请'
				}, {
					id:1004,
					name: 'ayashinta',
					mail: 'ayashinta@gmail.com',
					phonenumber: '184********',
					addr:'北京清华大学',
					state:'未邀请'
				}, {
					id:1005,
					name: 'ayashinta',
					mail: 'ayashinta@gmail.com',
					phonenumber: '184********',
					addr:'北京清华大学',
					state:'未邀请'
				}, {
					id:1006,
					name: 'ayashinta',
					mail: 'ayashinta@gmail.com',
					phonenumber: '184********',
					addr:'北京清华大学',
					state:'未邀请'
				}, {
					id:1007,
					name: 'ayashinta',
					mail: 'ayashinta@gmail.com',
					phonenumber: '184********',
					addr:'北京清华大学',
					state:'未邀请'
				}],
				listLoading:false
     		}
    },
    methods: {
			//删除记录
			handleDel:function(row){
				//console.log(row);
				var _this=this;
				this.$confirm('确认删除该记录吗?', '提示', {
					//type: 'warning'
				}).then(() => {
					_this.listLoading=true;
					NProgress.start();
					$.post("/api/account/detail/interviewee_list",
					  {
					    data:row.id,
					  },
					  function(data,status){
					    if (data['error_code'] == 0) {
					      _this.$router.replace('/interviewee');
					      _this.editLoading=false;
					      NProgress.done();
					      _this.btnEditText='删 除';
					      _this.$notify({
					        title: '成功',
					        message: '删除成功',
					        type: 'success'
					      });
					      _this.editFormVisible = false;
					      $.get("/api/account/detail/interviewee_list",{},
					              function(data,status){
					                console.log(status)
					                this.tableData = data['interviewee_list'];
					              }); 
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

			//查看面试报告
			handleView:function(){
				//TODO
			},
			//显示编辑界面
			handleEdit:function(row){
				this.editFormVisible=true;
				this.editFormTtile='编辑';
				this.editForm.id=row.id;
				this.editForm.name=row.name;
				this.editForm.mail=row.mail;
				this.editForm.phonenumber=row.phonenumber;
				this.editForm.addr=row.addr;
				this.editForm.state=row.state;
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
							$.post("/api/account/detail/interviewee_list",
							  {
							    num:_this.editForm.id,
							    username:_this.editForm.name,
							    email:_this.editForm.mail,
							    telephone:_this.editForm.phonenumber,
							    address:_this.editForm.addr,
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
							      $.get("/api/account/detail/interviewee_list",{},
							              function(data,status){
							                console.log(status)
							                this.tableData = data['interviewee_list'];
							              }); 
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
						});
					}
				});

			},
			//显示新增界面
			handleAdd:function(){
				var _this=this;

				_this.editFormVisible=true;
				_this.editFormTtile='新增';
				_this.editForm.room='';
				_this.editForm.id=0;
				_this.editForm.name='';
				_this.editForm.mail='';
				_this.editForm.phonenumber='';
				_this.editForm.addr='';
				_this.editForm.state='';
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