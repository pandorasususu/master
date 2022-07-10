<template>
  <div class="container home">
    <h1 id="title">Top Rated 🏆</h1>
    <!--top rated-->
    <div id="carouselDiv1">
      <carousel
        id="carousel-toprated"
        class="mx-4 mb-8"
        :interval="4000"
        :paginationEnabled="false"
        :perPage="7"
        :minSwipeDistance="3"
        :navigationEnabled="true"
        :perPageCustom="[
          [768, 4],
          [1024, 5],
          [1240, 6],
          [1520, 7],
        ]"
      >
        <slide v-for="movie in movieListHomeView" :key="movie.id">
          <home-view-item :movie="movie"></home-view-item>
        </slide>
      </carousel>
    </div>
    <br />
    <!--popular-->
    <div id="carouselDiv2">
      <h1 id="title">Popular 👑</h1>
      <carousel
        id="carousel-popular"
        class="mx-4 mb-8"
        :interval="4000"
        :paginationEnabled="false"
        :perPage="7"
        :minSwipeDistance="3"
        :navigationEnabled="true"
        :perPageCustom="[
          [768, 4],
          [1024, 5],
          [1240, 6],
          [1520, 7],
        ]"
      >
        <slide v-for="movie in movieListHomeView2" :key="movie.id">
          <home-view-item :movie="movie"></home-view-item>
        </slide>
      </carousel>
    </div>
    <br />
    <!--recent-->
    <div id="carouselDiv3">
      <h1 id="title">New ✨</h1>
      <carousel
        id="carousel-recent"
        class="mx-4 mb-8"
        :interval="4000"
        :paginationEnabled="false"
        :perPage="7"
        :minSwipeDistance="3"
        :navigationEnabled="true"
        :perPageCustom="[
          [768, 4],
          [1024, 5],
          [1240, 6],
          [1520, 7],
        ]"
      >
        <slide v-for="movie in movieListHomeView3" :key="movie.id">
          <home-view-item :movie="movie"></home-view-item>
        </slide>
      </carousel>
    </div>
  </div>
</template>

<script>
import HomeViewItem from "@/components/home/HomeViewItem.vue";
import { mapActions, mapGetters } from "vuex";

export default {
  name: "HomeView",
  components: {
    HomeViewItem,
  },
  data() {
    return {
      swtich: false,
      secondTime: 4000,
      slide: 0,
      sliding: null,
    };
  },
  methods: {
    ...mapActions([
      "movieListHomeViewGet",
      "movieListHomeViewGet2",
      "movieListHomeViewGet3",
    ]),
    onSlideStart() {
      this.sliding = true;
    },
    onSlideEnd() {
      this.sliding = false;
    },
    // click이벤트 발생시, switch의 boolean값을 바꾸어, true일 경우에는 자동 바꿈이 8초 간격으로 활성화, false인 경우에는 비활성화
    changeSwitching() {
      this.swtich = !this.swtich;
      if (this.swtich) {
        this.secondTime = 0;
      } else {
        this.secondTime = 4000;
      }
    },
  },
  computed: {
    ...mapGetters([
      "movieListHomeView",
      "movieListHomeView2",
      "movieListHomeView3",
    ]),
  },
  created() {},
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Merriweather&family=Oleo+Script&display=swap");

.home {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

#title {
  font-family: "Merriweather", serif;
  font-family: "Oleo Script", cursive;
}
</style>
