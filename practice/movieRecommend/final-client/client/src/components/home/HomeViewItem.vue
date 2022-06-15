<template>
  <div id="HomeViewItem" @click="goToMovieDetail" >
    <div class="cards">
      <figure class="card m-4">
        <img :src="poster">
        <figcaption><strong>{{movie.title}}</strong></figcaption>
      </figure>
    </div>
    <!-- <b-carousel-slide :img-src="poster" style="width:450px;"></b-carousel-slide> -->
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

  export default {
    name:"HomeViewItem",
    props:{ movie:Object },
    methods:{
      goToMovieDetail(){
        this.$router.push({name: 'moviesDetail', params:{ movieId: this.movie.id }})
        console.log('goToMovieDetail')
        console.log(this.movie.id)
      }
    },
    computed:{
      ...mapGetters(['movie_detail', 'articleAndCommentError']),
      poster(){
        return `https://image.tmdb.org/t/p/original`+`${this.movie.poster_path}`
      }
    },
    created(){
    }
  }
</script>

<style scoped>
.movieimg {
  height: auto;
  width:10vw;
}

/*제목 반짝*/
.abs,
.cards .card figcaption,
.cards .card:after,
.news .card figcaption,
.news .card:after,
.news .article figcaption {
  position: absolute;
}

.fix {
  position: fixed;
}
.dfix {
  display: inline;
}
.dib {
  display: inline-block;
}
.db {
  display: block;
}
.dn {
  display: none;
}
.df,
.cards,
.news {
  display: grid;
}
.dif {
  display: inline-flex;
}
.dg {
  display: grid;
}
.dig {
  display: inline-grid;
}
.vm {
  vertical-align: middle;
}

.news .card {
  margin: 2px;
  width: 180px;
  height: 270px;
  overflow: hidden;
  box-shadow: 0 5px 10px rgba(0,0,0,0.8);
  transform-origin: center top;
  transform-style: preserve-3d;
  transform: translateZ(0);
  transition: 0.3s;
}

.card img,
.news .card img {
  width: 100%;
  min-height: 100%;
}

.cards .card figcaption,
.news .card figcaption {
  bottom: 0;
  left: 0;
  right: 0;
  padding: 20px;
  padding-bottom: 10px;
  font-size: 20px;
  background: none;
  color: #fff;
  transform: translateY(100%);
  transition: 0.3s;
}
.cards .card:after,
.news .card:after {
  content: '';
  z-index: 10;
  width: 200%;
  height: 100%;
  top: -90%;
  left: -20px;
  opacity: 0.1;
  transform: rotate(45deg);
  background: linear-gradient(to top, transparent, #fff 15%, rgba(255,255,255,0.5));
  transition: 0.3s;
}
.cards .card:hover,
.news .card:hover,
.cards .card:focus,
.news .card:focus,
.cards .card:active,
.news .card:active {
  box-shadow: 0 8px 16px 3px rgba(0,0,0,0.6);
  transform: translateY(-3px) scale(1.05) rotateX(15deg);
}
.cards .card:hover figcaption,
.news .card:hover figcaption,
.cards .card:focus figcaption,
.news .card:focus figcaption,
.cards .card:active figcaption,
.news .card:active figcaption {
  transform: none;
}
.cards .card:hover:after,
.news .card:hover:after,
.cards .card:focus:after,
.news .card:focus:after,
.cards .card:active:after,
.news .card:active:after {
  transform: rotate(25deg);
  top: -40%;
  opacity: 0.15;
}

</style>