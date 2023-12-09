lesson completion              Users

compl id                        userid

user id  (fk) users.userid      uname
                                active
lesson id
comple date



At Mindtickle, a client has requested a custom report that lists all
active users on the platform and the number of daily lessons they have completed in the last 30 days.
Your task is to create a Python script to generate this report and save it in an AWS S3 Bucket.

select Users.Uname, Users.activestatus,lessoncomple.completionid,count(completionid) as lessons_completed from
Users JOin lesson_compl
ON User.userid  = lesson_completion.usersid
Group BY (Userid,)


select l.completion_date,u.uname,u.userid, count(*) as lessonscompleted
from users u JOIN  lesson_completion l 
ON u.userid = l.userid
WHERE u.activestatus = "active"
GROUP BY completiondate,userid
ORDER BY l.completiondate