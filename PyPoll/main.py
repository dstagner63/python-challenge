import os
import csv
import pandas as pd

csvpath_in = os.path.join("Resources", "election_data.csv")
csvpath_out = os.path.join("Analysis", "pypoll.txt")
print(csvpath_in)

df = pd.read_csv(csvpath_in)
# df.head()

total_votes = len(df['Voter ID'].unique())
str_total_votes = 'Total Votes: ' + str(total_votes)
# str_total_votes

candidate_list = df['Candidate'].unique()
# candidate_list

list_df = df.groupby(by=['Candidate']).count()
list_df = list_df.rename(columns={'County': 'Count'})
list_df = list_df.drop(columns=['Voter ID'])
# list_df.head()

list_df['Percent Vote'] = (list_df['Count']/total_votes * 100).round(3)
# list_df

max_vote = list_df['Count'].max()
# From list_df find the value in count column that is equal to max vote. Then get the index's value. 
vote_winner = list_df[list_df['Count'] == max_vote].index[0]
# vote_winner

column_order = ['Percent Vote', 'Count']
list_df = list_df.loc[:, column_order]
list_df = list_df.sort_values(by='Count', ascending=False)
# list_df

print('Election Results')
print('--------------------------')
print(str_total_votes)
print('--------------------------')

for i in list_df.index:
    pct_vote = list_df['Percent Vote'][i]
    pct_vote = "{:.3f}".format(pct_vote)

    num_vote = list_df['Count'][i]
    num_vote = '% (' + str(num_vote) + ')'

    output_format = i + ': ' + pct_vote + num_vote
    print(output_format)

print('--------------------------')
print('Winner: %s' %vote_winner)
print('--------------------------')

file = open(csvpath_out, 'w')
file.write('Election Results\n')
file.write('--------------------------\n')
file.write(str_total_votes)
file.write('\n--------------------------\n')

for i in list_df.index:
    pct_vote = list_df['Percent Vote'][i]
    pct_vote = "{:.3f}".format(pct_vote)

    num_vote = list_df['Count'][i]
    num_vote = '% (' + str(num_vote) + ')'

    output_format = i + ': ' + pct_vote + num_vote
    file.write(output_format)
    file.write('\n')

file.write('--------------------------\n')
file.write('Winner: %s' %vote_winner)
file.write('\n--------------------------')
file.close()
