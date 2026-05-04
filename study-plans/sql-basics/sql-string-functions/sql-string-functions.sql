-- Write your SQL query here
select lower(trim(respondent)) as respondent_clean, length(trim(raw_answer)) as answer_length, substring(trim(raw_answer), 1, 20) as answer_preview, split_part(source_url, '/', 3) as source_domain  from survey_responses 
ORDER BY respondent_clean ASC;

