<template>
  <el-card class="box-card">
    <div slot="header" class="clearfix">
      <span>博物馆管理</span>
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
                data.name.toLowerCase().includes(search.toLowerCase())
            )
            .slice((currentPage - 1) * pagesize, currentPage * pagesize)
        "
          stripe
          style="width: 100%"
      >
        <el-table-column sortable  fixed  prop="id" label="编号" width="80"> </el-table-column>
        <el-table-column sortable fixed prop="name" label="博物馆名" width="150">
        </el-table-column>
        <el-table-column sortable prop="intro" label="介绍" width="150">
        </el-table-column>
        <el-table-column sortable prop="open" label="开放时间" width="150">
        </el-table-column>
        <el-table-column sortable prop="link" label="链接" width="150">
        </el-table-column>
        <el-table-column sortable prop="level" label="等级" width="150">
        </el-table-column>
        <el-table-column sortable prop="location" label="位置" width="150"> </el-table-column>

        <el-table-column sortable prop="grade" label="评分" width="150"> </el-table-column>
        <el-table-column sortable prop="tele" label="电话" width="150"> </el-table-column>
        <el-table-column sortable prop="fee" label="门票" width="150"> </el-table-column>
        <el-table-column sortable prop="bulid" label="建馆时间" width="150"> </el-table-column>
        <el-table-column sortable prop="num" label="藏品数" width="150"> </el-table-column>
        <el-table-column sortable prop="city" label="城市" width="150"> </el-table-column>
        <el-table-column sortable prop="look" label="浏览量" width="150"> </el-table-column>
        <el-table-column sortable prop="status" label="状态" width="150"> </el-table-column>

        <el-table-column align="right" width="170">
          <template slot="header" slot-scope="">
            <el-input
                v-model="search"
                size="mini"
                placeholder="输入博物馆名称搜索"
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
            >删除</el-button>
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
          title="添加博物馆信息"
          :visible.sync="dialogVisible1"
          width="30%"
      >
        <el-form ref="form" :model="form" label-width="80px">
          <el-form-item label="博物馆名">
            <el-input v-model="form.name"></el-input>
          </el-form-item>
          <el-form-item label="介绍">
            <el-input v-model="form.intro "></el-input>
          </el-form-item>
          <el-form-item label="开放时间">
            <el-input v-model="form.open "></el-input>
          </el-form-item>
          <el-form-item label="链接">
            <el-input v-model="form.link "></el-input>
          </el-form-item>
          <el-form-item label="等级">
            <el-input v-model="form.level "></el-input>
          </el-form-item>
          <el-form-item label="位置">
            <el-input v-model="form.location "></el-input>
          </el-form-item>
          <el-form-item label="电话">
            <el-input v-model="form.tele "></el-input>
          </el-form-item>
          <el-form-item label="评分">
            <el-input v-model="form.grade "></el-input>
          </el-form-item>
          <el-form-item label="门票">
            <el-input v-model="form.fee "></el-input>
          </el-form-item>
          <el-form-item label="建馆时间">
            <el-input v-model="form.bulid "></el-input>
          </el-form-item>
          <el-form-item label="藏品数">
            <el-input v-model="form.num "></el-input>
          </el-form-item>
          <el-form-item label="城市">
            <el-input v-model="form.city "></el-input>
          </el-form-item>
          <el-form-item label="浏览量">
            <el-input v-model="form.look "></el-input>
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
          title="添加博物馆信息"
          :visible.sync="dialogVisible2"
          width="30%"
      >
        <el-form ref="form" :model="form" label-width="80px">
          <el-form-item label="博物馆名">
            <el-input v-model="form.name"></el-input>
          </el-form-item>
          <el-form-item label="介绍">
            <el-input v-model="form.intro "></el-input>
          </el-form-item>
          <el-form-item label="开放时间">
            <el-input v-model="form.open "></el-input>
          </el-form-item>
          <el-form-item label="链接">
            <el-input v-model="form.link "></el-input>
          </el-form-item>
          <el-form-item label="电话">
            <el-input v-model="form.tele "></el-input>
          </el-form-item>
          <el-form-item label="等级">
            <el-input v-model="form.level "></el-input>
          </el-form-item>
          <el-form-item label="位置">
            <el-input v-model="form.location "></el-input>
          </el-form-item>
          <el-form-item label="评分">
            <el-input v-model="form.grade "></el-input>
          </el-form-item>
          <el-form-item label="门票">
            <el-input v-model="form.fee "></el-input>
          </el-form-item>
          <el-form-item label="建馆时间">
            <el-input v-model="form.bulid "></el-input>
          </el-form-item>
          <el-form-item label="藏品数">
            <el-input v-model="form.num "></el-input>
          </el-form-item>
          <el-form-item label="城市">
            <el-input v-model="form.city "></el-input>
          </el-form-item>
          <el-form-item label="浏览量">
            <el-input v-model="form.look "></el-input>
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
          title="添加博物馆信息"
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
  name: "museum",
  data() {
    return {
      total: 1000,
      pagesize: 7,
      currentPage: 1,
      form: {
        id: "",
        name: "",
        location: "",
        intro: "",
        open:"",
        tele:"",
        link:"",
        level:"",
        grade:"",
        fee:"",
        bulid:"",
        num:"",
        city:"",
        look:"",
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
          .post("/api/addmuseum", {
            id: this.form.id,
            name: this.form.name,
            location: this.form.location,
            intro: this.form.intro,
            open:this.form.open,
            link:this.form.link,
            level:this.form.level,
            grade:this.form.grade,
            fee:this.form.fee,
            bulid:this.form.bulid,
            num:this.form.num,
            city:this.form.city,
            tele:this.form.tele,
            look:this.form.look,
            status:this.form.status
          })
          .then((response) => {
            console.log(response);
          });
      (this.form.name = ""),
          (this.form.location = ""),
          (this.form.intro  = ""),
          (this.form.open = ""),
          (this.form.link = ""),
          (this.form.level = ""),
          (this.form.grade  = ""),
          (this.form.fee = ""),
          (this.form.bulid  = ""),
          (this.form.tele  = ""),
          (this.form.num  = ""),
          (this.form.city  = ""),
          (this.form.look  = ""),
          (this.form.status  = ""),
          location.reload();
    },
    tijiao2() {
      this.$axios
          .post("/api/editmuseum", {
            id: this.form.id,
            name: this.form.name,
            location: this.form.location,
            intro: this.form.intro,
            open:this.form.open,
            link:this.form.link,
            level:this.form.level,
            grade:this.form.grade,
            fee:this.form.fee,
            bulid:this.form.bulid,
            tele:this.form.tele,
            num:this.form.num,
            city:this.form.city,
            look:this.form.look,
            status:this.form.status
          })
          .then((response) => {
            console.log(response);
          });
      (this.form.name = ""),
          (this.form.location = ""),
          (this.form.intro  = ""),
          (this.form.open = ""),
          (this.form.link = ""),
          (this.form.level = ""),
          (this.form.grade  = ""),
          (this.form.fee = ""),
          (this.form.bulid  = ""),
          (this.form.tele  = ""),
          (this.form.num  = ""),
          (this.form.city  = ""),
          (this.form.look  = ""),
          (this.form.status  = ""),
          location.reload();
    },
    tijiao3() {
      this.$axios
          .post("/api/deletemuseum", {
            id: this.form.id,
          })
          .then((response) => {
            console.log(response);
          });
      location.reload();
    },
    handleEdit(index, row) {
      this.form.id = row.id;
      this.form.name = row.name;
      this.form.intro = row.intro;
      this.form.open  = row.open ;
      this.form.link   = row.link ;
      this.form.tele   = row.tele ;
      this.form.level  = row.level ;
      this.form.location  = row.location ;
      this.form.grade  = row.grade ;
      this.form.fee  = row.fee ;
      this.form.bulid  = row.bulid ;
      this.form.num  = row.num ;
      this.form.city  = row.city ;
      this.form.look  = row.look ;
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
    this.$axios.get("/api/getmuseum").then((response) => {
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