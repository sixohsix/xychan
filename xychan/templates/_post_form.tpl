<div class="post_form">
<form action="{{post_action}}" method="POST"
    enctype="multipart/form-data" name="post_form">
  <label for="name">Name</label><br>
  <input type="text" name="poster_name" value="{{c.visitor_prefs.poster_name if c.visitor_prefs else ""}}"><br>
  <label for="subject">Subject</label><br>
  <input type="text" name="subject" value=""><br>
  <label for="content">Content</label><br>
  <textarea name="content" value=""></textarea><br>
  <label for="image">Image</label><br>
  <input type="file" name="image"><br>
  <input type="submit" name="submit" value="Post" class="button">
</form>
</div>
