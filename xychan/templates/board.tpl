<html>
<head>
  <title>{{board.short_name}}</title>
</head>
<body>
  <h1>{{board.short_name}}</h1>
  %include _post_form.tpl board=board
  %for post in posts:
  <div>
    {{post.content}}
  </div>
  %end
</body>
</html>
