import dash_html_components as html
import dash_core_components as dcc
import re
import os



def file_selector(directory, pattern, id='run_selection'):
    """
    File selection drop-down item
    """
    options = []

    for file in os.listdir(directory):
        if re.match(pattern, file):
            options.append({'label': os.path.splitext(file)[0], 'value': os.path.join(directory , file)})

    return dcc.Dropdown(
        id=id,
        options=options,
        value=options[0]['value']
    )
