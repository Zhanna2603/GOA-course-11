const checkAuth =()=>{
    const user =localStorage.getItem('user');
    if (user){
      loggedInUser = user;
      showDashboard();
    } 
    else{
      showAuth();
    }
};
const showAuth =()=>{
    loginSection.style.display = 'none';
    dashboard.style.display = 'none';
};
const showDashboard =()=>{
    loginSection.style.display = 'none';
    dashboard.style.display = 'none';
};