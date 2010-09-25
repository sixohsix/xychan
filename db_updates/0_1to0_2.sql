
alter table visitor_prefs rename to visitors;

alter table visitors add column tripcode string not null default '';

alter table visitors add column use_tripcode boolean not null default false;

alter table posts add column visitor_id int null default null;
