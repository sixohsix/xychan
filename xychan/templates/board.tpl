<html>
<head>
%include _header.tpl
  <title>{{board.short_name}}</title>
</head>
<body>
  <h1>{{board.short_name}}</h1>
  %include _post_form.tpl board=board
  <hr />
  %for thread in threads:
  <div class="thread">
    %reply_link = url('thread', board_name=board.short_name, thread_id=thread.id)
    %for post in thread.short_view_posts:
      %include _post post=post, reply_link=reply_link, first_post=reply_link
      %reply_link = None
    </div>
    %end
  </div>
  <hr>
  %end
</body>
</html>
