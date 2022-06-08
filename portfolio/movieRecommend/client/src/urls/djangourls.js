const HOST = 'http://127.0.0.1:8000/'
const USERS = 'api/v1/users/'
const ACCOUNTS = 'api/v1/accounts/'
const COMMUNITY = 'api/v1/community/'


export default {
  admin: {  
    admin:() => HOST + 'admin/'
  },
  accounts:{
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    userProfileOrFollow: username => HOST + ACCOUNTS + 'profile/' + username,
  },
  movies:{

  },
  communities:{


  }
}
