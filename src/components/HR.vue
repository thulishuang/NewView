<template>
	<el-row class="panel">
		<el-col :span="24" class="panel-top">
      		<el-col :span="1"><span>&nbsp</i></span></el-col>
			<el-col :span="20" style="font-size:26px;">
				<span>New<i style="color:#20a0ff">View</i></span>
			</el-col>
      		<el-col :span="1"  style="font-size:20px;">
       			<span>首页</span>
      		</el-col>
      		<el-col :span="1" style="font-size:20px;">
        		<span>登出</span>
     		  </el-col>
          <el-col :span="1" style="font-size:20px;">
            <span style="color:#FFD700">HR</span>
          </el-col>
    	</el-col>
		<el-col :span="24" class="panel-center">
			<!--<el-col :span="4">-->
			<aside style="width:230px;">
        <el-menu default-active="2" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" theme="dark" >
          <el-menu-item index="1" style="font-size:20px;">房间</el-menu-item>
          <el-menu-item index="2" style="font-size:20px;">候选人</el-menu-item>
          <el-menu-item index="3" style="font-size:20px;">服务</el-menu-item>
        </el-menu>
				<!--<el-menu style="border-top: 1px solid #475669;" default-active="/table" class="el-menu-vertical-demo" @open="handleopen"
					@close="handleclose" @select="handleselect" theme="dark" unique-opened router>
					<el-submenu index="1">
						<template slot="title"><i class="el-icon-message"></i>导航一</template>
						<el-menu-item index="/table">Table</el-menu-item>
						<el-menu-item index="/form">Form</el-menu-item>
						<el-menu-item index="/page3">页面3</el-menu-item>
					</el-submenu>
					<el-submenu index="2">
						<template slot="title"><i class="fa fa-id-card-o"></i>导航二</template>
						<el-menu-item index="/page4">选项4</el-menu-item>
						<el-menu-item index="/page5">选项5</el-menu-item>
					</el-submenu>
					<el-menu-item index="/page6"><i class="fa fa-line-chart"></i>导航三</el-menu-item>
				</el-menu>-->
	<!--			<el-menu style="border-top: 1px solid #475669;" default-active="/table" class="el-menu-vertical-demo" @open="handleopen"
					@close="handleclose" @select="handleselect" theme="dark" unique-opened router>
					<template v-for="(item,index) in $router.options.routes" v-if="!item.hidden">
						<el-submenu :index="index+''" v-if="!item.leaf">
							<template slot="title"><i :class="item.iconCls"></i>{{item.name}}</template>
							<el-menu-item v-for="child in item.children" :index="child.path">{{child.name}}</el-menu-item>
						</el-submenu>
						<el-menu-item v-if="item.leaf&&item.children.length>0" :index="item.children[0].path"><i :class="item.iconCls"></i>{{item.children[0].name}}</el-menu-item>
					</template>
				</el-menu>
  -->
			</aside>
			<!--</el-col>-->
			<!--<el-col :span="20" class="panel-c-c">-->
			<el-col :span="24" class="panel-c-c">
      </el-col>
			<!--</el-col>-->
		</el-col>
	</el-row>
</template>

<script>
  export default {
    data() {
      return {
		 
      }
    },
	watch: {
		
	},
    methods: {
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
    left:0px;
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