<template>
  <div>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>数据库备份与恢复</span>
        <span></span>
      </div>
      <el-container>
        <el-header><h2>待审核项目</h2></el-header>
        <el-main>
          <div>
            <el-card v-for="(item,index) in list">
              <br>
              <div>
                <span>{{index+1}}.{{item}}</span>
                <el-button @click="getAudio(index)" icon="el-icon-video-play" type="success" circle></el-button>
                <br>
                <br>
                <el-button @click="go(item,index)" type="primary" >通过</el-button>
                <el-button @click="reject(item,index)" type="danger">驳回</el-button>
              </div>
            </el-card>
          </div>
          <audio ref='audio' @play="play" @pause="pause" :src="soundUrl" controls loop class="el-icon-video-play"></audio>
        </el-main>
        <el-footer></el-footer>
      </el-container>
    </el-card>

  </div>
</template>

<script>
export default {
  name: "not_viewed",
  data(){
    return {
      list:[],
      inputValue:"",
      isPlaying:false,
      soundFile:[],
      soundUrl:"",
    }
  },
  methods:{
    reject:function (name,index){
      this.axios({
        url:'/api/modify/',
        data:{
          modify:name
        },
        method:'post'
      }).then(
          res=>{
            console.log(res)
          }
      )
      this.$store.state.title="审核未通过";
      this.$store.state.message="请重新编辑讲解内容";
      this.inputValue=this.list[index];
      this.list.splice(index,1);
    },
    add:function (){
      this.list.push(this.inputValue);
      this.$store.state.title="暂无消息";
      this.$store.state.message="";
    },
    play:function (){
      this.isPlaying=true;
    },
    pause:function (){
      this.isPlaying=false;
    },
    go:function (name,index){
      this.axios({
        url:'/api/del/',
        data:{del:name},
        method:'post'
      }).then(res=>{
        console.log(res)
      })
      this.$store.state.musicID.push(index)
      console.log(this.$store.state.musicID)
      this.addDate();
      this.$store.state.listAll.push(this.list[index])
      //this.list.splice(index,1);
    },
    addDate(){
      const nowDate = new Date();
      const date = {
        year: nowDate.getFullYear(),
        month: nowDate.getMonth() + 1,
        date: nowDate.getDate(),
      }
      const newmonth = date.month>10?date.month:'0'+date.month
      const day = date.date>10?date.date:'0'+date.date
      this.$store.state.updateTime = date.year + '-' + newmonth + '-' + day

    },
    getAudio(index){
      this.axios({
        url:'/api/audio/'+index,
        method:'get',
      }).then(res=>{
        this.soundUrl=res.config.url
      })
    }
  },
  created(){
    this.$axios.get("/api/user/")
        .then(response=>{
          //console.log(response)
          this.list=response.data.name
          this.$store.state.listExamine=this.list
          //console.log(this.$store.state.listExamine)
        })
    // this.$axios.get("/api/audio/1")
    //     .then(response=>{
    //       console.log(response)
    //     })
  },
}
</script>

<style scoped>

</style>
