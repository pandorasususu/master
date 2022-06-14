import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'

import HomeView from '@/views/HomeView.vue'
import MoviesView from '@/views/movies/MoviesView.vue'
import MoviesDetail from '@/views/movies/MoviesDetail.vue'

import SignUpView from '@/views/accounts/SignUpView.vue'
import LoginView from '@/views/accounts/LoginView.vue'
import ProfileView from '@/views/accounts/ProfileView.vue'

import CommunityView from '@/views/communities/CommunityView.vue'
import ArticleView from '@/views/communities/ArticleView.vue'
import ArticleCreateView from '@/views/communities/ArticleCreateView.vue'
import ArticleUpdateView from '@/views/communities/ArticleUpdateView.vue'

import NotFound404 from '@/views/NotFound404.vue'

Vue.use(VueRouter)

const routes = [
  //메인 홈페이지
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/movies/:movieId',
    name: 'moviesDetail',
    component: MoviesDetail
  },
  {
    path: '/movies',
    name: 'movies',
    component: MoviesView
  },

  //계정 기능
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView
  },

  //커뮤니티 기능
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/community/create',
    name: 'articleCreate',
    component: ArticleCreateView
  },
  {
    path: '/community/:articlePk',
    name: 'article',
    component: ArticleView
  },
  {
    path: '/community/:articlePk/update',
    name: 'ArticleUpdate',
    component: ArticleUpdateView
  },

  //에러
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  // 이전 페이지에서 발생한 에러메시지 삭제
  store.commit('SET_AUTH_ERROR', null)

  const { isLoggedIn } = store.getters

  const noAuthPages = ['login','signup']

  const isAuthRequired = !noAuthPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    // alert('Require Login. Redirecting..')
    next({ name: 'login' })
  } else {
    next()
  }

  if (!isAuthRequired && isLoggedIn) {
    next({ name: 'home'})
  }
})

export default router
