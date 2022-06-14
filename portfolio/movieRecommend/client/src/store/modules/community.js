import router from '@/router'
import djangourls from '@/urls/djangourls'
import axios from 'axios'
import _ from 'lodash'

export default {
  state: {
    articleList: [],
    article: {},
  },
  getters: {
    articleList: state => state.articleList,
    article: state => state.article,
    isArticleAuthor: state => state.article.user?.username === getters.currentUser.user.username,
    isArticle: state => !_.isEmpty(state.Article),
  },
  mutations: {
    SET_ARTICLE_LIST: (state, articleList) => state.articleList = articleList,
    SET_ARTICLE: (state, article) => state.article = article,
    SET_ARTICLE_COMMENTS: (state, comments) => (state.article.comments = comments),
  },
  actions: {
    setArticleLlist({getters, commit}) {
      axios({
        method: 'get',
        url: djangourls.community.readOrCreateArticles(),
        headers: getters.authHeader
      })
      .then(res => commit('SET_ARTICLE_LIST', res.data))
      .catch(err => console.error(err.response.data))
    },

    setArticle({getters, commit}, articlePk){
      axios({
        method: 'get',
        url: djangourls.community.detailOrUpdateOrDeleteArticle(articlePk),
        headers: getters.authHeader
      })
      .then(res => {
        commit('SET_ARTICLE', res.data)
      })
      .catch(err => {
        console.error(err.response.data)
        if (err.response.data === 404){
          router.push({name:'NotFound404'})
        }
      })    
    },

    createArticle({getters, commit}, articleInfo){
      axios({
        method: 'post',
        url: djangourls.community.readOrCreateArticles(),
        data: articleInfo,
        headers: getters.authHeader,
      })
      .then(res => {
        commit('SET_ARTICLE', res.data)
        router.push({name:'ArticleView', params: { articlePk: getters.article.pk } })
      })
      .catch(err => console.error(err.response.data))   
    },

    updateArticle({getters, commit}, {articlePk, title, content}){
      axios({
        method: 'put',
        url: djangourls.community.detailOrUpdateOrDeleteArticle(articlePk),
        data: {title, content},
        headers: getters.authHeader,
      })
      .then(res => {
        commit('SET_ARTICLE', res.data)
        router.push({name:'ArticleView', params: { articlePk: getters.article.pk } })
      })
      .catch(err => console.error(err.response.data))   
    },

    deleteArticle({getters, commit}, articlePk){
      if (confirm('정말로 해당 게시글을 삭제하시겠습니까?')) {
        axios({
          method:'delete',
          url: djangourls.community.detailOrUpdateOrDeleteArticle(articlePk),
          headers: getters.authHeader,
        })
        .then(() => {
          commit('SET_ARTICLE', {})
          router.push({name: 'community'})
        })
        .catch(err => console.error(err.response.data))   
      }
    },

    likeArticle({getters, commit}, articlePk) {
      axios({
        method: 'post',
        url: djangourls.community.likeArticle(articlePk),
        headers: getters.authHeader,
      })
      .then(res =>  commit('SET_ARTICLE', res.data.data))
      .catch(err => console.error(err.response.data))   
    },

    createComment({getters, commit}, {articlePk, content}){
      const comment = {content}
      axios({
        method:'post',
        url: djangourls.community.createComment(articlePk),
        headers: getters.authHeader,
        data: comment
      })
      .then(res=> commit('SET_ARTICLE_COMMENTS', res.data))
      .catch(err => console.error(err.response.data))   
    },

    updateComment({getters, commit}, {articlePk, commentPk, content}){
      const comment = {content}
      axios({
        method:'put',
        url: djangourls.community.updateOrDeleteComment(articlePk, commentPk),
        headers: getters.authHeader,
        data: comment
      })
      .then(res => commit('SET_ARTICLE_COMMENTS', res.data))
      .catch(err => console.error(err.response.data))   
    },

    deleteComment({getters, commit}, {articlePk, commentPk}){
      if (confirm('정말로 해당 댓글을 삭제하시겠습니까?')) {
        axios({
          method:'delete',
          url: djangourls.community.updateOrDeleteComment(articlePk, commentPk),
          headers: getters.authHeader,
        })
        .then(res => commit('SET_ARTICLE_COMMENTS', res.data))
        .catch(err => console.error(err.response.data))   
      }
    },

    likeComment({getters, commit}, {articlePk, commentPk}){
      axios({
        method: 'post',
        url: djangourls.community.likeComment(articlePk, commentPk),
        headers: getters.authHeader
      })
      .then(res => commit('SET_ARTICLE_COMMENTS', res.data))
      .catch(err => console.error(err.response.data))   
    },
  },
}
