<template>
	<el-row class="panel">
		<el-col :span="24" class="panel-top">
      <el-col :span="1"><span>&nbsp</i></span></el-col>
			<el-col :span="19" style="font-size:26px;">
				<span>New<i style="color:#20a0ff">View</i></span>
			</el-col>
      <el-col :span="2" v-link="{ path: '/home'}" style="font-size:20px;">
        <span>登录</span>
      </el-col>
      <el-col :span="2" style="font-size:20px;">
        <span>注册</span>
      </el-col>
    </el-col>
  <el-col :span="24" class="panel-center">
      <el-col :span="24">
         <img src="./assets/NewView.png" class="bg">
      </el-col>
  </el-col>

	</el-row>

</template>

<script>
  export default {
    data() {

    },
  }
</script>

<style scoped>
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
		background: #2F3D4D;
    position: absolute;
		color: #c0ccda;
	}

	.panel-center {
		background: #324057;
		position: absolute;
		top: 60px;
		bottom: 0px;
		overflow: hidden;
	}

  .bg {
    width: 100%;
    float: left;
  }

</style>