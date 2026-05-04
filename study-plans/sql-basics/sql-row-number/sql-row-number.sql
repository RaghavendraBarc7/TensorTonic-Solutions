-- Write your SQL query here
select username, segment, engagement_score, row_number() over (partition by segment order by engagement_score desc, username) as activity_rank from user_activity 
order by segment, activity_rank