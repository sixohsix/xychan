
alter table threads add column pinned integer not null default 0;

alter table threads add column locked integer not null default 0;

