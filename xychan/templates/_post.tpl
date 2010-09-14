    <div class="post{{' first' if first_post else ''}}">
      <div class="subject">{{post.subject}}</div>
      <div class="poster_name">{{post.poster_name}}</div>
      <div class="post_id"><a name="{{post.id}}">No. {{post.id}}</a></div>
      <div class="reply_link">
      %if reply_link:
        <a class="button" href="{{reply_link}}">Reply</a>
      %end
        <a class="button-red" href="#">☢</a>
      </div>
      <br>
      <div class="content">
        %if post.image_key:
        <a href="{{url('image', image=post.image_key)}}">
<img class="post_image" src="{{url('thumb', image=post.image_key)}}"></a>
        %end
        {{!post.content}}
      </div>
