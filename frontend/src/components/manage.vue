<template>
  <el-card class="box-card">
    <div slot="header" class="clearfix">
      <span>欢迎！</span>
    </div>
    <div>
      <h1>管理</h1>
    </div>
  </el-card>
</template>

<script>
export default {
  name: "manage"
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