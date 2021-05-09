import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Home from "../views/Home";
import welcome from "@/components/welcome";
import museum from "@/components/museum";
import collection from "@/components/collection";
import comment from "@/components/comment";
import db from "@/components/db";
import db_log from "@/components/db_log";
import exhibition from "@/components/exhibition";
import explain from "@/components/explain";
import manage from "@/components/manage";
import news from "@/components/news";
import not_viewed from "@/components/not_viewed";
import server from "@/components/server";
import userinfo from "@/components/userinfo";
import viewed from "@/components/viewed";
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'login',
    component: Login
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/home',
    name: Home,
    component: Home,
    children:[
      {
        path:'',
        component:welcome
      },
      {
        path:'museum',
        component:museum
      },
      {
        path:'collection',
        component:collection
      },
      {
        path:'comment',
        component:comment
      },
      {
        path:'db',
        component:db
      },
      {
        path:'db_log',
        component:db_log
      },
      {
        path:'exhibition',
        component:exhibition
      },
      {
        path:'explain',
        component:explain
      },
      {
        path:'manage',
        component:manage
      },
      {
        path:'news',
        component:news
      },
      {
        path:'not_viewed',
        component:not_viewed
      },
      {
        path:'server',
        component:server
      },
      {
        path:'userinfo',
        component:userinfo
      },
      {
        path:'viewed',
        component:viewed
      },
    ]
  }
]

const router = new VueRouter({
  routes
})

export default router
