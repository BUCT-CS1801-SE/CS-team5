<template>
  <el-card class="box-card">
    <div slot="header" class="clearfix">
      <span>管理员管理</span>
      <span></span>
      <el-button style="float: right;" size="mini" @click="dialog = true">添加</el-button>
    </div>
    <div>
      <el-table
          :data="datalist.filter(data => !search || data.username.toLowerCase().includes(search.toLowerCase())).slice((currentPage-1)*pagesize,currentPage*pagesize)"
          stripe
          style="width: 100%">
        <el-table-column
            sortable
            prop="id"
            label="id"
            width="80">
        </el-table-column>
        <el-table-column
            sortable
            prop="username"
            label="用户名"
            width="100">
        </el-table-column>
        <el-table-column
            sortable
            prop="password"
            label="密码"
            width="350">
        </el-table-column>
        <el-table-column
            sortable
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
                @click="setForm(scope.row),dialogFormVisible = true">编辑</el-button>
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
          title="添加管理员"
          :before-close="handleClose"
          :visible.sync="dialog"
          direction="ltr"
          custom-class="demo-drawer"
          ref="drawer"
      >
        <div class="demo-drawer__content">
          <el-form :model="FormData" status-icon ref="FormData" :rules="rules">
            <el-form-item label="用户名" prop="username">
              <el-input type="text" v-model="FormData.username" placeholder="请输入用户名"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
              <el-input type="password" v-model="FormData.password" placeholder="请输入密码"></el-input>
            </el-form-item>
            <el-form-item label="再次输入密码" prop="repassword">
              <el-input type="password" v-model="FormData.repassword" placeholder="请再次输入密码"></el-input>
            </el-form-item>
            <el-form-item label="邮箱" prop="email">
              <el-input v-model="FormData.email" placeholder="请输入邮箱"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="submitd('FormData')">添加</el-button>
              <el-button @click="resetForm('FormData')">重置</el-button>
            </el-form-item>
          </el-form>
        </div>
      </el-drawer>
      <el-dialog title="编辑数据" :visible.sync="dialogFormVisible">
        <el-form :model="FormData">
          <el-form-item label="用户名" :label-width="formLabelWidth">
            <el-input v-model="FormData.username" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="密码" :label-width="formLabelWidth">
            <el-input v-model="FormData.password" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="email" :label-width="formLabelWidth">
            <el-input v-model="FormData.email" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="handleEdit()">确 定</el-button>
        </div>
      </el-dialog>
    </div>
  </el-card>
</template>

<script>
export default {
  name: "manage",
  data(){
    var checkPassword = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.FormData.password) {
        callback(new Error('两次输入的密码不一致.'))
      } else {
        callback()
      }
    }
    // 检测用户名是否已经被注册
    var dulaUsername = (rule, value, callback) => {
      // 验证用户名是否存在.  一会再写
      if (value.length < 3) {
        callback(new Error('你的用户名太短了！'))
      } else if (value.length > 18) {
        callback(new Error('你的用户名太长了！'))
      } else {
        this.$axios.post('/api/register?select=1', {
          select_username: value
        })
            .then(response => {
              if (response.data.is_indb === 1) {
                callback(new Error('该用户名已经被注册'))
              } else {
                callback();
              }
            })
      }
    }

    // 检测密码的长度
    var checkLen = (rule, value, callback) => {
      if (value.length < 6) {
        callback(new Error('密码长度不能小于6位'))
      } else if (value.length > 18) {
        callback(new Error('密码长度不能超过18位'))
      } else {
        callback()
      }
    }
    return{
      FormData:{
        id:'',
        username:'',
        password:'',
        repassword:'',
        email:''
      },
      rules: {
        username: [{required: true, message: '这是必填项', trigger: 'blur'}, {validator: dulaUsername, trigger: 'blur'}],
        password: [{required: true, message: "这是必填项", trigger: 'blur'}, {validator: checkLen, trigger: 'blur'}],
        repassword: [{required: true, message: '这是必填项', trigger: 'blur'}, {validator: checkPassword, trigger: 'blur'}],
        email: [{required: true, message: "请输入邮箱地址", trigger: 'blur'}, {type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change']}]
      },
      dialogFormVisible:false,
      formLabelWidth:'80px',
      dialog:false,
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
      this.$axios.get("/api/getinfo")
          .then(response=>{
            this.datalist = response.data.data
          })
    },
    setnullform(){
      this.FormData.id = '';
      this.FormData.username='';
      this.FormData.password='';
      this.FormData.repassword='';
      this.FormData.email='';
    },
    submitd: function (formdata) {
      this.$refs[formdata].validate((valid) => {
        if (valid) {
          // 成功.
          this.$axios.post('/api/register', {
            username: this.FormData.username,
            password: this.FormData.password,
            email: this.FormData.email
          })
              .then(response => {
                if (response.data.status === 0) {
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

        } else {
          return false;
        }
      });
    },
    resetForm: function (formdata) {
      this.$refs[formdata].resetFields()
    },
    handleClose(done) {
      this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
    },
    setForm(row){
      this.FormData.id = row.id;
      this.FormData.username=row.username;
      this.FormData.email=row.email;
    },
    handleEdit(){
      this.$axios.post('/api/m_change', {
        id:this.FormData.id,
        username: this.FormData.username,
        password: this.FormData.password,
        email: this.FormData.email
      }).then(response=>{
        console.log(response);
        this.dialogFormVisible = false;
      })
    },
    handleDelete(index,row){
      this.$confirm('是否删除该数据?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$axios.get('/api/m_d',{params:{data:row.id}})
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
  created() {
    this.updatedata();
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