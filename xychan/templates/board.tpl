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
  %reply_link = str(thread.id) + '/'
  <div class="thread">
    %first_post = True
    %for post in thread.posts[-3:]:
      %include _post post=post, reply_link=reply_link, first_post=first_post
      %first_post = False
      %reply_link = None
    </div>
    %end
  </div>
  <hr>
  %end
</body>
</html>
