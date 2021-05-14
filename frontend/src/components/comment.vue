<template>
<div>
  <el-row class="header">
    <div class="header-text">评论数据管理</div>
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
    || data.commentID.toString().toLowerCase().includes(search)
    ||data.comment.toLowerCase().includes(search))
    .slice((currentpage)*pageSize,(currentpage+1)*pageSize)
    "
    stripe
    :default-sort="{prop:'commentID',order:'ascending'}"
    class="table-style">
      
      <el-table-column
        type="index"
        label="序号"
        fixed
        width="80">
      </el-table-column>
      <el-table-column
        sortable
        label="评论ID"
        prop="commentID"
        width="150">
      </el-table-column>
      <el-table-column
        sortable
        label="用户ID"
        prop="userID"
        width="150">
      </el-table-column>
      <el-table-column
        sortable
        label="博物馆ID"
        prop="museumID"
        width="150">
      </el-table-column>
      <el-table-column
        label="评论"
        prop="comment"
        width="150">
      </el-table-column>
      <el-table-column
        label="感情分析数组-环境"
        sortable
        prop="sentiAnalysis_environment"
        width="180">
      </el-table-column>

      <el-table-column
        label="感情分析数组-展览"
        sortable
        prop="sentiAnalysis_exhibit"
        width="180"
        >
      </el-table-column>

      <el-table-column
        label="感情分析数组-服务"
        sortable
        prop="sentiAnalysis_service"
        width="180">
      </el-table-column>
      <el-table-column
        label="评论时间"
        sortable
        prop="commentdata"
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
          <el-input
            class="ipt-style"
            v-model="search"
            size="mini"
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
    :total="50"
    @current-change="jumpTo">
  </el-pagination>

  <!-- 弹出层 -->
  <el-drawer
  modal
  title="编辑"
  :before-close="handleClose"
  :visible.sync="isvisible"
  direction="ltr"
  custom-class="drawer-style"
  size='50%'
  ref="drawer"
  >
  <div class="drawer-content-style">
  <el-scrollbar style="height:70%">
    <el-form 
      :model="formData"
      label-position="left"
      label-width="80px"
    >
      <el-form-item label="用户ID">
        <el-input v-model="formData.userID"></el-input>
      </el-form-item>
      <el-form-item label="评论时间">
        <el-date-picker 
          type="date" 
          value-format="yyyy-MM-dd"  
          v-model="formData.commentdata" 
          style="width: 80%;">
        </el-date-picker>
      </el-form-item>
      <el-form-item label="评论">
        <el-input
          type="textarea"
          rows="3"
          v-model="formData.comment">
        </el-input>
      </el-form-item>

      <el-form-item label="博物馆ID">
        <el-input v-model="formData.museumID"></el-input>
      </el-form-item>
      <el-form-item label="感情分析数组-环境">
        <el-input v-model.number="formData.sentiAnalysis_environment"></el-input>
      </el-form-item>
      <el-form-item label="感情分析数组-展览">
        <el-input v-model.number="formData.sentiAnalysis_exhibit"></el-input>
      </el-form-item>
       <el-form-item label="感情分析数组-服务">
        <el-input v-model.number="formData.sentiAnalysis_service"></el-input>
       </el-form-item>
      <el-form-item label="状态">
        <el-input v-model.number="formData.status"></el-input>
      </el-form-item>
    </el-form>
  </el-scrollbar>
    <div class="drawer-footer">
      <el-button 
      type="danger"
      size="medium"
      @click="cancelForm">取 消</el-button>
      <el-button type="primary" 
      size="medium"
      @click="$refs.drawer.closeDrawer()" :loading="loading">{{ loading ? '提交中 ...' : '确 定' }}</el-button>
    </div>
  </div>
  </el-drawer>
</div>
</template>

<script>
export default {
  name: "news",
  data(){
    return{
      newsdata:[],
      search: '',
      isvisible:false,
      loading:false,
      formData:'',
      currentpage:0,
      pageSize:7
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
          var commentID = this.newsdata[index].commentID;
          //发起请求,然后删除
          that.$axios({
            url:'/api/deleteCommentOneitem/',
            method:'get',
            params:{
              ID:commentID
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
      if(currentPage*this.pageSize<=this.newsdata.length)
        this.currentpage = currentPage-1;
      else{
        //请求数据

        //改变当前页
        this.currentpage = currentPage-1;
        this.getdatainfo();
      }
    },
    splitchar(row, column, cellValue, index){
      var content = row.newsmaintext;
      return content.length>10?content.substring(0,9)+'...':content;
    },
    handleClose(done){
      var that  = this;
      var tempdata = this.formData;
       this.$confirm('确定要提交表单吗？')
       .then(_=>{
          this.loading = true;
          //提交表单
          that.$axios({
            url:"/api/addinfoTocomment/",
            method:"post",
            data:tempdata,
            header:{
                'Content-Type':'application/json'  //如果写成contentType会报错
             }
          }).then(res=>{
            if(res.status == 200){
              this.$notify({
                title:'成功!'
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
      //增加新表单
      this.formData = {};
      this.loading = false;
    },
    getdatainfo(){
    var that = this;
    that.$axios({
            url:"/api/getcommentdata/",
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
  height: 60px;
  margin-top: 30px;
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
  height: 115%;
}
.drawer-footer{
  /* border: 1px solid red; */
  padding-left: 30%;
  /* height: 20%; */
}
.el-scrollbar__wrap {
        overflow: scroll; 
        width: 110%;
        height: 100%;  
}
</style>