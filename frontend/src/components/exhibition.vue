<template>
  <el-card class="box-card">
    <div slot="header" class="clearfix">
      <span>展览管理</span>
      <span></span>

      <el-button style="float: right" size="mini" @click="dialogVisible1 = true"
      >添加</el-button
      >


    </div>

    <div>
      <el-table
          :data="
          datalist
            .filter(
              (data) =>
                !search ||
                data.id.toLowerCase().includes(search.toLowerCase())
            )
            .slice((currentPage - 1) * pagesize, currentPage * pagesize)
        "
          stripe
          style="width: 100%"
      >
        <el-table-column sortable fixed  prop="id" label="编号" width="80"> </el-table-column>
        <el-table-column sortable fixed prop="mu_id" label="博物馆号" width="150">
        </el-table-column>
        <el-table-column sortable prop="intro" label="介绍" width="150">
        </el-table-column>
        <el-table-column sortable prop="list" label="清单" width="150">
        </el-table-column>
        <el-table-column sortable prop="pic" label="图片链接" width="150">
        </el-table-column>
        <el-table-column sortable prop="theme" label="主题" width="150">
        </el-table-column>
        <el-table-column sortable prop="location" label="位置" width="150"> </el-table-column>

        <el-table-column sortable prop="time" label="时间" width="150"> </el-table-column>
        <el-table-column sortable prop="tele" label="电话" width="150"> </el-table-column>
        <el-table-column sortable prop="status" label="状态" width="150"> </el-table-column>

        <el-table-column align="right" width="150">
          <template slot="header" slot-scope="">
            <el-input
                v-model="search"
                size="mini"
                placeholder="输入展览名称搜索"
            />
          </template>
          <template slot-scope="scope">
            <el-button
                size="mini"
                type="primary"
                @click="
                handleEdit(scope.$index, scope.row), (dialogVisible2 = true)
              "
            >编辑</el-button
            >

            <el-button
                size="mini"
                type="danger"
                @click="
                handleDelete(scope.$index, scope.row), (dialogVisible3 = true)
              "
            >删除</el-button
            >

          </template>
        </el-table-column>
      </el-table>
      <el-pagination
          style="text-align: center"
          layout="prev, pager, next"
          @current-change="current_change"
          :page-size="pagesize"
          :total="datalist.length"
      >
      </el-pagination>
      <el-dialog
          title="添加展览信息"
          :visible.sync="dialogVisible1"
          width="30%"
      >
        <el-form ref="form" :model="form" label-width="80px">
          <el-form-item label="博物馆号">
            <el-input v-model="form.mu_id"></el-input>
          </el-form-item>
          <el-form-item label="介绍">
            <el-input v-model="form.intro "></el-input>
          </el-form-item>
          <el-form-item label="照片链接">
            <el-input v-model="form.pic "></el-input>
          </el-form-item>
          <el-form-item label="清单">
            <el-input v-model="form.list "></el-input>
          </el-form-item>
          <el-form-item label="电话">
            <el-input v-model="form.tele "></el-input>
          </el-form-item>
          <el-form-item label="主题">
            <el-input v-model="form.theme "></el-input>
          </el-form-item>
          <el-form-item label="位置">
            <el-input v-model="form.location "></el-input>
          </el-form-item>
          <el-form-item label="时间">
            <el-input v-model="form.time "></el-input>
          </el-form-item>
          <el-form-item label="状态">
            <el-input v-model="form.status "></el-input>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible1 = false">取 消</el-button>
          <el-button
              type="primary"
              @click="tijiao1('form'), (dialogVisible1 = false)"
          >确 定</el-button
          >
        </span>
      </el-dialog>
      <el-dialog
          title="添加展览信息"
          :visible.sync="dialogVisible2"
          width="30%"
      >
        <el-form ref="form" :model="form" label-width="80px">
          <el-form-item label="博物馆号">
            <el-input v-model="form.mu_id"></el-input>
          </el-form-item>
          <el-form-item label="介绍">
            <el-input v-model="form.intro "></el-input>
          </el-form-item>
          <el-form-item label="照片链接">
            <el-input v-model="form.pic "></el-input>
          </el-form-item>
          <el-form-item label="清单">
            <el-input v-model="form.list "></el-input>
          </el-form-item>
          <el-form-item label="电话">
            <el-input v-model="form.tele "></el-input>
          </el-form-item>
          <el-form-item label="主题">
            <el-input v-model="form.theme "></el-input>
          </el-form-item>
          <el-form-item label="位置">
            <el-input v-model="form.location "></el-input>
          </el-form-item>
          <el-form-item label="时间">
            <el-input v-model="form.time "></el-input>
          </el-form-item>
          <el-form-item label="状态">
            <el-input v-model="form.status "></el-input>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible2 = false">取 消</el-button>
                <el-button
                    type="primary"
                    @click="tijiao2('form'), (dialogVisible2 = false)"
                >确 定</el-button
                >
              </span>
      </el-dialog>
      <el-dialog
          title="添加展览信息"
          :visible.sync="dialogVisible3"
          width="30%"
      >
        <span  >确认删除吗</span>
        <span slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible3 = false">取 消</el-button>
                <el-button
                    type="primary"
                    @click="tijiao3('form'), (dialogVisible3 = false)"
                >确 定</el-button
                >
              </span>
      </el-dialog>
    </div>
  </el-card>
</template>

<script>
export default {
  name: "exhibition",
  data() {
    return {
      total: 1000,
      pagesize: 7,
      currentPage: 1,
      form: {
        id: "",
        mu_id: "",
        location: "",
        intro: "",
        pic:"",
        tele:"",
        theme:"",
        time:"",
        list:"",

        status:""
      },
      dialogVisible1: false,
      dialogVisible2: false,
      dialogVisible3: false,
      datalist: [
      ],
      search: "",
    };
  },
  methods: {
    tijiao1() {
      this.$axios
          .post("/api/addexhibition", {
            id: this.form.id,
            mu_id: this.form.mu_id,
            location: this.form.location,
            intro: this.form.intro,
            list:this.form.list,
            pic:this.form.pic,
            theme:this.form.theme,
            time:this.form.time,

            tele:this.form.tele,

            status:this.form.status
          })
          .then((response) => {
            console.log(response);
          });
      (this.form.mu_id = ""),
          (this.form.location = ""),
          (this.form.intro  = ""),
          (this.form.list = ""),
          (this.form.pic = ""),
          (this.form.theme = ""),
          (this.form.time  = ""),

          (this.form.tele  = ""),

          (this.form.status  = ""),
          location.reload();
    },
    tijiao2() {
      this.$axios
          .post("/api/editexhibition", {
            id: this.form.id,
            mu_id: this.form.mu_id,
            location: this.form.location,
            intro: this.form.intro,
            list:this.form.list,
            pic:this.form.pic,
            theme:this.form.theme,
            time:this.form.time,

            tele:this.form.tele,

            status:this.form.status
          })
          .then((response) => {
            console.log(response);
          });
      (this.form.mu_id = ""),
          (this.form.location = ""),
          (this.form.intro  = ""),
          (this.form.list = ""),
          (this.form.pic = ""),
          (this.form.theme = ""),
          (this.form.time  = ""),

          (this.form.tele  = ""),

          (this.form.status  = ""),
          location.reload();
    },
    tijiao3() {
      this.$axios
          .post("/api/deleteexhibition", {
            id: this.form.id,
          })
          .then((response) => {
            console.log(response);
          });
      location.reload();
    },
    handleEdit(index, row) {
      this.form.id = row.id;
      this.form.mu_id = row.mu_id;
      this.form.intro = row.intro;
      this.form.pic  = row.pic ;
      this.form.list   = row.list ;
      this.form.tele   = row.tele ;
      this.form.theme  = row.theme ;
      this.form.location  = row.location ;
      this.form.time  = row.time ;
      this.form.status  = row.status ;
    },
    handleDelete(index, row) {
      this.form.id = row.id;
    },
    handleClose(done) {
      this.$confirm("确认关闭？")
          .then((_) => {
            done();
          })
          .catch((_) => {});
    },
    current_change: function (currentPage) {
      this.currentPage = currentPage;
    },
  },
  created() {
    this.$axios.get("/api/getexhibition").then((response) => {
      this.datalist = response.data.data;
    });
  },
};
</script>

<style scoped>
.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both;
}
</style>