<template>
  <div>
    <el-row class="header">
      <div class="header-text">服务器文件恢复</div>
      <div class="header-btn">
        <el-button
            size="mini"
            type="primary"
            icon="el-icon-plus"
            @click="add"
        >
          备份
        </el-button>
      </div>
    </el-row>
    <el-table
        :data="newsdata.filter(
    data => !search
    ||data.serverID.toString().toLowerCase().includes(search)
    )
    .slice((currentpage)*pageSize,(currentpage+1)*pageSize)
    "
        stripe
        :default-sort="{prop:'serverID',order:'ascending'}"
        class="table-style">

      <el-table-column
          type="index"
          label="序号"
          fixed
          width="200"
      >
      </el-table-column>
      <el-table-column
          sortable
          label="备份ID"
          prop="serverID"
          width="200"
      >
      </el-table-column>
      <el-table-column
          sortable
          label="备份时间"
          prop="serverData"
          width="200"
      >
      </el-table-column>
      <el-table-column
          align="right"
          fixed="right"
          width="200"
      >
        <template slot="header">
          <input
              v-model="search"
              size="mini"
              placeholder="输入关键字搜索"/>
        </template>
        <template slot-scope="scope">
          <el-button
              size="mini"
              type="success"
              icon="el-icon-edit"
              @click="handleApply(scope.$index, scope.row)">Apply</el-button>
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
  </div>
</template>

<script>
export default {
  name: "server",
  data(){
    return{
      newsdata:[],
      search:'',
      currentpage:0,
      pageSize:20
    }
  },
  methods:{
    jumpTo(currentPage){
      // console.log(currentPage);
      //发起请求获取分页数据
      if((currentPage-1)*this.pageSize>this.newsdata.length){
        this.currentpage = currentPage-1;
        this.getdatainfo();
      }
      else{
        //改变当前页
        this.currentpage = currentPage-1;
      }
    },
    getdatainfo(){
      var that = this;
      that.$axios({
        url:"/api/getserverCopy/",
        method:"get",
        params:{
          page:that.currentpage,
          pageSize:that.pageSize
        }
      }).then(res=>{
        console.log(res)
        if(res.data.status){
          this.$notify({
            title:'暂无更多服务器备份！'
          })
        }else if(res.status == 200){
          if(that.newsdata.length==0)
            that.newsdata = res.data;
          else
            that.newsdata = that.newsdata.concat(res.data);
        }
      })
    },
    add(){
      var that = this;
      this.$confirm('确认备份当前服务器')
          .then(_=>{
            that.$axios({
              url:'/api/addNewServerCopy/'
            }).then(res=>{
              if(res.data.status){
                this.$notify({
                  title:'备份失败'
                })
              }else{
                this.$notify({
                  title:'备份成功！'
                })
              }
            })
          })
    },
    handleApply(index, row){
      var that = this;
      var ID = row.serverID;
      that.$confirm('确认应用？')
      then(_=>{
        that.$notify({
          title:'请立刻关闭并稍后重启！'
        })
        that.$axios({
          url:'/api/ApplyNewServerCopy/',
          methods:'post',
          params:{
            ID
          }
        })
      })
    },
    handleDelete(index, row){
      var that = this;
      var ID = row.serverID;
      this.$confirm('确认删除此备份?')
          .then(_=>{
            //发起请求,然后删除
            that.$axios({
              url:'/api/deleteServerCopy/',
              method:'get',
              params:{
                ID
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
</style>