<html>
<head>
%include _mod_header.tpl
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
    <form name="ban_{{ban.id}}" action="{{url('mod_ban_submit')}}" method="POST">
    <input type="hidden" name="ban_id" value="{{ban.id}}">
    <tr class="ban_row {{'active' if ban.is_active else 'expired'}}">
      <td>{{ban.ip_address}}</td>
      <td>{{ban.ban_start}}</td>
      <td>{{ban.ban_expire if ban.ban_expire else "never"}}</td>
      <td>
        %if ban.is_active:
        <input type="submit" name="delete" value="X" class="button-lite"></td>
        %end
        &nbsp;
    </tr>
    </form>
    %end
  </table>
</body>
</html>

