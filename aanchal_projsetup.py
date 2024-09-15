print("starting project 2")
####This module provides functions for creating a series of project folders.####

## importing modules from python library##

import pathlib
import time

## importing local module ##
import utils_gupta

# Create a path object
project_path = pathlib.Path.cwd()

# Define the new sub folder path
data_path = project_path.joinpath('data')

# Create new if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

#### defining functions for folder creation ####

##function 1 ##
start_year = 2020
end_year = 2023
duration_secs = 5
def create_folders_for_range(start_year: int, end_year: int) -> None:
    for year in range(start_year, end_year + 1 ):
        year_path = project_path.joinpath(str(year))
        year_path.mkdir(exist_ok=True)
        time.sleep(duration_secs)

 # Log the function call and its arguments using an f-string
print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")

## Function 2: Creates folders from a list of names ##

folder_names = ['data-csv', 'data-excel', 'data-json']
def create_folders_from_list(folder_list: list, to_lowercase=True, remove_spaces=True) -> None:
           
    for folder_names in folder_list:
        folder_path = project_path.joinpath(str(folder_names))
        folder_path.mkdir(exist_ok=True)
        
print(f"Function called: create_folders_from_list with '{folder_names}'")

## Function 3:  List comprehension ##
folder_id = ['csv', 'excel', 'json']
prefix = 'format-'
def create_prefixed_folders(folder_list: list, prefix: str) -> None:
  for folder_id in folder_list:
  # Create the full folder name with prefix
    folder_path = project_path / f"{prefix}-{folder_id}"
    folder_path.mkdir(exist_ok=True)

print(f"FUNCTION CALLED: create_folders_from_list with '{folder_id}'")

## Function 4: A While Loop ##

def create_folders_periodically(duration):
 #loop continously to create folders, until program is stopped
    folder_counter = 0
    
    while folder_counter < number_of_folders:
        # Define the folder path
        folder_path = project_path.joinpath(f"folder_{folder_counter}")
        
        # Create the folder if it doesn't already exist
        folder_path.mkdir(exist_ok=True)
        
        # Print a message indicating the folder creation
        print(f"FUNCTION CALLED: create_folder_periodically duration_seconds'{duration_secs}'")
        
        # Wait for the specified duration
        time.sleep(duration_secs)
        
        # Increment the counter
        folder_counter += 1

        #stop loop for running forever
        if folder_counter > number_of_folders:
            break
        

########### Define Main Function ###########


    ## Start of execution of main##
def main():

  ''' Main function to demonstrate module capabilities. '''

# Print byline from imported module

print(f"Byline: {utils_gupta.byline}")

    # Call function 1 to create folders for a range (e.g. years)
create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
folder_id = ['data-csv', 'data-excel', 'data-json']
create_folders_from_list(folder_id)

    # Call function 3 to create folders using comprehension
folder_id = ['csv', 'excel', 'json']
prefix = 'data-'
create_prefixed_folders(folder_id, prefix)

    # Call function 4 to create folders periodically using while
duration_secs = 5  # duration in seconds
number_of_folders = 5
folder_counter = 0
create_folders_periodically(duration_secs)

    # Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

     ## End of execution of main ##

     # Conditional Script Execution
if __name__ == '__main__':
    main()