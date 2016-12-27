<template>
	<section>
		<!--列表-->
		<template>
			<el-table :data="tableData" highlight-current-row v-loading="listLoading" style="width: 100%;">
				<el-table-column type="index" width="50">
				</el-table-column>
				<el-table-column prop="name" label="房间名" width="180">
				</el-table-column>
				<el-table-column prop="intro" label="房间简介" width="180" :formatter="formatSex">
				</el-table-column>
				<el-table-column prop="personA" label="面试官" width="180">
				</el-table-column>
				<el-table-column prop="state" label="状态">
				</el-table-column>
				<el-table-column inline-template :context="_self" label="操作" width="200">
					<span>
					<el-button type="text" size="small" @click="handleInvite1(row)">邀请候选人</el-button>
					<el-button type="text" size="small" @click="handleInvite2(row)">邀请面试官</el-button>
					<el-button type="text" size="small" @click="handleEdit(row)">编辑</el-button>
					<el-button type="text" size="small" @click="handleDel(row)">关闭房间</el-button>
				</span>
				</el-table-column>
			</el-table>
		</template>

		<!--编辑界面-->
		<el-dialog :title="editFormTtile" v-model="editFormVisible" :close-on-click-modal="false">
			<el-form :model="editForm" label-width="80px" :rules="editFormRules" ref="editForm">
				<el-form-item label="房间名" prop="name">
					<el-input v-model="editForm.name" auto-complete="off"></el-input>
				</el-form-item>
				<el-form-item label="房间介绍" prop="intro">
					<el-input type="textarea" v-model="editForm.intro"></el-input>
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
  $.get("/api/account/detail/room_list",{},
          function(data,status){
            console.log(status)
            this.tableData = data['room_data'];
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
					name: '',
					intro: '',
					personA:'',
					state: ''
				},
				editLoading:false,
				btnEditText:'提 交',
				editFormRules:{
					name:[
						{ required: true, message: '请输入姓名', trigger: 'blur' }
					]
				},
				tableData: [
          {
  					id:1,
  					name: '计蒜客面试',
  					intro: '招收前端工程师',
  					personA: '无',	
  					state:'使用中'
  				}
        ],
				listLoading:false
     		}
    },
    methods: {
			//显示编辑界面
			handleEdit:function(row){
				this.editFormVisible=true;
				this.editFormTtile='编辑';
				this.editForm.id=row.id;
				this.editForm.name=row.name;
				this.editForm.intro=row.intro;
				this.editForm.personA=row.personA;
				this.editForm.personB=row.personB;
				this.editForm.state=row.state;
			},
			//邀请候选人
			handleInvite1:function(row){
        //TODO
			},
			//邀请面试官
			handleInvite2:function(row){
        //TODO
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
                  roomnum:_this.editForm.id,
                  title:_this.editForm.name,
                  description:_this.editForm.intro,
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
                    $.get("/api/account/detail/room_list",{},
                            function(data,status){
                              console.log(status)
                              this.tableData = data['room_data'];
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