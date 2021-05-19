<template>
  <el-card class="box-card">
    <div slot="header" class="clearfix">
      <span>数据库备份与恢复</span>
      <span></span>
    </div>
    <div>
      <el-collapse>
        <el-collapse-item title="备份 Backup" name="1">
          <el-card class="box-card">
            <span>这将会备份当前整个数据库数据，并将覆盖当前备份！</span><br>
            <el-button style="width: 20%" type="primary" @click="backup">备份</el-button>
          </el-card>
        </el-collapse-item>
        <el-collapse-item title="恢复 Recovery" name="2">
          <el-card class="box-card">
            <span style="color: #F56C6C">这将会恢复数据库数据至最近保存备份！</span><br>
            <el-button style="width: 20%" type="warning" @click="recovery">恢复</el-button>
          </el-card>
        </el-collapse-item>
      </el-collapse>
    </div>
  </el-card>
</template>

<script>
export default {
  name: "db",
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
    backup(){
      this.$axios.post('/api/backup',{
        flag:1
      }).then(response=>{
        if(response.data.status === 0){
          this.$notify({
            title: '成功',
            message: '备份成功',
            type: 'success'
          });
        }
        else{
          this.$notify.error({
            title: '错误',
            message: '备份失败'
          });
        }
      })
    },
    recovery(){
      this.$axios.post('/api/recovery',{
        flag:1
      }).then(response=>{
        if(response.data.status === 0){
          this.$notify({
            title: '成功',
            message: '恢复成功',
            type: 'success'
          });
        }
        else{
          this.$notify.error({
            title: '错误',
            message: '恢复失败'
          });
        }
      })
    }
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