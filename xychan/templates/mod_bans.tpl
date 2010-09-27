<html>
<head>
%include _header.tpl
<link rel="stylesheet" type="text/css" href="{{url('static', file='mod_style.css')}}" />
  <title>Moderate bans</title>
</head>
<body>
  <h1>Moderate bans</h1>
  <table class="bans">
    <tr>
      <th>IP Address</th>
      <th>Ban Started</th>
      <th>Ban Expires</th>
      <th>&nbsp;</th>
    </tr>
    %for ban in bans:
    <form name="ban_{{ban.id}}" action="#" method="POST">
    <input type="hidden" name="ban_id" value="{{ban.id}}">
    <tr>
      <td>{{ban.ip_address}}</td>
      <td>{{ban.ban_start}}</td>
      <td>{{ban.ban_expire if ban.ban_expire else "never"}}</td>
      <td><input type="submit" name="delete" value="X" class="button-lite"></td>
    </tr>
    </form>
    %end
  </table>
</body>
</html>

