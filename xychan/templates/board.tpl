<html>
<head>
%include _header.tpl
  <title>{{board.short_name}}</title>
</head>
<body>
  <h1>{{board.short_name}}</h1>
  %include _post_form.tpl board=board
  <hr />
  %for post in posts:
  <div class="post">
    <div class="subject">{{post.subject}}</div>
    <div class="poster_name">{{post.poster_name}}</div>
    <div class="content">
      {{post.content}}
    </div>
  </div>
  %end
</body>
</html>
