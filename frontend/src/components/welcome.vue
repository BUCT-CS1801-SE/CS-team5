<template>
  <el-card class="box-card">
    <div slot="header" class="clearfix">
      <span>欢迎！</span>
    </div>
    <div>
      <h1>欢迎来到后台管理系统</h1>
    </div>
  </el-card>
</template>

<script>
export default {
  name: "welcome"
}
</script>

<style scoped>

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both
}
</style>