<template>
  <div id="communityView">
    <h1 id="community-title">Community🖊️</h1>
    <router-link :to="{ name:'articleCreate' }">
      <b-button id="create-button" class="m-3">새 글 작성 <b-icon icon="pencil"></b-icon></b-button> 
    </router-link>

    <b-table id="community-table" 
      :per-page="perPage" 
      :total-rows="rows"
      :current-page="currentPage"
      selectable
      hover
      :items="community" 
      :fields="fields"
      @row-clicked="onRowClicked"
      primary-key="pk">
      <template #cell(created_at)="data">
        {{data.item.created_at.substring(0,10)}}
      </template>
    </b-table>
    
    <div id="community-pagination" class="m-3">
      <b-pagination 
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        aria-controls="community-table">
      </b-pagination>
    </div>

  </div>
</template>

<script>

import {mapGetters, mapActions} from 'vuex'

export default {
  name: 'CommunityView',
  data(){
    return {
      currentPage: 1,
      perPage: 5,
      fields: [{key: 'pk',label: '번호'},
      {key: 'user.username',label: '작성자'},
      {key: 'title',label: '제목'},
      {key: 'created_at', label: '작성일'},
      ]
    }
  },
  methods:{
    ...mapActions(['communityGet', 'articleGet']),
    onRowClicked(item){
      console.log(item.pk)
      this.$router.push({ name: 'article', params: { articlePk: item.pk } })
    }
  },
  computed: {
    ...mapGetters(['community']),
    rows() {
      return this.community.length
    }
  },
  created(){
    this.communityGet()
  }

}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Merriweather&family=Oleo+Script&display=swap');

#create-button{
  background-color: #3282B8;
  float: right;
  
}

#community-table{
  color: #112D4E;
  border-style: solid;
  border: 3px solid #112D4E;
  border-color: #112D4E;
  background-color: #F9F7F7;
  font-family: 'Gowun Dodum', sans-serif;
}

#community-pagination{
  display: inline-block;
}

#community-title{
  font-family: 'Merriweather', serif;
  font-family: 'Oleo Script', cursive;
  color: #112D4E;
}

</style>
