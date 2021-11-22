--------------------------------------------------------
-- SAM database shema
-- last update: 24/06/2021
--------------------------------------------------------
drop database if exists sam;
create database sam; -- beware that the database name also exists on several occurrences in this script.
use sam;

--
-- table structure for table 'module_group'
--
drop table if exists question;
create table question (
  id int(11) not null auto_increment,
  content varchar(255) not null,
  description text default null,
  multipleanswers tinyint(4) default 0,
  createdon datetime default current_timestamp(),
  updatedon datetime default current_timestamp(),
  primary key (id)
);

--
-- table structure for table 'answer'
--
drop table if exists answer;
create table answer (
  id int(11) not null auto_increment,
  content varchar(100) not null,
  description text default null,
  createdon datetime default current_timestamp(),
  updatedon datetime default current_timestamp(),
  primary key (id)
);

--
-- table structure for table 'user'
--
drop table if exists user;
create table user (
  id int(11) not null auto_increment,
  email varchar(45) not null,
  firstname varchar(30) not null,
  lastname varchar(30) default null,
  psw varchar(255) not null,
  avatar varchar(45) default null,
  userstatus tinyint(4) not null default 1 comment 'flag defines if the user is active.',
  administrator tinyint(4) default 0,
  createdon datetime default current_timestamp(),
  updatedon datetime default current_timestamp(),
  primary key (id),
  unique key email_unique (email)
);

--
-- table structure for table 'auth_token_blacklist'
--
drop table if exists auth_token_blacklist;
create table auth_token_blacklist (
  id int(11) not null auto_increment,
  userid int(11) not null,
  token varchar(255) not null comment 'avoid doubles',
  createdon datetime not null default current_timestamp(),
  updatedon datetime not null default current_timestamp(),
  primary key (id),
  unique key (token),
  key (userid),
  constraint fk_autho_token_blacklist_userid foreign key (userid) references user (id) on delete cascade on update cascade
);

--
-- table structure for table 'type'
--
drop table if exists type;
create table type (
  id int(11) not null auto_increment,
  name varchar(45) not null,
  description text default null,
  createdon datetime default current_timestamp(),
  updatedon datetime default current_timestamp(),
  primary key (id)
);

--
-- table structure for table 'module'
--
drop table if exists module;
create table module (
  id int(11) not null auto_increment,
  typeid int(11) default null,
  shortname varchar(45) not null,
  fullname varchar(100) not null,
  displayname varchar(45) not null,
  logicfilename varchar(45) default null,
  description text default null,
  avatar varchar(45) default null,
  disable int(1) default 0,
  createdon datetime not null default current_timestamp(),
  updatedon datetime not null default current_timestamp(),
  primary key (id),
  key (typeid),
  constraint fk_module_typeid foreign key (typeid) references type (id) on delete no action on update no action
);

--
-- table structure for table 'dependency'
--
drop table if exists dependency;
create table dependency (
  id int(11) not null auto_increment,
  moduleid int(11) not null,
  dependson int(11) not null,
  createdon datetime not null default current_timestamp(),
  updatedon datetime not null default current_timestamp(),
  primary key (id),
  unique key (moduleid,dependson),
  key (moduleid),
  key (dependson),
  constraint fk_dependency_moduleid foreign key (moduleid) references module (id) on delete cascade on update cascade,
  constraint fk_dependency_dependson foreign key (dependson) references module (id) on delete cascade on update cascade
);

--
-- table structure for table 'group'
--
drop table if exists sam.group;
create table sam.group (
  id int(11) not null auto_increment,
  designation varchar(45) not null,
  createdon datetime default current_timestamp(),
  updatedon datetime default current_timestamp(),
  primary key (id)
);

--
-- table structure for table 'module_group'
--
drop table if exists module_group;
create table module_group (
  id int(11) not null auto_increment,
  moduleid int(11) not null,
  groupid int(11) not null,
  createdon datetime default current_timestamp(),
  updatedon datetime default current_timestamp(),
  primary key (id),
  unique key (moduleid,groupid),
  key (groupid),
  key (moduleid),
  constraint fk_module_group_groupid foreign key (groupid) references sam.group (id) on delete cascade on update cascade,
  constraint fk_module_group_moduleid foreign key (moduleid) references module (id) on delete cascade on update cascade
);


--
-- table structure for table 'module_question'
--
drop table if exists module_question;
create table module_question (
  id int(11) not null auto_increment,
  moduleid int(11) not null,
  questionid int(11) not null,
  questionorder int(11) not null comment 'set the question order (i.e., first, second ?).',
  primary key (id),
  key (questionid),
  key (moduleid),
  constraint fk_module_question_moduleid foreign key (moduleid) references module (id) on delete cascade on update cascade,
  constraint fk_module_question_questionid foreign key (questionid) references question (id) on delete cascade on update cascade
);

--
-- table structure for table 'question_answer'
--
drop table if exists question_answer;
create table question_answer (
  id int(11) not null auto_increment,
  questionid int(11) not null,
  answerid int(11) not null,
  createdon datetime default current_timestamp(),
  updatedon datetime default current_timestamp(),
  primary key (id),
  unique key (answerid,questionid),
  key (questionid),
  key (answerid),
  constraint fk_question_answer_answerid foreign key (answerid) references answer (id) on delete cascade on update cascade,
  constraint fk_question_answer_questionid foreign key (questionid) references question (id) on delete cascade on update cascade
);


--
-- table structure for table 'question_has_child'
--
drop table if exists question_has_child;
create table question_has_child (
  id int(11) not null auto_increment,
  parent int(11) not null,
  child int(11) not null,
  ontrigger int(11) not null comment 'the answer (id) that triggers this sub-question (child) to be asked.',
  questionorder int(11) not null,
  createdon datetime not null default current_timestamp(),
  updatedon datetime not null default current_timestamp(),
  primary key (id),
  key (child),
  key (parent),
  key (ontrigger),
  constraint fk_question_has_child_ontrigger foreign key (ontrigger) references answer (id) on delete cascade on update cascade,
  constraint fk_question_has_child_parent foreign key (parent) references question (id) on delete cascade on update cascade,
  constraint fk_question_has_child_child foreign key (child) references question (id) on delete cascade on update cascade
);

--
-- table structure for table 'recommendation'
--
drop table if exists recommendation;
create table recommendation (
  id int(11) not null auto_increment,
  content varchar(100) not null,
  description text default null,
  guidefilename varchar(45) default null,
  createdon datetime default current_timestamp(),
  updatedon datetime default current_timestamp(),
  primary key (id)
);

--
-- table structure for table 'recommendation_question_answer'
--
drop table if exists recommendation_question_answer;
create table recommendation_question_answer (
  id int(11) not null auto_increment,
  recommendationid int(11) not null,
  questionanswerid int(11) not null,
  createdon datetime default current_timestamp(),
  updatedon datetime default current_timestamp(),
  primary key (id),
  unique key (recommendationid,questionanswerid),
  key (recommendationid),
  key (questionanswerid),
  constraint fk_recommendation_question_answer_questionanswerid foreign key (questionanswerid) references question_answer (id) on delete cascade on update cascade,
  constraint fk_recommendation_question_answer_recommendationid foreign key (recommendationid) references recommendation (id) on delete cascade on update cascade
);

--
-- table structure for table 'session'
--
drop table if exists session;
create table session (
  id int(11) not null auto_increment,
  userid int(11) not null,
  moduleid int(11) not null,
  ended tinyint(4) default 0,
  createdon datetime default current_timestamp(),
  updatedon datetime default current_timestamp(),
  primary key (id),
  key (moduleid),
  key (userid),
  constraint fk_session_moduleid foreign key (moduleid) references module (id) on delete cascade on update cascade,
  constraint fk_session_userid foreign key (userid) references user (id) on delete cascade on update cascade
);

--
-- table structure for table 'session_recommendation'
--
drop table if exists session_recommendation;
create table session_recommendation (
  id int(11) not null auto_increment,
  sessionid int(11) not null,
  recommendationid int(11) not null,
  createdon datetime default current_timestamp(),
  updatedon datetime default current_timestamp(),
  primary key (id),
  unique key (sessionid,recommendationid),
  key (recommendationid),
  key (sessionid),
  constraint fk_session_recommendation_recommendationid foreign key (recommendationid) references recommendation (id) on delete cascade on update cascade,
  constraint fk_session_recommendation_sessionid foreign key (sessionid) references session (id) on delete cascade on update cascade
);

--
-- table structure for table 'session_user_answer'
--
drop table if exists session_user_answer;
create table session_user_answer (
  id int(11) not null auto_increment,
  sessionid int(11) not null,
  questionanswerid int(11) default null comment 'this fk is only set if the answer is static (i.e. not provided by the user).',
  questionid int(11) default null comment 'this fk is only set if the answer is dynamic (i.e. provided by the user in a field input).',
  input varchar(45) default null,
  createdon datetime default current_timestamp(),
  updatedon datetime default current_timestamp(),
  primary key (id),
  unique key (sessionid,questionanswerid),
  key (sessionid),
  key (questionanswerid),
  key (questionid),
  constraint fk_session_user_answer_sessionid foreign key (sessionid) references session (id) on delete cascade on update cascade,
  constraint fk_session_user_answer_questionid foreign key (questionid) references question (id) on delete cascade on update cascade,
  constraint fk_session_user_answer_questionanswerid foreign key (questionanswerid) references question_answer (id) on delete cascade on update cascade
);

--
-- table structure for table 'user_group'
--
drop table if exists user_group;
create table user_group (
  id int(11) not null auto_increment,
  userid int(11) not null,
  groupid int(11) not null,
  createdon datetime default current_timestamp(),
  updatedon datetime default current_timestamp(),
  primary key (id),
  unique key (userid,groupid),
  key (groupid),
  key (userid),
  constraint fk_user_group_groupid foreign key (groupid) references sam.group (id) on delete cascade on update cascade,
  constraint fk_user_group_userid foreign key (userid) references user (id) on delete cascade on update cascade
);