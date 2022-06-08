import router from '@/router'
import djangourls from '@/urls/djangourls'
import axios from 'axios'


export default {
  state: {
    token: localStorage.getItem('token') || '',
    currentUser: {},
    userProfile: {},
    authError: null,
  },
  getters: {
    isLoggedin(state) {return !!state.token},
    currentUser(state) {return state.currentUser},
    userProfile(state) {return state.userProfile},
    authError(state) {return state.authError},
    authHeader(state) {return ({Authorization: `Token ${state.token}`})}
  },
  mutations: {
    SET_TOKEN(state, token) { return state.token = token },
    SET_CURRENT_USER(state, user) {return state.currentUser = user},
    SET_USER_PROFILE(state, userprofile) {return state.userProfile = userprofile},
    SET_USER_FOLLOW(state, followInfo) {
      state.userProfile.followings_count = followInfo.followings_count
      state.userProfile.followers_count = followInfo.followers_count
    },
    SET_AUTH_ERROR(state, error) {return state.authError = error},
  },
  actions: {
    setToken({commit}, token){
      commit('SET_TOKEN', token)
      localStorage.setItem('token', token)
    },
    removeToken({commit}){
      // SET_TOKEN은 token을 인자로 필요한 거 같은데... ''를 넣어보고 에러나면 원래대로 아무것도 넣지 않는 걸로
      commit('SET_TOKEN', '')
      localStorage.setItem('token', '')      
    },
    signUp({commit, dispatch, getters}, signUpInfo){
      axios({
        method:'post',
        url: djangourls.accounts.signup(),
        data: signUpInfo
      })
      .then(res => {
        dispatch('setToken', res.data.key)
        dispatch('getCurrentUser')
        dispatch('getUserProfile', {username: getters.getCurrentUser.username})
        router.push({name: 'profile', params: { username: getters.getCurrentUser.username }})
      })
      .catch(err => {
        commit('SET_AUTH_ERROR', err.response.data)
      })
    },
    logIn({commit, dispatch}, LogInInfo){
      console.log('logIn에서 받은 정보',LogInInfo)
      axios({
        method:'post',
        url: djangourls.accounts.login(),
        data: LogInInfo
      })
      .then(res => {
        dispatch('setToken', res.data.key)
        dispatch('getCurrentUser')
        alert('로그인되셨습니다!')
        // dispatch('getUserProfile', {username: getters.getCurrentUser.username})
        // router.push({name: 'profile', params: { username: getters.getCurrentUser.username }})
      })
      .catch(err => {
        commit('SET_AUTH_ERROR', err.response.data)
      })
    },
    logOut({commit, dispatch, getters}){
      axios({
        method:'post',
        url: djangourls.accounts.logout(),
        headers: getters.authHeader
      })
      .then(res => {
        dispatch('removeToken')
        commit('SET_CURRENT_USER', {})
        alert('성공적으로 로그아웃하셨습니다!')
        router.push({name: 'home'})
      })
      .catch(err => console.log(err.response.data))

    },
    getCurrentUser({commit, dispatch, getters}){
      if (getters.isLoggedin) {
        axios({
          method:'get',
          url: djangourls.accounts.currentUserInfo(),
          headers: getters.authHeader
        })
        .then(res => {
          commit('SET_CURRENT_USER', res.data)
        })
        .catch(err => {
          if (err.response.status === 401) {
            dispatch('removeToken')
            router.push({name: 'login'})
          }
        })
    }
    },
    getUserProfile({commit, getters}, {username}){
      axios({
        method: 'get',
        url: djangourls.accounts.userProfileOrFollow(username),
        headers: getters.authHeader
      })
      .then(res => {
        commit('SET_USER_PROFILE', res.data)
      })
      .catch(err => console.log(err.response.data))
    },
    followUser({commit, getters}, username){
      axios({
        method: 'post',
        url: djangourls.accounts.userProfileOrFollow(username),
        headers: getters.authHeader
      })
      .then(res => {
        commit('SET_USER_PROFILE', res.data)
      })
      .catch(err => console.log(err.response.data))
    },
  },

}
