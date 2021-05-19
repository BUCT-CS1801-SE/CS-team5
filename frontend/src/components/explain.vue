<template>
  <div>
    <el-row class="header">
      <div class="header-text">讲解数据管理</div>
      <div class="header-btn">
        <el-button
            size="mini"
            type="primary"
            icon="el-icon-plus"
            @click="add"
        >
          添加
        </el-button>
      </div>
    </el-row>
    <el-table
        :data="newsdata.filter(
    data => !search
    || data.explanationID.toString().toLowerCase().includes(search)
    ||data.explanationName.toLowerCase().includes(search)
    ||data.explainerID.toString().toLowerCase().includes(search))
    .slice((currentpage)*pageSize,(currentpage+1)*pageSize)
    "
        stripe
        :default-sort="{prop:'explanationID',order:'ascending'}"
        class="table-style">

      <el-table-column
          type="index"
          label="序号"
          fixed
          width="80">
      </el-table-column>
      <el-table-column
          sortable
          label="讲解ID"
          prop="explanationID"
          width="150">
      </el-table-column>
      <el-table-column
          label="讲解名称"
          prop="explanationName"
          width="150">
      </el-table-column>
      <el-table-column
          label="讲解员ID"
          sortable
          prop="explainerID"
          width="150">
      </el-table-column>
      <el-table-column
          label="讲解时长"
          sortable
          prop="explanationTime"
          width="150">
      </el-table-column>

      <el-table-column
          label="讲解语言"
          prop="explanationLanguage"
          width="150"
      >
      </el-table-column>

      <el-table-column
          label="推荐游玩时长"
          prop="recommendedTime"
          width="150">
      </el-table-column>

      <el-table-column
          label="状态"
          prop="status"
          width="150">
      </el-table-column>

      <el-table-column
          align="right"
          width="200"
          fixed="right">
        <template slot="header">
          <input
              class="ipt-style"
              v-model="search"
              placeholder="输入关键字搜索"/>
          <!-- <el-button type="primary" size="mini" icon="el-icon-search">搜索</el-button> -->
        </template>
        <template slot-scope="scope">
          <el-button
              size="mini"
              type="success"
              icon="el-icon-edit"
              @click="handleEdit(scope.$index, scope.row)">Edit</el-button>
          <el-button
              size="mini"
              type="danger"
              icon="el-icon-delete"
              @click="handleDelete(scope.$index, scope.row)">Delete</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-pagination
        class="page-divide-style"
        layout="prev, pager, next"
        :total="newsdata.length+pageSize"
        :page-size="pageSize"
        @current-change="jumpTo">
    </el-pagination>

    <!-- 弹出层 -->
    <el-drawer
        modal
        title="编辑"
        :before-close="Close"
        :visible.sync="isvisible"
        direction="ltr"
        custom-class="drawer-style"
        size='50%'
        ref="drawer"
    >
      <div class="drawer-content-style">
        <el-form :model="formData"
                 label-position="left"
                 label-width="80px"
        >
          <el-form-item label="讲解名称">
            <el-input v-model="formData.explanationName"></el-input>
          </el-form-item>
          <el-form-item label="讲解员ID">
            <el-input v-model="formData.explainerID"></el-input>
          </el-form-item>
          <el-form-item label="讲解时长">
            <el-input
                v-model.number="formData.explanationTime">
            </el-input>
          </el-form-item>
          <el-form-item label="讲解语言">
            <el-input v-model="formData.explanationLanguage"></el-input>
          </el-form-item>
          <el-form-item label="推荐时长">
            <el-input
                v-model.number="formData.recommendedTime">
            </el-input>
          </el-form-item>
          <el-form-item label="状态">
            <el-input v-model.number="formData.status"></el-input>
          </el-form-item>
        </el-form>
        <div class="drawer-footer">
          <el-button
              type="danger"
              size="medium"
              @click="cancelForm">取 消</el-button>
          <el-button type="primary"
                     size="medium"
                     @click="handleClose" :loading="loading">{{ loading ? '提交中 ...' : '确 定' }}</el-button>
        </div>
      </div>
    </el-drawer>
  </div>
</template>

<script>
export default {
  name: "explain",
  data(){
    return{
      newsdata:[],
      search: '',
      isvisible:false,
      loading:false,
      formData:'',
      currentpage:0,
      pageSize:20
    }
  },
  methods:{
    handleEdit(index, row) {
      console.log(index, row);
      this.isvisible = true;
      this.formData = row;
    },
    handleDelete(index, row){
      console.log(index, row);
      var that = this;
      this.$confirm('确认删除此项?')
          .then(_=>{
            var explanationID = this.newsdata[index].explanationID;
            //发起请求,然后删除
            that.$axios({
              url:'/api/deleteExplainOneitem/',
              method:'get',
              params:{
                ID:explanationID
              }
            }).then(res=>{
              if(res.status == 200){
                if(res.data.status == 1){
                  that.$notify({
                    title:'删除成功！'
                  })
                  that.newsdata.splice(index,1);
                }else{
                  that.$notify({
                    title:'删除失败！'
                  })
                }
              }else{
                that.$notify({
                  title:'请检查网络是否连接！'
                })
              }
            })
          })
    },
    jumpTo(currentPage){
      console.log(currentPage);
      //发起请求获取分页数据
      if((currentPage-1)*this.pageSize>this.newsdata.length){
        this.currentpage = currentPage-1;
        this.getdatainfo();
      }
      else{
        this.currentpage = currentPage-1;
      }
    },
    splitchar(row, column, cellValue, index){
      var content = row.newsmaintext;
      return content.length>10?content.substring(0,9)+'...':content;
    },

    Close(){
      this.$confirm('确定要关闭么？').then(res=>{
        this.isvisible = false;
        this.loading = false;
        this.formData = {};
      })
    },
    handleClose(){
      var that  = this;
      var tempdata = this.formData;

      this.$confirm('确定要提交表单吗？')
          .then(_=>{
            this.loading = true;
            that.$axios({
              url:"/api/addinfoToexplain/",
              method:"post",
              data:tempdata,
              header:{
                'Content-Type':'application/json'  //如果写成contentType会报错
              }
            }).then(res=>{
              if(res.status == 200){
                this.$notify({
                  title:'添加成功'
                })
              }else{
                this.$notify({
                  title:'失败！',
                  type: 'error'
                })
              }
            })
          })
      this.isvisible = false;
      this.loading = false;
      this.formData = {};
    },
    cancelForm(){
      this.loading = false;
      this.isvisible = false;
    },
    add(){
      this.isvisible = true;
      this.loading = false;
      //增加新表单
      this.formData = {};
    },
    getdatainfo(){
      var that = this;
      that.$axios({
        url:"/api/getexplaindata/",
        method:"get",
        params:{
          page:that.currentpage,
          pageSize:that.pageSize
        }
      }).then(res=>{
        console.log(res)
        if(res.data.status){
          this.$notify({
            title:'暂无更多数据！'
          })
        }else if(res.status == 200){
          if(that.newsdata.length==0)
            that.newsdata = res.data;
          else
            that.newsdata = that.newsdata.concat(res.data);
        }
      })
    }
  },
  created(){//获取初始数据
    this.getdatainfo()
  }
}
</script>

<style scoped>
.table-style{
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  /* margin-top: 30px; */
  margin-right: 20px;
}
/* .ipt-style{
  width: 100px;
  margin-right: 5px;
} */
.page-divide-style{
  /* border: 1px solid red; */
  padding-left: 35%;
}
.header{
  display: flex;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  width: 100%;
}
.header .header-text{
  margin-top: 2%;
  margin-left: 5%;
  color: black;
  font-size: 22px;
  font-weight: 600;
}
.header-btn{
  margin-top: 2%;
  height: 30px;
  margin-left: 70%;
  /* border:1px solid red; */
}

.drawer-content-style{
  margin-left: 2%;

}
.drawer-footer{
  /* border: 1px solid red; */
  padding-left: 30%;
}


</style>