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
				<el-table-column prop="addr" label="地址" width="250">
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
			</el-form>
			<div slot="footer" class="dialog-footer">
				<el-button @click.native="editFormVisible = false">取消</el-button>
				<el-button type="primary" @click.native="editSubmit" :loading="editLoading">{{btnEditText}}</el-button>
			</div>
		</el-dialog>
	</section>
</template>

<script>

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
					setTimeout(function(){
						for(var i=0;i<_this.tableData.length;i++){
							if(_this.tableData[i].id==row.id){
								_this.tableData.splice(i,1);

								_this.listLoading=false;
								NProgress.done();
								_this.$notify({
									title: '成功',
									message: '删除成功',
									type: 'success'
								});

								break;
							}
						}
					},1000);
				}).catch(() => {
							
				});
			},
			//查看面试报告
			handleView:function(){
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
							setTimeout(function(){
								_this.editLoading=false;
								NProgress.done();
								_this.btnEditText='提 交';
								_this.$notify({
									title: '成功',
									message: '提交成功',
									type: 'success'
								});
								_this.editFormVisible = false;

								if(_this.editForm.id==0){
									//新增
									_this.tableData.push({
										id:new Date().getTime(),
										name: _this.editForm.name,
										mail: _this.editForm.mail,
										phonenumber: _this.editForm.phonenumber,
										addr: _this.editForm.addr,
										state: _this.editForm.state
									});
								}else{
									//编辑
									for(var i=0;i<_this.tableData.length;i++){
										if(_this.tableData[i].id==_this.editForm.id){
											_this.tableData[i].name=_this.editForm.name;
											_this.tableData[i].mail=_this.editForm.mail;
											_this.tableData[i].phonenumber=_this.editForm.phonenumber;
											_this.tableData[i].addr=_this.editForm.addr;
											_this.tableData[i].state=_this.editForm.state;
											break;
										}
									}
								}
							},1000);
						
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