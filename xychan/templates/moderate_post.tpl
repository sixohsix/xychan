<html>
<head>
%include _header.tpl
  <title>Moderate post {{post.id}}</title>
</head>
<body>
  <h1>Moderate post {{post.id}}</h1>
  <div style="border:2px solid black;margin-bottom:24pt;">
    %include _post.tpl post=post, reply_link=None, first_post=True
  </div>
  <h2>Actions</h2>
  <form name="mod_actions" action="{{url("mod_submit")}}" method="POST">
  <input type="hidden" name="post_id" value="{{post.id}}">
  <ul>
    <li><input type="submit" name="delete" value="Delete post">
    <li><input type="submit" name="delete_and_ban" value="Delete post and ban IP"> for <input name="num_days_to_ban" style="width:32pt;"> days
    <li><input type="submit" name="delete_and_ban_forever" value="Delete post and ban IP forever">
    <li><input type="submit" name="annihilate" value="Annihilate all posts and ban IP forever">
  </ul>
  </form>
</body>
</html>

