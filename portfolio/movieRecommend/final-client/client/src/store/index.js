import Vue from 'vue'
import Vuex from 'vuex'
import accounts from './modules/accounts'
import communities from './modules/communities'
import movies from './modules/movies'
Vue.use(Vuex)

export default new Vuex.Store({
  modules:{
    accounts,
    communities,
    movies,
  }

})