<html>
<head>
%include _mod_header.tpl
  <title>Moderate boards</title>
</head>
<body>
  <h1>Boards</h1>
  <table class="pt">
    <tr>
      <th>Board ID</th>
      <th>Short Name</th>
      <th>Long Name</th>
      <th>Locked</th>
      <th>Hidden</th>
    </tr>
    %for board in boards:
    <tr>
      <td>{{board.id}}</td>
      <td>{{board.short_name}}</td>
      <td>{{board.long_name}}</td>
      %if board.locked:
      <td>Locked [<a href="{{url('mod_lock', board_name=board.short_name)}}?state=unlock">Unlock</a>]</td>
      %else:
      <td>Unlocked [<a href="{{url('mod_lock', board_name=board.short_name)}}?state=lock">Lock</a>]</td>
      %end
      %if board.hidden:
      <td>Hidden [<a href="{{url('mod_hide', board_name=board.short_name)}}?state=make_visible">Make visible</a>]</td>
      %else:
      <td>Visible [<a href="{{url('mod_hide', board_name=board.short_name)}}?state=hide">Hide</a>]</td>
      %end
    </tr>
    %end
  </table>
<h2>Create a new board</h2>
<form id="new_board" action="{{url('mod_create_board')}}" method="POST">
  <label for="short_name">Short Name</label>
  /<input type="text" name="short_name" value="">/<br>
  <label for="long_name">Long Name</label>
  <input type="text" name="long_name" value=""><br>
  <input type="submit" name="submit" class="button" value="Create Board">
</form>
</body>
</html>

