import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    listAll:[],
    listExamine:[],
    updateTime:"",
    message:"",
    title:"暂无消息",
    musicID:[]
  },
  mutations: {
    completeExamine(){
      //console.log(this.state.listExamine)
      var temp=this.state.listExamine
      if(temp.length!==0){
        this.state.title="通知"
        this.state.message="有消息未审核完成"
      }
    }
  },
  actions: {
  },
  modules: {
  }
})
