<template>
  <div>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>数据库备份与恢复</span>
        <span></span>
      </div>
      <el-container>
        <el-header><h2>已通过审核</h2></el-header>
        <el-main>
          <el-button
              plain
              @click="open1">
            通知栏1
          </el-button>
          <el-button
              plain
              @click="open2">
            通知栏2
          </el-button>
          <ul>
            <li v-for="(item,index) in $store.state.listAll">
              <div>
                <span>{{index+1}}.{{item}}</span>
                <br>
                <el-button @click="getAudio($store.state.musicID[index])">播放</el-button>
                <br>
                <span>审核时间:{{$store.state.updateTime}}</span>
                <br>
                <span>点赞数:{{support}}</span>
              </div>
              <br>
            </li>
          </ul>
          <audio ref='audio' @play="play" @pause="pause" :src="soundUrl" controls  loop class="el-icon-video-play"></audio>
        </el-main>
      </el-container>
    </el-card>

  </div>
</template>

<script>
export default {
  name: "viewed",
  data(){
    return {
      support:"",
      soundUrl:""
    }
  },
  methods:{
    play:function (){
      this.isPlaying=true;
    },
    pause:function (){
      this.isPlaying=false;
    },
    open1() {
      const h = this.$createElement;

      this.$store.commit("completeExamine");

      this.$notify({
        title: this.$store.state.title,
        message: h('i', { style: 'color: teal'}, this.$store.state.message)
      });
    },
    open2() {
      const h = this.$createElement;

      this.$notify({
        title: this.$store.state.title,
        message: h('i', { style: 'color: teal'}, this.$store.state.message)
      });
    },
    getAudio(index){
      this.axios({
        url:'/api/audio/'+index,
        method:'get',
      }).then(res=>{
        this.soundUrl=res.config.url
        console.log(this.soundUrl)
      })
    }
  }
  //获取点赞数
  // created() {
  //   this.$axios.get('')
  //   .then(response=>{
  //     this.support=response.data.support
  //   })
  // }
}
</script>

<style scoped>

</style>
