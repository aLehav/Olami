def monthly_grapher(directory, pipeline, query, y_label, title, save_path=None):
    import os
    import matplotlib.pyplot as plt
    from datetime import datetime
    import pandas as pd
    from helpers.queries import mention_tracker

    data = []
    dates = []

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            date_obj = datetime.strptime(filename[:-4], '%Y_%m_%d')
            dates.append(date_obj)

            with open(filepath, 'r', encoding="utf8") as file:
                contents = file.read()
            hillel_count = mention_tracker(contents, pipeline, query)
            data.append({'date': date_obj, 'count': 1 if hillel_count > 0 else 0})

    df = pd.DataFrame(data)
    df['month'] = df['date'].dt.to_period('M')
    grouped = df.groupby('month')['count'].sum()

    fig, ax = plt.subplots()
    ax.plot(grouped.index.strftime('%Y-%m'), grouped.values)
    plt.xticks(rotation=60)
    ax.set_xlabel('Month')
    ax.set_ylabel(y_label)
    ax.set_title(title)

    # Show only every third x-axis label
    tick_locations = ax.get_xticks()
    ax.set_xticks(tick_locations[::6])

    if save_path is not None:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, bbox_inches='tight')
    plt.show()

def monthly_grapher_multiple(school_names, pipeline, query, y_label, title=None, save_path=None):
    import os
    import matplotlib.pyplot as plt
    from datetime import datetime
    import pandas as pd
    from helpers.queries import mention_tracker

    data = []
    dates = []

    for school_name in school_names:
        directory = f"journal_data/txt/{school_name}"
        for filename in os.listdir(directory):
            if filename.endswith('.txt'):
                filepath = os.path.join(directory, filename)
                date_obj = datetime.strptime(filename[:-4], '%Y_%m_%d')
                dates.append(date_obj)

                with open(filepath, 'r', encoding="utf8") as file:
                    contents = file.read()
                hillel_count = mention_tracker(contents, pipeline, query)
                data.append({'school': school_name, 'date': date_obj, 'count': 1 if hillel_count > 0 else 0})

    df = pd.DataFrame(data)
    df['month'] = df['date'].dt.to_period('M')
    grouped = df.groupby(['school', 'month'])['count'].sum()

    fig, ax = plt.subplots()
    for school_name in sorted(school_names, key = lambda x: grouped.loc[x].index.min()):
        ax.plot(grouped[school_name].index.strftime('%Y-%m'), grouped[school_name].values, label=school_name)    
    plt.xticks(rotation=60)
    ax.set_xlabel('Month')
    ax.set_ylabel(y_label)
    if title is not None:
        ax.set_title(title)
    ax.legend()

    # Show only every sixth x-axis label
    tick_locations = ax.get_xticks()
    ax.set_xticks(tick_locations[::6])

    if save_path is not None:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, bbox_inches='tight')
    plt.show()

def yearly_grapher_multiple(school_names, pipeline, query, y_label, title=None, save_path=None):
    import os
    import matplotlib.pyplot as plt
    from datetime import datetime
    import pandas as pd
    from helpers.queries import mention_tracker

    data = []
    dates = []

    for school_name in school_names:
        directory = f"journal_data/txt/{school_name}"
        for filename in os.listdir(directory):
            if filename.endswith('.txt'):
                filepath = os.path.join(directory, filename)
                date_obj = datetime.strptime(filename[:-4], '%Y_%m_%d')
                dates.append(date_obj)

                with open(filepath, 'r', encoding="utf8") as file:
                    contents = file.read()
                hillel_count = mention_tracker(contents, pipeline, query)
                data.append({'school': school_name, 'date': date_obj, 'count': 1 if hillel_count > 0 else 0, 'school_year': get_school_year(date_obj)})

    df = pd.DataFrame(data)
    grouped = df.groupby(['school', 'school_year'])['count'].sum()

    fig, ax = plt.subplots()
    for school_name in sorted(school_names, key = lambda x: grouped.loc[x].index.min()):
        # Note we cut out 2008-2009 as it's incomplete
        grouped_school = grouped.loc[school_name][1:]
        ax.plot(grouped_school.index, grouped_school.values, label=school_name)
    plt.xticks(rotation=60)
    ax.set_xlabel('School Year')
    ax.set_ylabel(y_label)
    if title is not None:
        ax.set_title(title)
    ax.legend()

    # Show only every sixth x-axis label
    # tick_locations = ax.get_xticks()
    # ax.set_xticks(tick_locations[::6])

    if save_path is not None:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, bbox_inches='tight')
    plt.show()


def get_school_year(date_obj):
    if date_obj.month < 8:
        return f"{date_obj.year-1}-{date_obj.year}"
    else:
        return f"{date_obj.year}-{date_obj.year+1}"