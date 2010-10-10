    <div class="post{{' first' if first_post else ''}}">
      <div class="reply_link">
        %if c.user:
          <div class="post_ip"><a
            href="{{url("mod_post", post_id=post.id)}}">{{post.poster_ip}}</a>
          </div>
        %end
        %if reply_link and not post.thread.locked:
        <a class="button" href="{{reply_link}}">Reply</a>
        %end
      </div>
      %if post.thread.pinned:
      <div class="pinned"><img src="{{url('static', file='pushpin.png')}}"></div>
      %end
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
      %if post.thread.locked:
      <div class="locked"><img src="{{url('static', file='lock.png')}}"></div>
      %end
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
    </div>
