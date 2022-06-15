import Vue from 'vue'
import VueRouter from 'vue-router'

import HomeView from '@/views/HomeView.vue'
import NotFound404View from '@/views/NotFound404View.vue'

import LoginView from '@/views/user/LoginView.vue'
import SignUpView from '@/views/user/SignUpView.vue'
import UserProfileView from '@/views/user/UserProfileView.vue'

import CommunityView from '@/views/community/CommunityView.vue'
import ArticleView from '@/views/community/ArticleView.vue'
import ArticleCreateView from '@/views/community/ArticleCreateView.vue'
import ArticleUpdateView from '@/views/community/ArticleUpdateView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/404',
    name: 'NotFound404View',
    component: NotFound404View
  },
//////////////////////////////////////////
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/profile/:username',
    name: 'UserProfileView',
    component: UserProfileView
  },
//////////////////////////////////////////
  {
    path: '/community',
    name: 'CommunityView',
    component: CommunityView
  },
  {
    path: '/community/form',
    name: 'ArticleCreateView',
    component: ArticleCreateView
  },
  {
    path: '/community/:articlePk',
    name: 'ArticleView',
    component: ArticleView
  },
  {
    path: '/community/:articlePk/form',
    name: 'ArticleUpdateView',
    component: ArticleUpdateView
  },


]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
