    <div class="post{{' first' if first_post else ''}}">
      <div class="reply_link">
        %if c.user:
          <div class="post_ip">{{post.poster_ip}}</div>
          <!-- <a class="button-lite" href="#" title="Pin thread">☝</a> -->
          <form name="mod_trash"
            action="{{url("trash_post", post_id=post.id)}}"
            method="POST">
            <input type="submit" class="button-lite"
              title="Trash {{"thread" if first_post else "post"}}"
              value="♺"></form>
        %end
        <a class="button-lite" href="#" title="Report post as offensive">⚑</a>
      %if reply_link:
        <a class="button" href="{{reply_link}}">Reply</a>
      %end
      </div>
      %if post.subject:
      <div class="subject">{{post.subject}}</div>
      %end
      %if post.poster_name:
      <div class="poster_name">{{post.poster_name}}</div>
      %end
      %if post.visitor_id:
      <div class="tripcode">!!{{post.visitor.tripcode}}</div>
      %end
      <div class="post_date">{{post.formatted_date}}</div>
      <div class="post_id"><a name="{{post.id}}">No. {{post.id}}</a></div>
      <br>
      <div class="content">
        %if post.image_key:
        <div class="p_img"><a href="{{url('image', image=post.image_key)}}">
<img class="post_image" src="{{url('thumb', image=post.image_key)}}"></a></div>
        %end
        <div class="p_con">
        {{!post.content}}
        </div><div class="foot">&nbsp;</div>
      </div>
