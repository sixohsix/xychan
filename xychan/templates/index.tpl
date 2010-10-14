<html>
<head>
%include _header.tpl
  <title>Welcome to xychan</title>
</head>
<body>
  <h1>This is xychan</h1>
  <ul>
  %for board in boards:
    %if not board.hidden:
    <li><a href="{{url('board', board_name=board.short_name)}}">
      {{board.long_name if board.long_name else board.short_name}}</a></li>
    %end
  %end
  </ul>
  %include _footer.tpl
</body>
</html>
