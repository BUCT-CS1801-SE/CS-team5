<template>
  <el-row type="flex" justify="space-around" class="tac">
    <el-col :span="5">
      <el-menu
          default-active="2"
          class="el-menu-vertical-demo"
          @open="handleOpen"
          @close="handleClose">
        <el-submenu index="1">
          <template slot="title">
            <i class="el-icon-user"></i>
            <span>用户管理</span>
          </template>
          <el-menu-item index="1-1" @click="goTo('/userinfo')">用户信息管理</el-menu-item>
          <el-menu-item index="1-2" @click="goTo('/manage')">管理员管理</el-menu-item>
        </el-submenu>
        <el-submenu index="2">
          <template slot="title">
            <i class="el-icon-time"></i>
            <span slot="title">讲解审核</span>
          </template>
          <el-menu-item index="2-1" @click="goTo('/not_viewed')">未审核</el-menu-item>
          <el-menu-item index="2-2" @click="goTo('/viewed')">已审核</el-menu-item>
        </el-submenu>
        <el-submenu index="3">
          <template slot="title">
            <i class="el-icon-collection"></i>
            <span slot="title">数据管理</span>
          </template>
          <el-menu-item index="3-1" @click="goTo('/museum')">博物馆</el-menu-item>
          <el-menu-item index="3-2" @click="goTo('/exhibition')">展览</el-menu-item>
          <el-menu-item index="3-3" @click="goTo('/collection')">藏品</el-menu-item>
          <el-menu-item index="3-4" @click="goTo('/news')">新闻</el-menu-item>
          <el-menu-item index="3-5" @click="goTo('/explain')">讲解</el-menu-item>
          <el-menu-item index="3-6" @click="goTo('/comment')">评论</el-menu-item>
        </el-submenu>
        <el-submenu index="4" >
          <template slot="title">
            <i class="el-icon-setting"></i>
            <span slot="title">数据备份与恢复</span>
          </template>
          <el-menu-item index="4-1" @click="goTo('/server')">服务器端文件恢复</el-menu-item>
          <el-menu-item index="4-2" @click="goTo('/db')">数据库文件恢复</el-menu-item>
        </el-submenu>
        <el-menu-item index="5" @click="dialogVisible = true">
          <template slot="title">
            <i class="el-icon-switch-button"></i>
            <span slot="title">登出</span>
          </template>
        </el-menu-item>
      </el-menu>
    </el-col>
    <el-col :span="18">
      <transition name="fade">
        <router-view></router-view>
      </transition>
    </el-col>
    <el-dialog
        title="提示"
        :visible.sync="dialogVisible"
        width="30%"
        :before-close="handleClose1">
      <span>确定登出？</span>
      <span slot="footer" class="dialog-footer">
    <el-button @click="dialogVisible = false">取 消</el-button>
    <el-button type="primary" @click="logout">确 定</el-button>
  </span>
    </el-dialog>
  </el-row>

</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      dialogVisible: false
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    goTo(path){
      this.$router.replace("/home"+path)
    },
    logout(){
      this.dialogVisible=false;
      this.$axios.get("/api/logout")
          .then(response => {
            this.$router.replace("/")
          })
    },
    handleClose1(done) {
      this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
    }
  },
  created:{

  }
}

</script>

<style scoped>
.fade-enter{
  visibility: hidden;
  opacity: 0;
}
.fade-leave-to{
  display: none;
}
.fade-enter-active,
.fade-leave-active{
  transition: opacity .2s ease;
}
.fade-enter-to,
.fade-leave{
  visibility: visible;
  opacity: 1;
}
</style>