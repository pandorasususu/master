const HOST = 'http://localhost:8000/'
const MOVIE = 'movies/'
const ACCOUNTS = 'accounts/'
// const COMMUNITY = 'community/'
//기존 django에 맞춰서, 원래는 community
const COMMUNITY = 'community/'

export default {
  admin: {  
    admin:() => HOST + 'admin/'
  },
  accounts:{
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    userProfile: username => HOST + ACCOUNTS + 'profile/' + username,
    // userDelete: username => HOST + ACCOUNTS + 'profile/' + username + '/delete/',
    userFollow: username => HOST + ACCOUNTS + 'profile/' + username + '/follow/',
  },
  movies:{
    random: () => HOST + MOVIE + 'random/',
    list: () => HOST + MOVIE + 'list/',
    recommend: (username) => HOST + MOVIE + `recommend/${username}/`,
    detail: (movie_pk) => HOST + MOVIE + `${movie_pk}`,
    save: (movie_pk) => HOST + MOVIE + `${movie_pk}/save/`,
    rating: (movie_pk, username) => HOST + MOVIE + `${movie_pk}/rating/${username}/`,
  },
  communities:{
    community: () => HOST + COMMUNITY,
    article: articlePk => HOST + COMMUNITY + `${articlePk}/`,
    articleLike: articlePk => HOST + COMMUNITY + `${articlePk}/` + 'like/',
    commentCreate: articlePk => HOST + COMMUNITY + `${articlePk}/` + 'comments/',
    commentUpdateDelete: (articlePk, commentPk) => HOST + COMMUNITY + `${articlePk}/comments/${commentPk}/`,
    commentLike: (articlePk, commentPk) => HOST + COMMUNITY + `${articlePk}/${commentPk}/` + 'like/',

  }
}