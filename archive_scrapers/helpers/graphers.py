import os
import matplotlib.pyplot as plt
import pandas as pd
from helpers.processors import schools_pipeline_query_to_csv
from datetime import datetime

def grapher(school_names, 
            pipeline, 
            query, 
            y_label, 
            data_path, data_name,
            time_slice='yearly',
            title=None, img_path=None):
    csv_file = f"{data_path}/csv/{data_name}.csv"
    # Works whether or not the csv exists
    df = schools_pipeline_query_to_csv(school_names=school_names, pipeline=pipeline, query=query, csv_file=csv_file)
    if(time_slice != 'yearly' and time_slice != 'monthly'):
        raise ValueError("Invalid Time Slice")
    else:
        pkl_file = f"{data_path}/pkl/{time_slice}/{data_name}.pkl"
    if os.path.exists(pkl_file) and os.path.exists(csv_file):
        print(f"{pkl_file} being read.")
        # Load the grouped object from file
        grouped = pd.read_pickle(pkl_file)
    else:
        # Create the grouped object and save to file
        print(f"{pkl_file} being created.")
        group = 'school_year' if time_slice == 'yearly' else 'month'
        grouped = df.groupby(['school', group])['count'].sum()
        grouped.to_pickle(pkl_file)

    fig, ax = plt.subplots()

    if time_slice == 'monthly':
        # Plot a line with all 0 values throughout the range
        start_date = grouped.index.min()[1]
        end_date = grouped.index.max()[1]
        all_dates = pd.period_range(start=start_date, end=end_date, freq='M').strftime('%Y-%m')
        zero_values = [0] * len(all_dates)
        zero_line = ax.plot(all_dates, zero_values, linestyle='--', color='gray')[0]

    # Plot the data with the sorted x-axis values 
    for school_name in sorted(school_names, key = lambda x: grouped.loc[x].index.min()):
        if time_slice == 'yearly':
            # Note we cut out 2008-2009 as it's incomplete
            grouped_school = grouped.loc[school_name][1:]
            ax.plot(grouped_school.index, grouped_school.values, label=school_name)
        else:
            index_type = type(grouped[school_name].index)
            if index_type == pd.PeriodIndex:
                ax.plot(grouped[school_name].index.to_timestamp().strftime('%Y-%m'), grouped[school_name].values, label=school_name)
            elif index_type == pd.Index:
                ax.plot(pd.to_datetime(grouped[school_name].index).strftime('%Y-%m'), grouped[school_name].values, label=school_name)
            else:
                print(f"Unsupported index type: {index_type}")
                raise TypeError("Invalid index type")
            
    plt.xticks(rotation=60)
    x_label = 'School Year' if time_slice == 'yearly' else 'Month'
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    if title is not None:
        ax.set_title(title)
    ax.legend()

    if time_slice == 'monthly':
        # Show only every twelfth x-axis label
        zero_line.remove()
        tick_locations = ax.get_xticks()
        ax.set_xticks(tick_locations[::6])

    if img_path is not None:
        os.makedirs(os.path.dirname(img_path), exist_ok=True)
        plt.savefig(img_path, bbox_inches='tight')
    plt.show()
