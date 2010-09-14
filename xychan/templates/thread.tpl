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
      %include _post post=post, first_post=first_post, reply_link=None
      %first_post = False
    </div>
    %end
  </div>
</body>
</html>
