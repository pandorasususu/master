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
    isLoggedIn(state) {return !!state.token},
    currentUser(state) {return state.currentUser},
    userProfile(state) {return state.userProfile},
    authError(state) {return state.authError},
    authHeader(state) {return ({Authorization: `Token ${state.token}`})}
  },
  mutations: {
    SET_TOKEN(state, token) { return state.token = token },
    SET_CURRENT_USER(state, user) {return state.currentUser = user},
    SET_USER_PROFILE(state, userprofile) {return state.userProfile = userprofile},
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

    signUp({commit, dispatch}, signUpInfo){
      axios({
        method:'post',
        url: djangourls.account.signup(),
        data: signUpInfo
      })
      .then(res => {
        dispatch('setToken', res.data.key)
        dispatch('getCurrentUser')
        router.push({name: 'home'})
      })
      // 로그인한 유저의 프로필로 이동하는 건 나중에 구현
      // 비동기 작업을 동기 작업처럼 수행할 수 있게 .then으로 chaining했는데도
      // getCurrentUser 작업이 끝나기 전에 getUserProfile작업이 시작되어서 username이 제대로 안넘어감
      // .then(() => {
      //   dispatch('getUserProfile', getters.getCurrentUser.username)
      // })
      // .then(() => {
      //   router.push({name: 'profile', params: { username: getters.getCurrentUser.username }})
      // })
      .catch(err => {
        commit('SET_AUTH_ERROR', err)
        console.error(err.response.data)
      })
    },

    logIn({commit, dispatch}, LogInInfo){
      axios({
        method:'post',
        url: djangourls.account.login(),
        data: LogInInfo
      })
      .then(res => {
        dispatch('setToken', res.data.key)
        dispatch('getCurrentUser')
        router.push({name: 'home'})

      })
      // 로그인한 유저의 프로필로 이동하는 건 나중에 구현
      // 비동기 작업을 동기 작업처럼 수행할 수 있게 .then으로 chaining했는데도
      // getCurrentUser 작업이 끝나기 전에 getUserProfile작업이 시작되어서 username이 제대로 안넘어감
      // .then(() => {
      //   dispatch('getUserProfile', getters.getCurrentUser.username)
      // })
      // .then(() => {
      //   router.push({name: 'profile', params: { username: getters.getCurrentUser.username }})
      // })
      .catch(err => {
        commit('SET_AUTH_ERROR', err)
        console.error(err)
      })
    },

    logOut({commit, dispatch, getters}){
      axios({
        method:'post',
        url: djangourls.account.logout(),
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
      console.log('getCurrentUser start')
      if (getters.isLoggedIn) {
        console.log('getCurrentUser enter if')
        axios({
          method:'get',
          url: djangourls.account.currentUserInfo(),
          headers: getters.authHeader
        })
        .then(res => {
          console.log('getCurrentUser then')
          commit('SET_CURRENT_USER', res.data)
          return res.data
        })
        .catch(err => {
          if (err.response.status === 401) {
            dispatch('removeToken')
            router.push({name: 'login'})
          }
        })   
      }
    },

    getUserProfile({commit, getters}, username){
      console.log('getUserProfile 실행!', username)
      axios({
        method: 'get',
        url: djangourls.user.userProfileOrFollow(username),
        headers: getters.authHeader
      })
      .then(res => {
        console.log('then',res.data)
        commit('SET_USER_PROFILE', res.data)
      })
      .catch(err => console.log(err.response.data))
    },

    followUser({commit, getters}, username){
      axios({
        method: 'post',
        url: djangourls.user.userProfileOrFollow(username),
        headers: getters.authHeader
      })
      .then(res => {
        commit('SET_USER_PROFILE', res.data)
      })
      .catch(err => console.log(err.response.data))
    },
  },

}
