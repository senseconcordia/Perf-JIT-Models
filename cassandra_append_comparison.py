import csv
import sys
csv.field_size_limit(sys.maxsize)

rq_1_dict = {}
rq_2_dict = {}


file = 'rq1 no smote/cassandra_final_results.csv'
with open(file) as csvfile:
    commits = csv.DictReader(csvfile, delimiter=',')
    for commit in commits:
        prediction = commit['x']
        false_rf = commit['False rf']	
        true_rf = commit['True rf']
        expected = commit['contains_bug']
        rq_1_dict[commit['commit_hash']] = [prediction, false_rf, true_rf, expected]

file = 'rq2 no smote/cassandra_final_results.csv'
with open(file) as csvfile:
    commits = csv.DictReader(csvfile, delimiter=',')
    for commit in commits:
        prediction = commit['x']
        false_rf = commit['False rf']	
        true_rf = commit['True rf']
        expected = commit['contains_bug']
        rq_2_dict[commit['commit_hash']] = [prediction, false_rf, true_rf, expected]

with open('cassandra_rq_1_2_comparison.csv', 'w') as outf:
    headers = ['commit_hash',
        'RQ1 prediction',
        'RQ1 False rf', 
        'RQ1 True rf',
        'RQ1 expected', 
        'RQ2 prediction',
        'RQ2 False rf', 
        'RQ2 True rf',
        'RQ2 expected']
         
    writer = csv.DictWriter(outf, headers, extrasaction='ignore',)
    writer.writeheader()  # For writing header
    for hash in rq_1_dict.keys():
        if hash in rq_2_dict.keys():
                d = {'commit_hash':hash,
                'RQ1 prediction':rq_1_dict[hash][0],
                'RQ1 False rf': rq_1_dict[hash][1],
                'RQ1 True rf': rq_1_dict[hash][2],
                'RQ1 expected':rq_1_dict[hash][3],
                'RQ2 prediction':rq_2_dict[hash][0],
                'RQ2 False rf': rq_2_dict[hash][1],
                'RQ2 True rf': rq_2_dict[hash][2],
                'RQ2 expected': rq_2_dict[hash][3]}
                writer.writerow(d)
                
# import csv
# import sys
# csv.field_size_limit(sys.maxsize)

# rq_1_dict = {}
# rq_2_dict = {}

# file = 'rq1/cassandra_final_results.csv'
# with open(file) as csvfile:
#     commits = csv.DictReader(csvfile, delimiter=',')
#     for commit in commits:
#         prediction = commit['x']
#         expected = commit['contains_bug']
#         # print(commit['commit_hash'])
#         rq_1_dict[commit['commit_hash']] = [prediction, expected]

# file = 'rq2/cassandra_final_results.csv'
# with open(file) as csvfile:
#     commits = csv.DictReader(csvfile, delimiter=',')
#     for commit in commits:
#         prediction = commit['x']
#         expected = commit['contains_bug']
#         # print(commit['commit_hash'])
#         rq_2_dict[commit['commit_hash']] = [prediction, expected]

# with open('cassandra_rq_1_2_comparison.csv', 'w') as outf:
#     headers = ['commit_hash','RQ1 prediction','RQ1 expected','RQ2 prediction','RQ2 expected']
#     writer = csv.DictWriter(outf, headers, extrasaction='ignore',)
#     writer.writeheader()  # For writing header
#     for hash in rq_1_dict.keys():
#                 d = {'commit_hash':hash,
#                 'RQ1 prediction':rq_1_dict[hash][0],
#                 'RQ1 expected':rq_1_dict[hash][1],
#                 'RQ2 prediction':rq_2_dict[hash][0],
#                 'RQ2 expected':rq_2_dict[hash][1]}
#                 writer.writerow(d)