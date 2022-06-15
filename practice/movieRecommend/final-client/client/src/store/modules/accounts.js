import router from '@/router'
import djangourl from '@/urls/djangourl'
import axios from 'axios'

export default {
  state: {
    token: localStorage.getItem('token') || '',
    currentUser: {},
    userProfile: {},
    authError: null,
  },
  getters: {
    isLoggedIn(state) {
      return !!state.token
    },
    //currentUser는 현재 로그인되어 있는 유저의 기본 정보
    currentUser(state) {
      return state.currentUser
    },
    //profile은 대상 유저의 기본 정보 + 작성글/좋아요글/(+작성댓글/좋아요댓글/본영화/보고싶은영화/기타)
    userProfile(state) {
      console.log(state.userProfile.username)
      return state.userProfile
    },
    authError(state) {
      return state.authError
    },
    //유저 인증을 위해 axios 요청 보낼 때 필수적으로 보내야됨. token이 있으면 authHeadr를 getter로 불러올 수 있음
    authHeader(state) {
      return ({Authorization: `Token ${state.token}`})
    }
  },
  mutations: {
    SET_TOKEN(state, token){
      return state.token = token
    },
    SET_CURRENT_USER(state, user) {
      console.log('지금 커런트 유저 설정됨', user)
      return state.currentUser = user
    },
    SET_USER_PROFILE(state, userProfile) {
      console.log('userprofile mutation',userProfile)
      return state.userProfile = userProfile
    },
    SET_USER_PROFILE_FOLLOW(state, userProfile) {
      return state.userProfile = userProfile

    },
    SET_AUTH_ERROR(state, error) {
      return state.authError = error
    }
  },
  actions: {
    setToken({commit}, token){
      commit('SET_TOKEN', token)
      console.log('setToken완료')
      localStorage.setItem('token',token)
    },
    removeToken({commit}){
      commit('SET_TOKEN')
      localStorage.setItem('token','')
    },

    signUp({commit, dispatch, getters}, credentials){
      axios({
        url: djangourl.accounts.signup(),
        method: 'post',
        data: credentials
      })
      .then(res => {
        dispatch('setToken', res.data.key)
        dispatch('getCurrentUser')
        setTimeout(
          function(){
            console.log('회원가입 후 currentUser',getters.currentUser)
            dispatch('getUserProfile', {username: getters.currentUser.username})
            router.push({name: 'profile', params:{ username: getters.currentUser.username }})
          }, 10
        )
      })
      .catch(err => {
        console.error(err.response.data)
        commit('SET_AUTH_ERROR', err.response.data)
      })
    },

    // userDelete({getters, dispatch}, username){
    //   if (confirm('정말로 탈퇴하시겠습니까?')){
    //     axios({
    //       url: djangourl.accounts.userDelete(username),
    //       method: 'delete',
    //       headers: getters.authHeader
    //     })
    //       .then((msg) => {
    //         dispatch('removeToken')
    //         alert(msg.delete_message)
    //         router.push({name: 'home'})
    //       })
    //       .catch(err => {
    //         console.error(err.response.data)
    //       })      
    //   }
    // },
    login({commit, dispatch, getters}, credentials){
      console.log('login에서', credentials)
      axios({
        url: djangourl.accounts.login(),
        method: 'post',
        data: credentials
      })
      .then(res => {
        dispatch('setToken', res.data.key)
        dispatch('getCurrentUser')
        //로그인과 회원가입 기능에서getCurrentUser하고 바로 getUserProfile하니 계속 그 전에 로그인되어 있었던 계정의 userProfile로 이동
        //setTimeout 함수를 통해 두 함수 사이에 약간의 지연을 두어 순차적으로 getCurrentUser가 완료 된 후 getUserProfile이 시행되도록 함
        setTimeout(
          function(){
            console.log('로그인 후 currentUser',getters.currentUser)
            dispatch('getUserProfile', {username: getters.currentUser.username})
            router.push({name: 'profile', params:{ username: getters.currentUser.username }})
          }, 10
        )
      })
      .catch(err => {
        console.error(err.response.data)
        commit('SET_AUTH_ERROR', err.response.data)
      })
    },
    logout({getters, dispatch, commit}){
      if(confirm('정말로 로그아웃 하시겠습니까?')){
        axios({
          url: djangourl.accounts.logout(),
          method: 'post',
          headers: getters.authHeader
        })
        .then(() => {
          dispatch('removeToken')
          commit('SET_CURRENT_USER', {})
          alert('성공적으로 로그아웃하셨습니다!')
          router.push({name: 'home'})
        })
        .catch(err => {
          console.error(err.response.data)
        })
      }
    },
    getCurrentUser({commit, getters, dispatch}){
      if (getters.isLoggedIn){
        axios({
          url: djangourl.accounts.currentUserInfo(),
          method: 'get',
          headers: getters.authHeader
        })
        .then(res => {
          commit('SET_CURRENT_USER', res.data)
        })
        .catch(err => {
          if(err.response.status === 401) {
            dispatch('removeToken')
            router.push({ name: 'login' })
          }
        })
      }
    },

    getUserProfile({commit, getters}, {username}){
      axios({
        method: 'get',
        url: djangourl.accounts.userProfile(username),
        headers: getters.authHeader
      })
      .then(res => {
        commit('SET_USER_PROFILE', res.data)
      })
      .catch(err => {
        console.error(err.response)
      })
    },

    userFollow({commit, getters}){
      const username = getters.userProfile.username
      axios({
        method: 'post',
        url: djangourl.accounts.userFollow(username),
        headers: getters.authHeader
      })
      .then(res => {
        commit('SET_USER_PROFILE_FOLLOW', res.data)
        console.log(res.data)
      })
      .catch(err => {
        console.error(err.response)
      })
    },
  },

}
