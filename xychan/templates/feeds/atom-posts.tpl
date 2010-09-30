<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">

%board = posts[0].thread.board
<title>{{feed_title}}</title>
<link href="{{feed_url}}" rel="self" />
<link href="{{rurl('index')}}" />
<id>urn:xychan:board/{{board.short_name}}</id>
<updated>{{posts[0].posted.strftime('%Y-%m-%dT%H:%M:%SZ')}}</updated>

%for post in posts:
<entry>
  <title>{{post.subject or 'No Subject'}}</title>
  <link href="{{rurl('thread', board_name=board.short_name, thread_id=post.thread.id)}}" />
  <id>urn:xychan:{{c.server_name}}/{{board.short_name}}/{{post.id}}</id>
  <updated>{{post.posted.strftime('%Y-%m-%dT%H:%M:%SZ')}}</updated>
  <context type="html">
{{post.content}}
  </content>
  <author>
    <name>{{post.poster_name or 'Anonymous'}}</name>
  </author>
</entry>
%end
</feed>
