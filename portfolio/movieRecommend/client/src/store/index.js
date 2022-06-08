import Vue from 'vue'
import Vuex from 'vuex'
import account from '@/store/modules/account'
import community from '@/store/modules/community'
import movie from '@/store/modules/movie'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    account,
    community,
    movie
  }
})
