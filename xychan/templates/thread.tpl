<html>
<head>
%include _header.tpl
  <title>{{board.short_name}} - Thread No. {{thread.id}}</title>
</head>
<body>
  <h1>{{board.short_name}} - Thread No. {{thread.id}}</h1>
  %include _post_form.tpl post_action=url("post_reply", board_name=board.short_name, thread_id=thread.id)
  <hr />
  <div class="thread">
    %first_post = True
    %for post in thread.posts:
      %include _post post=post, first_post=first_post, reply_link=None
      %first_post = False
    </div>
    %end
  </div>
  %include _footer.tpl
</body>
</html>
