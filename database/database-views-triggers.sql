--------------------------------------------------------
-- SAM database views and triggers
-- last update: 24/06/2021
--------------------------------------------------------
use sam;

-- view_module_recommendations: get the recommendations mapped to a module.
drop view if exists view_module_recommendations;
create view view_module_recommendations as
select distinct
	r.id as recommendation_id,
    m.id as module_id,
    r.content as recommendation_content,
    r.description as recommendation_description,
    r.guidefilename as recommendation_guide,
	r.createdon,
    r.updatedon
from 
	module as m,
    module_question as mq,
    question as q,
    question_answer as qa,
    recommendation_question_answer as rqa,
    recommendation as r
where
	m.id = mq.moduleid and mq.questionid = q.id and 
    q.id = qa.questionid and
    rqa.questionanswerid = qa.id and rqa.recommendationid = r.id;
    

-- view_module_recommendations: get the recommendations, questions and answers mapped to a module.
drop view if exists view_module_recommendations_questions_answers;
create view view_module_recommendations_questions_answers as
select distinct
	m.id as module_id,
    r.id as recommendation_id,
    r.content as recommendation_content,
    rqa.id as recommendation_question_answer_id,
    qa.questionid as question_id,
    qa.answerid as answer_id,
    rqa.createdon,
    rqa.updatedon
from 
	module as m,
    module_question as mq,
    question as q,
    question_answer as qa,
    recommendation_question_answer as rqa,
    recommendation as r
where
	m.id = mq.moduleid and mq.questionid = q.id and 
    q.id = qa.questionid and
    rqa.questionanswerid = qa.id and rqa.recommendationid = r.id;


-- view_user_group: get groups of user
drop view if exists view_user_group;
create view view_user_group as
select
	u.id as user_id,
    u.email as user_email,
    g.id as group_id,
    g.designation as user_group
from
sam.group as g,
user_group as ug,
user as u
where
g.id = ug.groupid and
u.id = ug.userid;



-- view_module_question: get dependencies of a module
drop view if exists view_module_dependency;
create view view_module_dependency as
select
	d.id as dependency_id,
	d.moduleid as module_id,
    m.shortname as module_shortname,
    m.fullname as module_name,
    m.displayname as display,
    --
    d.dependson as depends_module_id,
    d.createdon,
    d.updatedon
from 
	module as m, dependency as d
where 
	d.moduleid = m.id;

-- view_module_question: get questions of a module.
drop view if exists view_module_questions_answers;
create view view_module_questions_answers as
select 
	m.id as module_id,
    m.displayname as module_displayname,
    --
    q.id as question_id, 
    q.content as question,
    --
    mq.questionorder,
    -- 
    a.id as answer_id, 
    a.content as answer,
    --
    q.createdon as question_createdon,
    q.updatedon as question_updatedon,
    a.createdon as answer_createdon,
    a.updatedon as answer_updatedon
from 
	module as m,question as q, 
    module_question as mq, 
    question_answer as qa,
    answer as a
where
	m.id = mq.moduleid and q.id = mq.questionid 
    and
    a.id = qa.answerid and q.id = qa.questionid;

-- view_module_question: get questions of a module.
drop view if exists view_module_question;
create view view_module_question as
select 
	m.id as module_id,
    m.displayname as module_displayname,
    --
    q.id as question_id,
    q.multipleanswers as multipleanswers,
    q.content as question,
    q.description as question_description,
    --
    mq.questionorder,
    --
    q.createdon,
    q.updatedon
from module as m,question as q, module_question as mq where
m.id = mq.moduleid and q.id = mq.questionid;

-- view_module_question: get answers of a module.
drop view if exists view_module_answers;
create view view_module_answers as
select 
	distinct
	m.id as module_id,
    --
    a.id as answer_id, 
    a.content as answer,
    --
    a.createdon,
    a.updatedon
from 
	module as m,
    question as q, 
    module_question as mq,
    answer as a, 
    question_answer as qa
    where
	m.id = mq.moduleid and 
    q.id = mq.questionid and
    a.id = qa.answerid and
    q.id = qa.questionid;

-- view_module_question: get sub-questions of a question (child questions of a parent question).
drop view if exists view_question_childs;
create view view_question_childs as
select
	qp.parent as parent_id,
    --
    qp.child as child_id,
    q.content as question,
    q.multipleanswers as multipleanswers,
    --
    qp.ontrigger,
    qp.questionorder
from 
	question_has_child as qp,
    question as q
where
	qp.child = q.id;
    
-- view_answer_question: get answers of a question.
drop view if exists view_question_answer;
create view view_question_answer as
select
	qa.id as question_answer_id,
	--
	q.id as question_id,
	q.content as question,
    --
    a.id as answer_id,
    a.content as answer
from 
	question as q, question_answer as qa, answer as a
where
	q.id = qa.questionid and qa.answerid = a.id;
    
    
-- view_answer_question: get answers of a question.
drop view if exists view_recommendations;
create view view_recommendations as
select 
	q.id as question_id,
    q.content as question,
    --
    a.id as answer_id, 
    a.content as answer,
    --
    r.content as recommendation
    
from 
	question as q, answer as a, question_answer as qa, recommendation_question_answer as rqa, recommendation as r
where
	q.id = qa.questionid and a.id = qa.answerid and
    r.id = rqa.recommendationid and qa.id = rqa.questionanswerid;


-- view_session_input_answer: get sessions of users.
drop view if exists view_user_sessions;
create view view_user_sessions as
select
	s.id as session_id,
    u.id as user_id,
    u.email as user_email,    
	s.moduleid,
    s.ended,
    s.createdon,
    s.updatedon
from
	session as s,
    user as u
where
	u.id = s.userid;


-- view_session_input_answer: get answers of a question.
drop view if exists view_session_answers;
create view view_session_answers as
-- ## shows user selected answers
select distinct
s.id as session_id, 
s.userid as session_userid,
s.moduleid as session_moduleid,
s.ended as session_ended,
s.createdon as session_createdon,
s.updatedon as session_updatedon,
--
null as module_logic,
--
q.id as question_id,
q.content as question,
--
sua.input answer_input,
--
a.id as answer_id,
a.content as answer
from 
	session as s,
    session_user_answer as sua,
    question as q,
    question_answer as qa,
    answer as a,
    module as m
where
	s.id = sua.sessionid and
    sua.questionanswerid = qa.id and
    qa.questionid = q.id and
    qa.answerid = a.id
union
-- ## shows user inputted answers
select distinct
s.id as session_id, 
s.userid as session_userid,
s.moduleid as session_moduleid,
s.ended as session_ended,
s.createdon as session_createdon,
s.updatedon as session_updatedon,
--
m.logicfilename as module_logic,
--
q.id as question_id,
q.content as question,
--
sua.input answer_input,
--
null as answer_id,
null as answer
from 
	session as s,
    session_user_answer as sua,
    question as q,
    question_answer as qa,
    module as m
where
	s.id = sua.sessionid and
    sua.questionid = q.id and
    s.moduleid = m.id;

-- view_session_recommendation: get recommendations stored in a session.
drop view if exists view_session_recommendation;
create view view_session_recommendation as
select 
s.id as session_id, 
s.userid as session_userid,
s.moduleid as session_moduleid,
s.ended as session_ended,
s.createdon as session_createdon,
s.updatedon as session_updatedon,
--
r.id as recommendation_id,
r.content as recommendation,
r.description as recommendation_description,
r.guidefilename as recommendation_guide,
r.createdon as recommendation_createdon,
r.updatedon as recommendation_updatedon
from 
	session as s,
    session_recommendation as sr,
    recommendation as r
where
	s.id = sr.sessionid and
    sr.recommendationid = r.id;

-- view_session_recommendation: get recommendations to be stored in a session. 
drop view if exists view_recommendation;
create view view_recommendation as
select distinct
s.id as session_id,
r.id as recommendation_id,
r.content as recommendation,
r.description as recommendation_description,
r.guidefilename
from
	session as s,
	session_user_answer as sua,
    question_answer as qa,
    recommendation_question_answer as rqa,
    recommendation as r
where
	s.id = sua.sessionid and
    sua.questionanswerid = qa.id and
    --
    qa.id = rqa.questionanswerid and
    rqa.recommendationid = r.id;
    
-- view_session_recommendation: get recommendations to be stored in a session that were computed using some logic.
drop view if exists view_recommendation_logic;
create view view_recommendation_logic as
select distinct
s.id as session_id,
r.id as recommendation_id,
r.content as recommendation,
r.description as recommendation_description,
r.guidefilename,
sr.id as session_recommendation_id
from
	session as s,
    session_recommendation as sr,
    recommendation as r
where
	s.id = sr.sessionid and
    r.id = sr.recommendationid
order by
    session_recommendation_id;
    
drop view if exists view_question_answer_recommendation;
create view view_question_answer_recommendation as
select
qa.questionid as question_id,
qa.answerid as answer_id,
r.id as recommendation_id,
r.content as content,
r.description as description,
r.guidefilename as guide,
r.createdon as createdon,
r.updatedon as updatedon
from
question_answer as qa, 
recommendation_question_answer as rqa,
recommendation as r
where
qa.id = rqa.questionanswerid and
r.id = rqa.recommendationid;

use sam;

-- trigger_recommendation_delete: after deleting a recommendation that cascades to table session_recommendation delete also linked sessions.
drop trigger if exists trigger_recommendation_delete;
create trigger trigger_recommendation_delete before delete on recommendation
for each row
	-- only delete a session, if the session linked to the deleted recommendation has no more recommendations linked to it.
    delete from session where session.id = (select sessionid from session_recommendation where session_recommendation.recommendationid = old.id)
	and exists (select sessionid from session_recommendation where sessionid = session.id group by sessionid having count(sessionid) = 1);

-- trigger_question_delete: after deleting a question that cascades to other tables, also delete linked sessions. these sessions become invalid.
drop trigger if exists trigger_question_delete;
create trigger trigger_question_delete before delete on question
for each row
	-- delete sessions linked to this question
    delete from session where 
    session.id in (select sessionid from session_user_answer where questionid = old.id or questionanswerid in (select id from question_answer where questionid = old.id));

-- trigger_answer_delete: after deleting an answer that cascades to other tables, also delete linked sessions. these sessions become invalid.
drop trigger if exists trigger_answer_delete;
create trigger trigger_answer_delete before delete on answer
for each row
	-- delete sessions linked to this question
    delete from session where 
    session.id in (select sessionid from session_user_answer where questionanswerid in (select id from question_answer where answerid = old.id));

-- before updating an entry, set now() into the 'updatedon' date, apply this to the following tables:
drop trigger if exists trigger_question_update;
create trigger trigger_question_update before update on question
for each row
	set new.updatedon = now();

drop trigger if exists trigger_module_update;
create trigger trigger_module_update before update on module
for each row
	set new.updatedon = now();

drop trigger if exists trigger_answer_update;
create trigger trigger_answer_update before update on answer
for each row
	set new.updatedon = now();

drop trigger if exists trigger_type_update;
create trigger trigger_type_update before update on type
for each row
	set new.updatedon = now();

drop trigger if exists trigger_session_update;
create trigger trigger_session_update before update on session
for each row
	set new.updatedon = now();

drop trigger if exists trigger_user_update;
create trigger trigger_user_update before update on user
for each row
	set new.updatedon = now();

drop trigger if exists trigger_group_update;
create trigger trigger_group_update before update on sam.group
for each row
	set new.updatedon = now();

