function toggleLogin() {
    var login = document.querySelector('.floating-login');
    if (login.style.display === 'none') {
      login.style.display = 'block';
    } else {
      login.style.display = 'none';
    }
  }