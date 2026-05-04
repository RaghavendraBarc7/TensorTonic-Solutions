-- Write your SQL query here
select model_name, dataset, accuracy, rank() over (partition by dataset order by accuracy desc) as accuracy_rank, 
dense_rank() over (partition by dataset order by accuracy desc) as accuracy_dense_rank from model_metrics
order by 2, 3 desc, 1 