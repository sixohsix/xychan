% from xychan.db import get_all_visible_boards
<div class="board_list">[ <a href="{{url('index')}}">Home</a> ] [
%for board in get_all_visible_boards():
  / <a href="{{url('board', board_name=board.short_name)}}" title="{{board.long_name}}">{{board.short_name}}</a>
%end
  / ]</div>
