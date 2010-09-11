<html>
<head>
  <title>{{board.short_name}}</title>
</head>
<body>
  <h1>{{board.short_name}}</h1>
  %for post in posts:
  <div>
    {{post.content}}
  </div>
  %end
</body>
</html>
