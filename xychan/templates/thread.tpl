<html>
<head>
%include _header.tpl
<link rel="alternate" href="{{url('atom-thread-posts', board_name=board.short_name, thread_id=thread.id)}}" type="application/atom+xml">
  <title>{{board.pretty_title}}</title>
</head>
<body>
  %include _board_list.tpl
  <h1>{{board.pretty_title}} - Thread No. {{thread.id}}</h1>
  %if not board.locked:
    %include _post_form.tpl post_action=url("post_reply", board_name=board.short_name, thread_id=thread.id)
  %end
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
