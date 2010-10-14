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
    </tr>
    %for board in boards:
    <tr>
      <td>{{board.id}}</td>
      <td>{{board.short_name}}</td>
    </tr>
    %end
  </table>
<h2>Create a new board</h2>
<form id="new_board" action="{{url('mod_create_board')}}" method="POST">
  <label for="short_name">Short Name</label><br>
  /<input type="text" name="short_name" value="">/<br>
  <input type="submit" name="submit" value="Create Board">
</form>
</body>
</html>

