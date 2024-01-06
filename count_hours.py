import pandas as pd
from datetime import datetime, timedelta

# Define a dictionary of holiday dates and their corresponding names
holidays = {
    'New Year’s Day': ['2024-01-01'],
    'Family Day': ['2024-02-10'],
    'Good Friday': ['2024-04-05'],
    'Easter Monday': ['2024-04-08'],
    'Victoria Day': ['2024-05-20'],
    'Canada Day': ['2024-07-01'],
    'Civic Holiday': ['2024-08-07'],
    'Labour Day': ['2024-09-04'],
    'Thanksgiving': ['2024-10-09'],
    'Christmas': ['2024-12-25'],
    'Boxing Day': ['2024-12-26']
}

def add_data():
    # Adjust your start and end dates  
    start_date = datetime(2024,1,8).date()  
    end_date = datetime(2024,4,22).date()    
    df= pd.DataFrame()
    # Create a column of dates from start to end date
    df['Date'] = pd.date_range(start=start_date,end= end_date)

    return df


def calc_hours():
    df = add_data()
    # Call function to create the DataFrame with Date values only

    for index,row in df.iterrows():
    
    # iterate for each index and row in the DataFrame
        date= row['Date']
        # Check if the date is a holiday or a weekday

        if date in holidays.values():
            df.at[index,'Hours'] = 0
        
        elif date.weekday() in [1,2,3]: # Check if the date is our selected working day, I have selected
                                        # Tuesday, Wednesday and Thursday   
            # If the date is Tuesday, Wednesday and Thursday, add 8 to the hours column
            df.at[index,'Hours']= 8
        else:
            # If the date is anyother day, add 0.
            df.at[index,'Hours']= 0

    
    # Add your file path here, including the file name of your excel sheet at the end.
    file_path= r'Enter/your/file/path/file_name'

    # Write the DataFrame to an excel sheet
    df.to_excel(excel_writer=file_path, sheet_name='Hours', index=False)

    return df
calc_hours()