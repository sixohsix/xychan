
alter table threads add column pinned integer not null default 0;

alter table threads add column locked integer not null default 0;

alter table boards add column locked integer not null default 0;

alter table boards add column hidden integer not null default 0;

alter table boards add column long_name text not null default '';

CREATE TABLE ip_ban (
        id INTEGER NOT NULL, 
        ip_address VARCHAR NOT NULL, 
        ban_start DATETIME NOT NULL, 
        ban_expire DATETIME, 
        PRIMARY KEY (id)
);

