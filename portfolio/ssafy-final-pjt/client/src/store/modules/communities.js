import router from '@/router'
import djangourl from '@/urls/djangourl'
import axios from 'axios'
import _ from 'lodash'

export default {
  state: {
    community: [],
    article: {},
    articleAndCommentError: null,
  },
  getters: {
    community(state) {
      return state.community
    },
    article(state) {
      return state.article
    },
    isAuthor(state, getters) {
      return state.article.user?.username === getters.currentUser.username
    },
    isArticle(state) {
      return !_.isEmpty(state.article)
    },
    articleAndCommentError(state){
      return state.articleAndCommentError
    }

  },
  mutations: {
    //XXX_SET이라고 하면 XXX의 집합이라고 받아들여질 수 있으므로 예외적으로 동사 앞에 둠
    SET_COMMUNITY(state, community){
      state.community = community
    },
    SET_ARTICLE(state, article){
      state.article = article
    },
    SET_ARTICLE_COMMENTS(state, comments){
      state.article.comments = comments
    },
    SET_ARTICLE_AND_COMMENT_ERROR(state, error){
      state.articleAndCommentError = error
    },
  },
  actions: {
    communityGet({commit, getters}){
      axios({
        method:'get',
        url: djangourl.communities.community(),
        headers: getters.authHeader
      })
      .then(res =>{
        commit('SET_COMMUNITY', res.data)
      })
      .catch(err => console.error(err.response))
    },

    articleGet({commit, getters}, articlePk){
      axios({
        method:'get',
        url: djangourl.communities.article(articlePk),
        headers: getters.authHeader
      })
      .then(res =>{
        commit('SET_ARTICLE', res.data)
      })
      .catch(err => {
        if(err.response.status === 404){
          router.push({name: 'NotFound404'})
        }
      })
    },

    articleCreate({commit, getters}, article){
      axios({
        //이 단계에서는 db에 생성한 게시글 저장?
        method:'post',
        url: djangourl.communities.community(),
        data: article,
        headers: getters.authHeader
      })
      .then(res => {
        //이 단계에서는 res로 받은 데이터를 활용해 화면에 보여줄 게시물 화면 구성? article에 새롭게 만든 게시글 객체가 담김
        commit('SET_ARTICLE', res.data)
        router.push({
          name:'article',
          params: {
            articlePk: getters.article.pk
          }
        })
      })
      .catch(err => {
        commit('SET_ARTICLE_AND_COMMENT_ERROR', err.response.data)
        console.error(err.response)})
    },

    articleUpdate({commit, getters}, {pk, title, content}){
      axios({
        method: 'put',
        url: djangourl.communities.article(pk),
        data: {title, content,},
        headers: getters.authHeader
      })
      .then(res => {
        commit('SET_ARTICLE', res.data)
        router.push({
          name:'article',
          params: {
            articlePk: getters.article.pk
          }
        })
      })
      .catch(err => {
        commit('SET_ARTICLE_AND_COMMENT_ERROR', err.response.data)
        console.error(err.response)})
    },

    articleDelete({commit,getters}, articlePk){
      if(confirm(`<${getters.article.title}> 해당 게시글을 정말로 삭제하시겠습니까?`)) {
        axios({
          method: 'delete',
          url: djangourl.communities.article(articlePk),
          headers: getters.authHeader
        })
        .then(() => {
          commit('SET_ARTICLE', {})
          router.push({name: 'community'})
        })
        .catch(err => console.error(err.response))
      }
    },

    commentGet({commit, getters}, articlePk){
      axios({
        method:'get',
        url: djangourl.communities.article(articlePk),
        headers: getters.authHeader
      })
      .then(res =>{
        commit('SET_ARTICLE', res.data)
      })
    },

    commentCreate({commit, getters}, {articlePk, content}){
      axios({
        method:'post',
        url: djangourl.communities.commentCreate(articlePk),
        data: {content,},
        headers: getters.authHeader
      })
      .then(res => commit('SET_ARTICLE_COMMENTS', res.data))
      .catch(err => {
        commit('SET_ARTICLE_AND_COMMENT_ERROR', err.response.data)
        console.error(err.response)})
    },

    commentUpdate({commit, getters}, {articlePk, commentPk, content}){
      axios({
        method:'put',
        url: djangourl.communities.commentUpdateDelete(articlePk, commentPk),
        headers: getters.authHeader,
        data:{content,}
      })
      .then(res => commit('SET_ARTICLE_COMMENTS', res.data))
      .catch(err => {
        commit('SET_ARTICLE_AND_COMMENT_ERROR', err.response.data)
        console.error(err.response)})

    },

    commentDelete({commit, getters}, {articlePk, commentPk}){
      if(confirm('정말로 해당 댓글을 삭제하시겠습니까?')){
        console.log('here',{articlePk, commentPk})
        axios({
          method:'DELETE',
          url: djangourl.communities.commentUpdateDelete(articlePk, commentPk),
          headers: getters.authHeader,
          data: {},
        })
        .then(res => commit('SET_ARTICLE_COMMENTS', res.data))
        .catch(err => console.error(err.response))

      }
    },

    articleLike({ commit, getters }, articlePk) {
      axios({
        method: 'post',
        url: djangourl.communities.articleLike(articlePk),
        headers: getters.authHeader,
      })
      .then(res => commit('SET_ARTICLE', res.data))
      .catch(err => console.error(err.response))
    },

    // commentLike({ commit, getters }, {articlePk, commentPk}) {
    //   axios({
    //     url: djangourl.articles.commentLike(articlePk, commentPk),
    //     method: 'post',
    //     headers: getters.authHeader,
    //   })
    //   .then(res => commit('SET_ARTICLE', res.data))
    //   .catch(err => console.error(err.response))
    // },
  },

}
