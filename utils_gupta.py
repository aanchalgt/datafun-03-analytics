''' ITERATION 5

Module: Datapulse Analytics - Insight at your fingertips.

In this iteration, enhance the byline to include key statistics. '''



####################################
#Importing statistics module at the top
####################################

import statistics

#####################################
#Declare global variables 
#####################################

#boolean variable to indicate the field of company is a Global CRO
company_field : bool = True
#Integer variable for the number of years in operation
years_in_operation: int = 16
#List of strings representing the services offered by the company
services_offered: list = ["Data Analysis", "Machine Learning", "Clinical Research"]
#List of floats representing individual client satisfaction scores 
client_satisfaction_scores: list = [4.8, 4.9, 4.7, 5.0, 4.9]
#list of number of projects in the last 5 years
num_of_projects: list = [23, 19, 21, 19, 26]


#####################################
# Calculating basic statistics, before we declare the byline.
# We do this to have calculated values ready for use in the byline.
#####################################

#calculating basic stats using built-in functions min(),max() and statistics module functions mean() and stdev().
min_score: float = min(client_satisfaction_scores)
max_score: float = max(client_satisfaction_scores)
mean_score: float = statistics.mean(client_satisfaction_scores)
stdev_score: float = statistics.stdev(client_satisfaction_scores)

min_num: float = min(num_of_projects)
max_num: float = max(num_of_projects)
mean_num: float = statistics.mean(num_of_projects)
stdev_num: float = statistics.stdev(num_of_projects)



#####################################
# Declare a global variable named byline.
# Making it a multiline f-string to show our information.
#####################################

byline: str = f"""
-----------------------------------------------------
Datapulse Analytics - Insight at your fingertips.
-----------------------------------------------------
Is a Global CRO:    {company_field}
Years in operation: {years_in_operation}
Services offered:   {services_offered}
Client rating:      {client_satisfaction_scores}
No. of Projects:    {num_of_projects}

Minimum of Client Satisfaction score: {min_score}
Maximum of Client Satisfaction score: {max_score}
Mean of Client Satisfaction score: {mean_score}
Standard Deviation of Client Satisfaction score: {stdev_score}

Minimum of Number of projects: {min_num}
Maximum of Number of projects: {max_num}
Mean of Number of projects: {mean_num}
Standard Deviation of Number of projects: {stdev_num}


"""

#####################################
# Define the get_byline() Function.
#####################################

def get_byline() -> str:
   '''Return a byline for my analytics projects.'''
   return byline

#####################################
# Define a main() function for this module.
#####################################



def main() -> None:
    '''Print results of get_byline() when main() is called'''
    print(get_byline())


#####################################
# Conditional Execution 
#####################################

if __name__ == '__main__':
    main()
