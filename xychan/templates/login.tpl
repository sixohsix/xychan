<html>
<head>
%include _header.tpl
  <title>Login</title>
</head>
<body>
  <h1>Login</h1>
  <form name="login" method="POST" action="{{url('login_submit')}}">
    <input type="text" name="username" value="">
    <input type="password" name="password" value="">
    <input type="submit" type="button" class="button" value="login!">
  </form>
</body>
</html>
