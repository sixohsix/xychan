<html>
<head>
%include _header.tpl
  <title>Login</title>
</head>
<body>
  %if c.user:
  <h1>Logout</h1>
    <p>You are logged in as {{c.user.username}}.</p>
    <form name="logout" method="POST" action="{{url('logout_submit')}}">
      <input type="submit" class="button" name="logout" value="Logout!">
    </form>
  %else:
  <h1>Login</h1>
  <form name="login" method="POST" action="{{url('login_submit')}}">
    <input type="text" name="username" value="">
    <input type="password" name="password" value="">
    <input type="submit" class="button" value="Login!">
  </form>
  %end
</body>
</html>
