<template>
  <el-card class="box-card">
    <div slot="header" class="clearfix">
      <span>用户信息管理</span>
      <span></span>
      <el-button style="float: right;" size="mini" @click="dialog = true">添加</el-button>
    </div>
    <div>
      <el-table
          :data="datalist.filter(data => !search || data.username.toLowerCase().includes(search.toLowerCase())).slice((currentPage-1)*pagesize,currentPage*pagesize)"
          stripe
          :default-sort = "{prop: 'userID', order: 'ascending'}"
          style="width: 100%">
        <el-table-column
            sortable
            width="80px"
            fixed="left"
            prop="userID"
            label="id">
        </el-table-column>
        <el-table-column
            sortable
            width="150px"
            fixed="left"
            prop="username"
            label="用户名">
        </el-table-column>
        <el-table-column
            sortable
            width="150px"
            prop="nickname"
            label="昵称">
        </el-table-column>
        <el-table-column
            sortable
            width="150px"
            prop="telephone"
            label="电话">
        </el-table-column>
        <el-table-column
            sortable
            width="150px"
            prop="idcard"
            label="身份证号">
        </el-table-column>
        <el-table-column
            sortable
            width="150px"
            prop="password"
            label="密码">
        </el-table-column>
        <el-table-column
            sortable
            width="150px"
            prop="userRole"
            label="用户组">
        </el-table-column>
        <el-table-column
            sortable
            width="200px"
            prop="userCreateDate"
            label="用户创建时间">
        </el-table-column>
        <el-table-column align="right" fixed="right" width="150px">
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
                @click="setForm(scope.row),dialog1 = true">编辑</el-button>
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
          :page-size="pagesize"
          @current-change="current_change"
          :total="datalist.length">
      </el-pagination>
      <el-drawer
          size="40%"
          title="请进行操作"
          :before-close="handleClose"
          :visible.sync="dialog"
          direction="ltr"
          custom-class="demo-drawer"
          ref="drawer"
      >
        <div class="demo-drawer__content">
          <el-form :model="FormData">
            <el-form-item label="用户名" :label-width="formLabelWidth">
              <el-input v-model="FormData.username" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="昵称" :label-width="formLabelWidth">
              <el-input v-model="FormData.nickname" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="电话" :label-width="formLabelWidth">
              <el-input v-model="FormData.telephone" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="身份证号" :label-width="formLabelWidth">
              <el-input v-model="FormData.idcard" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="密码" :label-width="formLabelWidth">
              <el-input v-model="FormData.password" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="用户组" :label-width="formLabelWidth">
              <el-input v-model="FormData.userRole" autocomplete="off"></el-input>
            </el-form-item>
          </el-form>
          <div class="demo-drawer__footer">
            <el-button @click="resetForm('FormData')">重置</el-button>
            <el-button type="primary" @click="mysubmit()" :loading="loading">{{ loading ? '提交中 ...' : '确 定' }}</el-button>
          </div>
        </div>
      </el-drawer>
      <el-drawer
          size="40%"
          title="请进行操作"
          :before-close="handleClose"
          :visible.sync="dialog1"
          direction="ltr"
          custom-class="demo-drawer"
          ref="drawer"
      >
        <div class="demo-drawer__content">
          <el-form :model="FormData">
            <el-form-item label="用户名" :label-width="formLabelWidth">
              <el-input v-model="FormData.username" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="昵称" :label-width="formLabelWidth">
              <el-input v-model="FormData.nickname" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="电话" :label-width="formLabelWidth">
              <el-input v-model="FormData.telephone" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="身份证号" :label-width="formLabelWidth">
              <el-input v-model="FormData.idcard" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="密码" :label-width="formLabelWidth">
              <el-input v-model="FormData.password" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="用户组" :label-width="formLabelWidth">
              <el-input v-model="FormData.userRole" autocomplete="off"></el-input>
            </el-form-item>
          </el-form>
          <div class="demo-drawer__footer">
            <el-button @click="resetForm('FormData')">重置</el-button>
            <el-button type="primary" @click="handleEdit()" :loading="loading">{{ loading ? '提交中 ...' : '确 定' }}</el-button>
          </div>
        </div>
      </el-drawer>
    </div>
  </el-card>
</template>

<script>
export default {
  name: "userinfo",
  data(){
    return{
      loading:false,
      FormData:{
        userID:'',
        username:'',
        nickname:'',
        telephone:'',
        idcard:'',
        password:'',
        userRole:'',
        userCreateDate:''
      },
      dialogFormVisible:false,
      formLabelWidth:'80px',
      dialog:false,
      dialog1: false,
      total:1000,
      pagesize:7,
      currentPage:1,
      datalist : [

      ],
      search:''

    };
  },
  methods:{
    updatedata(){
      this.$axios.get("/api/getuserinfo")
          .then(response=>{
            this.datalist = response.data.data
          })
    },
    setnullform(){
      this.FormData.userID='';
      this.FormData.username='';
      this.FormData.nickname='';
      this.FormData.telephone='';
      this.FormData.idcard='';
      this.FormData.password='';
      this.FormData.userRole='';
      this.FormData.userCreateDate='';
    },
    mysubmit(){
      this.loading=true;
      this.$axios.post('/api/useradd', {
        username:this.FormData.username,
        nickname:this.FormData.nickname,
        telephone:this.FormData.telephone,
        idcard:this.FormData.idcard,
        password:this.FormData.password,
        userRole:this.FormData.userRole,
      })
          .then(response => {
            console.log(response)
            if (response.data.status === 0) {
              this.loading=false;
              this.dialog=false;
              this.setnullform();
              this.updatedata();
              this.$notify({
                title: '添加成功',
                message: '成功添加该项数据',
                type: 'success'
              });
            } else {
              return false
            }
          })
    },
    resetForm: function (formdata) {
      this.setnullform();
    },
    handleClose(done) {
      this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
    },
    setForm(row){
      this.FormData.userID = row.userID;
      this.FormData.username= row.username;
      this.FormData.nickname= row.nickname;
      this.FormData.telephone= row.telephone;
      this.FormData.idcard= row.idcard;
      this.FormData.password= row.password;
      this.FormData.userRole= row.userRole;
    },
    handleEdit(){
      this.loading=true;
      this.$axios.post('/api/u_change', {
        userID: this.FormData.userID,
        username:this.FormData.username,
        nickname:this.FormData.nickname,
        telephone:this.FormData.telephone,
        idcard:this.FormData.idcard,
        password:this.FormData.password,
        userRole:this.FormData.userRole,
      }).then(response=>{
        if (response.data.status === 0) {
          this.loading=false;
          this.dialog1=false;
          this.setnullform();
          this.updatedata();
          this.$notify({
            title: '编辑成功',
            message: '成功编辑该项数据',
            type: 'success'
          });
        } else {
          return false
        }
      })
    },
    handleDelete(index,row){
      this.$confirm('是否删除该数据?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$axios.get('/api/u_d',{params:{data:row.userID}})
            .then(response=>{
              console.log(response)
              this.updatedata()
              this.$notify({
                title: '删除成功',
                message: '成功删除该项数据',
                type: 'success'
              });
            })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        });
      });

    },
    current_change:function(currentPage){
      this.currentPage = currentPage;
    }
  },
  created(){
    this.updatedata();
  },
}
</script>

<style scoped>
.demo-drawer__content{
  padding-right: 5%;
}
.demo-drawer__footer{
  padding-left: 40%;
}
.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both
}
</style>