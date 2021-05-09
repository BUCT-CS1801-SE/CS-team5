<template>
  <el-card class="box-card">
    <div slot="header" class="clearfix">
      <span>管理员管理</span>
      <span></span>
      <el-button style="float: right;" size="mini" >添加</el-button>
    </div>
    <div>
      <el-table
          :data="datalist.filter(data => !search || data.username.toLowerCase().includes(search.toLowerCase())).slice((currentPage-1)*pagesize,currentPage*pagesize)"
          stripe
          style="width: 100%">
        <el-table-column
            prop="id"
            label="id"
            width="80">
        </el-table-column>
        <el-table-column
            prop="username"
            label="用户名"
            width="100">
        </el-table-column>
        <el-table-column
            prop="password"
            label="密码"
            width="350">
        </el-table-column>
        <el-table-column
            prop="email"
            label="邮箱">
        </el-table-column>
        <el-table-column align="right">
            <template slot="header" slot-scope="scope">
              <el-input
                  v-model="search"
                  size="mini"
                  placeholder="输入用户名搜索"/>
            </template>
          <template slot-scope="scope">
            <el-button
                size="mini"
                type="primary"
                @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
            <el-button
                size="mini"
                type="danger"
                @click="handleDelete(scope.$index, scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-pagination
          style="text-align: center"
          layout="prev, pager, next"
          @current-change="current_change"
          :total="datalist.length">
      </el-pagination>
    </div>
  </el-card>
</template>

<script>
export default {
  name: "manage",
  data(){
    return{
      total:1000,
      pagesize:7,
      currentPage:1,
      datalist : [

      ],
      search:''
    };
  },
  methods:{
    handleEdit(index,row){
      console.log(index,row)
    },
    handleDelete(index,row){
      console.log(index,row)
    },
    current_change:function(currentPage){
      this.currentPage = currentPage;
    }
  },
  created() {
    this.$axios.get("/api/getinfo")
    .then(response=>{
      this.datalist = response.data.data
    })
  }
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