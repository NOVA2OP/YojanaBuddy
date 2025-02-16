function login() {
  let username = document.getElementById("login-username").value;
  let password = document.getElementById("login-password").value;

  fetch("/accounts/login_api/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username: username, password: password }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.message) {
        window.location.href = data.redirect_url; // Redirect to chatbot
      } else {
        alert("Invalid credentials");
      }
    });
}

function signup() {
  let username = document.getElementById("signup-username").value;
  let email = document.getElementById("signup-email").value;
  let password = document.getElementById("signup-password").value;

  fetch("/accounts/signup_api/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      username: username,
      email: email,
      password: password,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      alert(data.message || data.error);
      if (data.message) {
        window.location.href = "/accounts/login/";
      }
    });
}
