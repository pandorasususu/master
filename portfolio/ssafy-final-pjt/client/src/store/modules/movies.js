import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import djangourl from '@/urls/djangourl'
Vue.use(Vuex)

const TMDB_API_KEY = '85b03cb96344fddee47b329076ffa046'
const TMDB_TOP_RATED_URL = 'https://api.themoviedb.org/3/movie/top_rated'
const TMDB_MOVIE_DISCOVER = 'https://api.themoviedb.org/3/discover/movie'
const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  state: {
    topRatedMovies: [],
    movieListTrending: [],
    genreList:[
      {
        "pk": 28,
        "fields": {
            "name": "액션"
        }
    },
    {
        "pk": 12,
        "fields": {
            "name": "모험"
        }
    },
    {
        "pk": 16,
        "fields": {
            "name": "애니메이션"
        }
    },
    {
        "pk": 35,
        "fields": {
            "name": "코미디"
        }
    },
    {
        "pk": 80,
        "fields": {
            "name": "범죄"
        }
    },
    {
        "pk": 99,
        "fields": {
            "name": "다큐멘터리"
        }
    },
    {
        "pk": 18,
        "fields": {
            "name": "드라마"
        }
    },
    {
        "pk": 10751,
        "fields": {
            "name": "가족"
        }
    },
    {
        "pk": 14,
        "fields": {
            "name": "판타지"
        }
    },
    {
        "pk": 36,
        "fields": {
            "name": "역사"
        }
    },
    {
        "pk": 27,
        "fields": {
            "name": "공포"
        }
    },
    {
        "pk": 10402,
        "fields": {
            "name": "음악"
        }
    },
    {
        "pk": 9648,
        "fields": {
            "name": "미스터리"
        }
    },
    {
        "pk": 10749,
        "fields": {
            "name": "로맨스"
        }
    },
    {
        "pk": 878,
        "fields": {
            "name": "SF"
        }
    },
    {
        "pk": 10770,
        "fields": {
            "name": "TV 영화"
        }
    },
    {
        "pk": 53,
        "fields": {
            "name": "스릴러"
        }
    },
    {
        "pk": 10752,
        "fields": {
            "name": "전쟁"
        }
    },
    {
        "pk": 37,
        "fields": {
            "name": "서부"
        }
    },
    ],
    movie_tmdb_detail: [],
    movie_server_detail: [],
    movieListHomeView: [],
    userGenreLike: null,
    movieListHomeView2: [],
    movieListHomeView3:[],
  },
  getters: {
    topRatedMovies: state => state.topRatedMovies,
    movieListTrending: state => state.movieListTrending,
    genreList: state => state.genreList,
    movie_tmdb_detail: state => state.movie_tmdb_detail,
    movie_server_detail: state => state.movie_server_detail,
    movieListHomeView: state => state.movieListHomeView,
    userGenreLike: state => state.userGenreLike,
    movieListHomeView2: state => state.movieListHomeView2,
    movieListHomeView3: state => state.movieListHomeView3,
  },
  mutations: {
    GET_TOP_RATED_MOVIES: (state, movies) => {
      state.topRatedMovies = movies
    },
    MOVIE_LIST_TRENDING_GET: (state, movies) => {
      console.log(movies)
      state.movieListTrending = movies
    },
    GET_TMDB_MOVIE_DETAIL: (state, movie_tmdb_detail) => {
      state.movie_tmdb_detail = movie_tmdb_detail
      console.log('GET_TMDB_MOVIE_DETAIL mutation에서 state.movie_tmdb_detail', state.movie_tmdb_detail)
    },
    GET_SERVER_MOVIE_DETAIL: (state, movie_server_detail) => {
      state.movie_server_detail = movie_server_detail
      console.log('GET_SERVER_MOVIE_DETAIL mutation에서 state.movie_server_detail', state.movie_server_detail)
    },

    MOVIE_LIST_HOME_VIEW_CREATE: (state, movieList) => {
      state.movieListHomeView = movieList
    },
    USER_GENRE_LIKE: (state, userGenreLike) => {
      console.log('USER_GENRE_LIKE mutation', userGenreLike)
      state.userGenreLike = userGenreLike
    },
    MOVIE_LIST_HOME_VIEW_CREATE2: (state, movieList) => {
      state.movieListHomeView2 = movieList
    },
    MOVIE_LIST_HOME_VIEW_CREATE3: (state, movieList) => {
      state.movieListHomeView3 = movieList
    },

  },
  actions: {
    // tmdb api 통해 첫 화면에 보여줄 영화들 가져오기
    getMoviesTopRated(context){
      axios({
        method:'get',
        url: TMDB_TOP_RATED_URL,
        params: {
          api_key: TMDB_API_KEY,
          language: 'ko-kr',
          page: 1
        }
      }).then(response =>{
        context.commit('GET_TOP_RATED_MOVIES', response.data)
      }).catch(error => {
        console.error(error)
      })
    },

    //TMDB API 통해 최근 관심을 끄는 영화들 가져오기
    movieListTrendingGet({commit}, {with_genres, movieViewDate, afterOrBefore}){    
      console.log('movieListTrendingGet',with_genres, movieViewDate, afterOrBefore)
      if (!with_genres) {
      axios({
        method:'get',
        url: `${TMDB_MOVIE_DISCOVER}?api_key=${TMDB_API_KEY}&language=ko-kr&region=KR&release_date.${afterOrBefore}=${movieViewDate}&sort_by=popularity.desc`
      })
      .then(res => {
        console.log('장르 선택 안하고')
        commit('MOVIE_LIST_TRENDING_GET', res.data.results)
      })
      .catch(error => {
        console.error(error.response)
      })} else {
        axios({
          method:'get',
          url: `${TMDB_MOVIE_DISCOVER}?api_key=${TMDB_API_KEY}&language=ko-kr&region=KR&release_date.${afterOrBefore}=${movieViewDate}&with_genres=${with_genres}&sort_by=popularity.desc`
        })
        .then(res => {
          console.log('장르 선택 하고')
          console.log(`${TMDB_MOVIE_DISCOVER}?api_key=${TMDB_API_KEY}&language=ko-kr&region=KR&release_date.${afterOrBefore}=${movieViewDate}&with_genres=${with_genres}&sort_by=popularity.desc`)
          commit('MOVIE_LIST_TRENDING_GET', res.data.results)
        })
        .catch(error => {
          console.error(error.response)
        })        
      }
      // console.log(with_genres)
      // if (!with_genres) {
      // axios({
      //   method:'get',
      //   url: `${TMDB_MOVIE_TRENDING}/movie/${dayOrWeek}?api_key=${TMDB_API_KEY}&language=ko-kr`
      // })
      // .then(res => {
      //   console.log('장르 선택 안하고')
      //   commit('MOVIE_LIST_TRENDING_GET', res.data.results)
      // })
      // .catch(error => {
      //   console.error(error.response)
      // })} else {
      //   axios({
      //     method:'get',
      //     url: `${TMDB_MOVIE_TRENDING}/movie/${dayOrWeek}?api_key=${TMDB_API_KEY}&language=ko-kr&with_genres=${with_genres}`
      //   })
      //   .then(res => {
      //     console.log('장르 선택 하고')
      //     commit('MOVIE_LIST_TRENDING_GET', res.data.results)
      //   })
      //   .catch(error => {
      //     console.error(error.response)
      //   })        
      // }
    },

    // 서버와 통신해서 첫 화면에 보여줄 영화들 가져오기
    movieListHomeViewGet({commit, getters}){
      axios({
        method:'get',
        url: `${SERVER_URL}/movies/toprated/`,
        headers: getters.authHeader
      }).then(response =>{
        commit('MOVIE_LIST_HOME_VIEW_CREATE', response.data)
      }).catch(error => {
        console.log('에러남')
        console.error(error.response)
      })

    },
    movieListHomeViewGet2({commit, getters}){
      axios({
        method:'get',
        url: `${SERVER_URL}/movies/popular/`,
        headers: getters.authHeader
      }).then(response =>{
        commit('MOVIE_LIST_HOME_VIEW_CREATE2', response.data)
      }).catch(error => {
        console.error(error.response)
      })
    },
    movieListHomeViewGet3({commit, getters}){
      axios({
        method:'get',
        url: `${SERVER_URL}/movies/recent/`,
        headers: getters.authHeader
      }).then(response =>{
        commit('MOVIE_LIST_HOME_VIEW_CREATE3', response.data)
      }).catch(error => {
        console.error(error.response)
      })
    },

    getTMDBMovieDetail({commit, dispatch}, movieId){
      axios({
        method:'get',
        url: `https://api.themoviedb.org/3/movie/${movieId}`,
        params: {
          api_key: TMDB_API_KEY,
          language: 'ko-kr',
        }
      }).then(response =>{
        commit('GET_TMDB_MOVIE_DETAIL', response.data)
        const movie = response.data
        console.log('movie',movie)
        dispatch('saveMovie', {movie, movieId})
      }).catch(error => {
        console.log('getTMDBMovieDetail 에러남')
        console.error(error.response)
      })
    },

    saveMovie({getters}, {movie, movieId}){
      console.log('movie',movie.id)
      axios({
        method:'post',
        url: djangourl.movies.save(movieId),
        headers: getters.authHeader,
        data: {movie}
      }).then(res =>{
        console.log(res)
      }).catch(error => {
        console.log('saveMovie에서 에러남')
        console.error(error.response)
      })
    },

    getServerMovieDetail({commit, getters}, movieId){
      axios({
        method:'get',
        url: djangourl.movies.detail(movieId),
        headers: getters.authHeader,
      }).then(response =>{
        commit('GET_SERVER_MOVIE_DETAIL', response.data)
      }).catch(error => {
        console.log('getServerMovieDetail에서 에러남')
        console.error(error.response)
      })
    },

    ratingScorePost({getters}, {movie_pk, username, score, genre_ids}){
      console.log('ratingScorePost에서 받은 정보', movie_pk, username, score, genre_ids)
      console.log(typeof(genre_ids))
      axios({
        method:'post',
        url: djangourl.movies.rating(movie_pk, username),
        data: {score,genre_ids,},
        headers: getters.authHeader,
      }).then(response =>{
        console.log('ratingScorePost', response.data)
      }).catch(error => {
        console.log('ratingScorePost 에러남')
        console.error(error.response)
      })
    },

    userGenreLikeGet({getters, commit}, {username}){
      console.log('userGenreLikeGet 메서드 실행', username)
      axios({
        method: 'get',
        url: djangourl.movies.recommend(username),
        headers: getters.authHeader,
      })
      .then(res => {
        console.log('userGenreLikeGet', res.data)
        commit('USER_GENRE_LIKE', res.data)
      })
      .catch(error => {
        console.log('userGenreLike 에러남')
        console.error(error.response)
      })
    }

  },
}
