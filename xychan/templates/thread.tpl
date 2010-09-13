<html>
<head>
%include _header.tpl
  <title>{{board.short_name}} - Thread No. {{thread.id}}</title>
</head>
<body>
  <h1>{{board.short_name}} - Thread No. {{thread.id}}</h1>
  %include _thread_post_form.tpl board=board, thread=thread
  <hr />
  <div class="thread">
    %first_post = True
    %for post in thread.posts:
    <div class="post{{' first' if first_post else ''}}">
      %first_post = False
      <div class="subject">{{post.subject}}</div>
      <div class="poster_name">{{post.poster_name}}</div>
      <div class="post_id">No. {{post.id}}</div>
      %if post.image_key:
      <a href="/i_/{{post.image_key}}"><img class="post_image" src="/t_/{{post.image_key}}/"></a>
      %end
      <div class="content">
        {{post.content}}
      </div>
    </div>
    %end
  </div>
</body>
</html>
