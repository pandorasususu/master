<template>
  <!-- 전체장르 평점 보기, 평균평점, 평점개수 기준 목록 보여주는 건 나중에 -->
  <div id="MoviesView">
    <div id="MovieViewTop">
      <!-- 제목 -->
      <h1 id="movies-title">MOVIES FOR YOU 😍</h1>
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=Merriweather&display=swap" rel="stylesheet">
      <hr>

      <!-- Movie 페이지 설명 -->
      <div id="MoviesViewDescription">
        <ul>
          <p>기간을 설정해 영화를 검색할 수 있습니다.</p>
          <p>유저의 평점을 종합해 최고평균평점, 최다평점개수에 해당하는 장르의 영화들을 검색할 수 있습니다.</p>
        </ul>
      </div>
      <hr>
      <!-- 사용자 사용 기능 모음 -->
      <b-form id="movie-view-trending-search" >
        <label for="movie-view-datepicker">기간 선정</label>
        <b-form-datepicker id="movie-view-datepicker" v-model="trendingPayload.movieViewDate"></b-form-datepicker>
        <b-form-select
        id="movie-view-select"
        v-model="trendingPayload.afterOrBefore"
        :options="formOneSelectOne"
        required>
        </b-form-select>
      </b-form>
      <br>

      <div id="btn-group">
        <!-- 장르 통해 검색 -->
        <button id="btn1" @click.prevent="pushUserGenreLikeGet(); movieListTrendingByGenreControl('avg'); showMovieListTrending();">최고 평균 평점 장르 검색</button>
        <button id="btn2" @click.prevent="pushUserGenreLikeGet(); movieListTrendingByGenreControl('cnt'); showMovieListTrending();">최다 평점 개수 장르 검색</button>
      </div>
      <b-button class="mt-3" variant="outline-danger" @click="resetAll">초기화</b-button>
      <hr>
      <div>
        <h5>🌟 최고 평균평점 장르: {{userGenreLike.genre_list_rating_avg.name}}, {{userGenreLike.genre_list_rating_avg.rating_avg}}점ㅤ  ㅤ🏅최다 평점개수 장르: {{userGenreLike.genre_list_rating_count.name}}, {{userGenreLike.genre_list_rating_count.rating_count}}개</h5>
      </div>
    </div>

    <br>

    <div id="MovieViewBody">

    

      <!-- 흥행 영화 목록 -->
      <div v-if="MovieListTrendingSwitch">
        <b-table 
        id="movie-list-trending-by-genre-table" 
        :per-page="perPage" 
        :total-rows="MovieListTrendingRows"
        :current-page="currentPage"
        hover 
        label-sort-clear=""
        label-sort-asc=""
        label-sort-desc=""
        :items="movieListTrending" 
        @row-clicked="MovieListTrendingOnRowClicked"
        :fields="MovieListTrendingFields">
        </b-table>

        <b-pagination
        id="movie-list-trending-table-pagination"
        v-model="currentPage"
        :total-rows="MovieListTrendingRows"
        :per-page="perPage"
        aria-controls="movie-list-trending-table">
        </b-pagination>
      </div>
    </div>

  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'

export default {
  name: 'MoviesView',
  data(){
    return {
      showFormOne: false,
      showFormTwo: false,
      showFormThree: false,

      formOneSelectOne: [
        {text: '이후의 영화들', value: 'gte'},
        {text: '이전의 영화들', value: 'lte'},
      ],
      movieViewDate: '',
      afterOrBefore: '',
      trendingPayload: {
        with_genres: null,
        movieViewDate: this.movieViewDate,
        afterOrBefore: this.afterOrBefore,
      },
      MovieListTrendingFields: [
        {key: 'title', label: '영화 제목'},
        {key: 'release_date', label:'개봉일', sortable:true},
        {key: 'vote_average', label:'평균 평점', sortable:true},

        {key: 'genre_ids', thClass: 'd-none', tdClass: 'd-none'},
        {key: 'adult', thClass: 'd-none', tdClass: 'd-none'},
        {key: 'backdrop_path', thClass: 'd-none', tdClass: 'd-none'},
        {key: 'id', thClass: 'd-none', tdClass: 'd-none'},
        {key: 'media_type', thClass: 'd-none', tdClass: 'd-none'},
        {key: 'original_language', thClass: 'd-none', tdClass: 'd-none'},
        {key: 'original_title', thClass: 'd-none', tdClass: 'd-none'},
        {key: 'overview', thClass: 'd-none', tdClass: 'd-none'},
        {key: 'popularity', thClass: 'd-none', tdClass: 'd-none'},
        {key: 'poster_path', thClass: 'd-none', tdClass: 'd-none'},
        {key: 'video', thClass: 'd-none', tdClass: 'd-none'},
        {key: 'vote_count', thClass: 'd-none', tdClass: 'd-none'},

      ],
      currentPage: 1,
      perPage: 10,
      genreField: [
        {key: 'name', label: '장르'},
        {key: 'rating_count', label: '평가한 영화 개수', sortable:true},
        {key: 'rating_avg', label: '평균평점', sortable:true},
        {key: 'rating_total', thClass: 'd-none', tdClass: 'd-none'},
      ],
      genreListAllSwitch: false,
      MovieListTrendingSwitch: false,
      ratingAvgFiveSwitch: false,
      ratingCountFiveSwitch: false,
    }
  },
  methods:{
    ...mapActions(['movieListTrendingGet', 'getTMDBMovieDetail', 'userGenreLikeGet']),
    formOne(){
      this.showFormOne = !this.showFormOne
    },
    showMovieListTrending(){
      this.MovieListTrendingSwitch = !this.MovieListTrendingSwitch
    },
    showGenreList(){
      this.genreListAllSwitch = !this.genreListAllSwitch
      this.ratingAvgFiveSwitch = false
      this.MovieListTrendingSwitch = false
      this.ratingCountFiveSwitch = false
    },
    MovieListTrendingOnRowClicked(item){
      this.$router.push({name:'moviesDetail', params: {movieId : item.id}})
      console.log(item.poster_path)
    },
    // 여기서 현재 로그인 된 유저의 장르 평점 정보 가져옴
    pushUserGenreLikeGet(){
      this.userGenreLikeGet({username: this.currentUser.username})
    },
    showRatingAvgFive() { 
      this.ratingAvgFiveSwitch = !this.ratingAvgFiveSwitch 
      this.genreListAllSwitch = false
      this.ratingCountFiveSwitch = false
      this.MovieListTrendingSwitch = false
    },
    showRatingCountFive() { 
      this.ratingCountFiveSwitch = !this.ratingCountFiveSwitch 
      this.genreListAllSwitch = false
      this.ratingAvgFiveSwitch = false
      this.MovieListTrendingSwitch = false
    },
    movieListTrendingByGenreControl(param){
      this.genreListAllSwitch = false
      this.ratingAvgFiveSwitch = false
      this.ratingCountFiveSwitch = false
      console.log('movieListTrendingByGenreControl 실행은 됨')
      if ( param === 'avg') {
        const ratingAvgFiveGenreList = []
        for (const[key, value] of Object.entries(this.userGenreLike.genre_list_rating_avg)) {
          console.log([key, value])
          if (key === 'id') { ratingAvgFiveGenreList.push(value) }
        }
        console.log('ratingAvgFiveGenreList', ratingAvgFiveGenreList)
        this.trendingPayload.with_genres = ratingAvgFiveGenreList.toString()
        this.movieListTrendingGet(this.trendingPayload)
      } else if (param === 'cnt' ) {
        const ratingCountFiveGenreList = []
        for (const[key, value] of Object.entries(this.userGenreLike.genre_list_rating_count)) {
          console.log([key, value])
          if (key === 'id') { ratingCountFiveGenreList.push(value) }
        }        
        console.log('ratingCountFiveGenreList', ratingCountFiveGenreList)
        this.trendingPayload.with_genres = ratingCountFiveGenreList.toString()
        this.movieListTrendingGet(this.trendingPayload)
      } else { 
        console.log('nowtrending 아래 검색 버튼 눌러서 에러')
        }
    },
    resetAll(){
      this.trendingPayload.movieViewDate = ''
      this.trendingPayload.afterOrBefore = ''
      this.MovieListTrendingSwitch = false
    },
  },
  computed:{
    ...mapGetters(['movieListTrending', 'genreList', 'userGenreLike','currentUser']),
    MovieListTrendingRows(){
      return this.movieListTrending.length
    },
  },
  created(){
      this.userGenreLikeGet({username: this.currentUser.username})
  },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Merriweather&family=Oleo+Script&display=swap');

#MoviesView {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  font-family: 'Gowun Dodum', sans-serif;
}

#MovieViewTop{
  width: 100%;
}

#movie-view-trending-search{
  width: 50%;
  height: 40px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  margin-bottom: 40px;
}

#movie-view-rating-buttons {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: center;
}


form label, form select {
  height: 100%;
  margin-left: 10px;
  margin-right: 10px;
}

#movie-person-select, #day-week-select{
  background-color: #dde6ea;;
}

#movie-list-trending-table-pagination{
  display: flex;
  flex-direction: row;
  justify-content: center;
}

#movie-list-trending-table{
  background-color: #646466;
  color: #bac6cb;
}

#movie-view-trending-search{
  margin: auto;
}

#movies-title{
  font-family: 'Gowun Dodum', sans-serif;
  font-family: 'Merriweather', serif;
  font-family: 'Oleo Script', cursive;
  color: #112D4E;
}

#btn1{
  border-top-left-radius: 5px;
  border-bottom-left-radius: 5px;
  margin-right:-4px;
  width: 25%;
}

#btn2{
  border-top-right-radius: 5px;
  border-bottom-right-radius: 5px;    
  margin-left:-3px;
  width: 25%;
}

#btn-group button{
  border: 1px solid #3282B8;
  color: #3282B8;
  text-decoration: bold;
  padding: 5px;
  font-weight: bold;
}
#btn-group button:hover{
  color: white;
  background-color: #3282B8;
}
</style>