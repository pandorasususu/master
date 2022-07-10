<template>
  <div id="MoviesDetail">
    <div class="container">
      <div id="movie-detail-img" class="m-5">
        <img :src="poster" alt="">
      </div>

      <div id="movie-detail-description">
        <h2 id="movie-title" style="text-align: center; font-weight: bold;">{{movie_tmdb_detail.title}}</h2>
        <hr>
        <div class="movie-info">
          <div id="date-div">
            <p>개봉일: &nbsp; {{movie_tmdb_detail.release_date}} </p>
          </div> 

          <div id="genre-div">
            장르: &nbsp;
            <p v-for="genre in movie_tmdb_detail.genres" :key="genre.id" :genre="genre">
              <span> {{genre.name}}, </span>&nbsp;&nbsp;
            </p>
          </div>

          <div id="company-div">
            제작사: &nbsp;
            <p v-for="company in movie_tmdb_detail.production_companies" :key="company.id" :comapny="company">
              <span>{{ company.name }}, </span>&nbsp;&nbsp;
            </p>
          </div>

          <div id="country-div">
            제작국가: &nbsp;
            <p v-for="country in movie_tmdb_detail.production_countries" :key="country.id" :country="country">
              <span>{{ country.name }},</span>&nbsp;&nbsp;
            </p>
          </div>
        </div>
      <hr>

      <div id="overview-div">
        <p>{{movie_tmdb_detail.overview}} </p>
      </div>
      <hr>

      <div id="movie-info2">
        <div id="movie-rate">
        <p>TMDB 평균 평점: &nbsp; {{movie_tmdb_detail.vote_average}} / 10점</p>
        <p>평균 평점: {{ratingAverage}}점 / 5점</p>
        <p>평가에 참여한 사람들: {{ratingCount}}명</p>
      </div>
      <hr>

      <div id="movie-rateform">
        <b-form id="movie-star-rating" @submit.prevent="saveScore();">
              <star-rating
          :star-size="40"
          v-model="boundRating"
          :increment="0.5"
          :glow="1.5"
          :fixed-points="1">
          </star-rating>
          <b-button type="submit" variant="secondary" 
          title="이미 별점을 등록하셨어도 다시 등록하시면 기존의 별점이 수정됩니다.">
            별점 등록</b-button>
        </b-form>
        <div v-if="movie_server_detail.already_rated">
            내 점수: {{userRateGet}} 점 / 5점
          </div>
        </div>
      </div>
      <hr>
    </div>
  </div>

  </div>
</template>

<script>
import StarRating from 'vue-star-rating'
import {mapActions, mapGetters} from 'vuex'

export default {
  name: 'MoviesDetail',
  components:{ StarRating },
  data(){
    return{
      boundRating:0,
    }
  },
  methods:{
    ...mapActions(['getTMDBMovieDetail', 'getServerMovieDetail', 'ratingMovieUpdate','ratingScorePost',]),
    saveScore(){
      const genreList = this.movie_tmdb_detail.genres.map(e=>e.id).toString()

      const ratingPayload = {
        username: this.currentUser.username,
        movie_pk: this.$route.params.movieId,
        score: this.boundRating,
        genre_ids: genreList,
      }
      this.ratingScorePost(ratingPayload)
      this.$store.dispatch('getServerMovieDetail', this.$route.params.movieId)
    },
  },
  computed:{
    ...mapGetters(['movie_tmdb_detail', 'movie_server_detail', 'articleAndCommentError','currentUser']),
    poster(){
      return `https://image.tmdb.org/t/p/original`+`${this.movie_tmdb_detail.poster_path}`
    },
    userRateGet(){
      return this.movie_server_detail.user_rate
    },
    ratingCount(){
      if (this.movie_server_detail){
        return this.movie_server_detail?.rated_user
      } else { return 0 }
    },
    ratingAverage(){
      if (this.ratingCount === 0){
        return 0
      } else { 
        const scoreAvg = this.movie_server_detail?.rating_avg?.score__avg 
        return scoreAvg?.toFixed(1)  
      }
    }
  },
  created(){
    const MovieId = parseInt(this.$route.params.movieId)
    this.getTMDBMovieDetail(MovieId)
    this.getServerMovieDetail(MovieId)
  }
}
</script>

<style scoped>

img{
  width: 400px;
  height: 600px
}

.container{
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

#movie-detail-description{
  color: #112D4E;
  margin-left: 20px;
  display: flex;
  flex-direction: column;
  justify-content: baseline;
}

#genre-div {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-content: center;
}

#date-div{
  width: 100%;
  display: flex;
  flex-direction: row;
  align-content: center;
}

#company-div{
  width: 100%;
  display: flex;
  flex-direction: row;
  align-content: center;
}

#country-div{
  width: 100%;
  display: flex;
  flex-direction: row;
  align-content: center;  
}

#movie-star-rating{
  display: flex;
  flex-direction: row;
  width: 100%;
}

#movie-star-rating .vue-star-rating{
  margin-right: 20px;
}

.vue-star-rating-rating-text {
  width: 40px;
}

#overview-div{
  margin-top: 15px;
  width: 100%;
  display: flex;
  flex-direction: row;
  text-align: start;
}

#movie-star-rating{
  width: 50%;
  margin: auto;
}
</style>