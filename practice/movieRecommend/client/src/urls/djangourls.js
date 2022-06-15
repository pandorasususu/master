const HOST = 'http://127.0.0.1:8000/'
const USERS = 'api/v1/users/'
const MOVIES = 'api/v1/movies/'
const ACCOUNTS = 'api/v1/accounts/'
const COMMUNITY = 'api/v1/community/'


export default {
  admin: {  
    admin:() => HOST + 'admin/'
  },
  account:{
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
  },
  movie:{
    readOrCreateRating: (movie_id) => HOST + MOVIES + `${movie_id}`,
    updateOrDeleteRating: (movie_id, rating_pk) => HOST + MOVIES + `${movie_id}/${rating_pk}/`,
    likeRating: (movie_id, rating_pk) => HOST + MOVIES + `${movie_id}/${rating_pk}/like/`
  },
  user:{
    userProfileOrFollow: username => HOST + USERS + 'profile/' + `${username}/`,
  },
  community:{
    readOrCreateArticles: () => HOST + COMMUNITY,
    detailOrUpdateOrDeleteArticle: (article_pk) => HOST + COMMUNITY + `${article_pk}`,
    likeArticle: (article_pk) => HOST + COMMUNITY + `${article_pk}/like/`,
    createComment: (article_pk) => HOST + COMMUNITY + `${article_pk}/comment/`,
    updateOrDeleteComment: (article_pk, comment_pk) => HOST + COMMUNITY + `${article_pk}/comment/${comment_pk}/`,
    likeComment: (article_pk, comment_pk) => HOST + COMMUNITY + `${article_pk}/comment/${comment_pk}/like/`,
  }
}
