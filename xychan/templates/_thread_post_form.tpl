<div class="post_form">
<form action="/{{board.short_name}}/{{thread.id}}/post" method="POST"
    enctype="multipart/form-data">
  <label for="name">Name</label><br>
  <input type="text" name="poster_name" value=""><br>
  <label for="subject">Subject</label><br>
  <input type="text" name="subject" value=""><br>
  <label for="content">Content</label><br>
  <textarea name="content" value=""></textarea><br>
  <label for="image">Image</label><br>
  <input type="file" name="image"><br>
  <input type="submit" name="submit" value="Post">
</form>
</div>
