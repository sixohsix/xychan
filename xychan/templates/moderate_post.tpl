<html>
<head>
%include _header.tpl
  <title>Moderate post {{post.id}}</title>
</head>
<body>
  <h1>Moderate post {{post.id}} in /{{post.thread.board.short_name}}/</h1>
  <div style="border:2px solid black;margin-bottom:24pt;">
    %include _post.tpl post=post, reply_link=None, first_post=post.is_first
  </div>
  %pn = "thread" if post.is_first else "post"
  <h2>Actions</h2>
  <form name="mod_actions" action="{{url("mod_submit")}}" method="POST">
  <input type="hidden" name="post_id" value="{{post.id}}">
  <ul>
    %if post.is_first:
      %if post.thread.pinned:
    <li><input type="submit" name="unpin" value="Unpin thread">
      %else:
    <li><input type="submit" name="pin" value="Pin thread">
      %end
      %if post.thread.locked:
    <li><input type="submit" name="unlock" value="Unlock thread">
      %else:
    <li><input type="submit" name="lock" value="Lock thread">
      %end
    %end
    <li><input type="submit" name="delete" value="Delete {{pn}}">
    <li><input type="submit" name="delete_and_ban" value="Delete {{pn}} and ban IP"> for <input name="num_days_to_ban" style="width:32pt;"> days
    <li><input type="submit" name="delete_and_ban_forever" value="Delete {{pn}} and ban IP forever">
    <li><input type="submit" name="annihilate" value="Annihilate all posts and threads and ban IP forever">
  </ul>
  </form>
</body>
</html>

