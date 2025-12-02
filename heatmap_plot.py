import pandas as pd
import plotly.express as px
from datetime import datetime
import re
import sys
import os

def parse_timestamps(file_path):
    """
    Parses the input file and extracts valid timestamps.
    Supports both ISO format and DD/MM/YYYY, HH:MM:SS.mmm format.
    Returns a DataFrame with weekdays and hours.
    """
    weekdays = []
    hours = []
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:  # Skip empty lines
                continue
                
            try:
                # Try ISO format first (e.g., 2025-09-15T09:58:53)
                if re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", line):
                    timestamp = datetime.fromisoformat(line.replace('Z', '+00:00'))
                    weekdays.append(timestamp.strftime('%A'))
                    hours.append(timestamp.hour)
                
                # Try DD/MM/YYYY, HH:MM:SS.mmm format
                elif re.match(r"^\d{2}/\d{2}/\d{4},\s*\d{2}:\d{2}:\d{2}", line):
                    # Parse the format: 15/09/2025, 09:58:53.000
                    timestamp = datetime.strptime(line.split('.')[0], '%d/%m/%Y, %H:%M:%S')
                    weekdays.append(timestamp.strftime('%A'))
                    hours.append(timestamp.hour)
                    
            except ValueError:
                # Skip invalid lines
                continue
    
    # Create a DataFrame with weekdays and hours
    return pd.DataFrame({'Weekday': weekdays, 'Hour': hours})

def generate_heatmap(dataframe, output_html):
    """
    Generates an HTML heatmap using Plotly and saves it as an HTML file.
    """
    # Create a pivot table to count occurrences
    heatmap_data = dataframe.pivot_table(index='Weekday', columns='Hour', aggfunc='size', fill_value=0)
    
    # Ensure rows are ordered by weekdays (Monday to Sunday)
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    heatmap_data = heatmap_data.reindex(weekday_order)
    
    # Ensure columns (hours) are ordered from 0 to 23
    heatmap_data = heatmap_data.reindex(range(24), axis=1, fill_value=0)
    
    # Replace NaN with 0 explicitly for visualization
    heatmap_data = heatmap_data.fillna(0)
    
    # Create the heatmap using Plotly Express
    fig = px.imshow(
        heatmap_data,
        labels=dict(x="Hour of Day", y="Weekday", color="Hits"),
        x=heatmap_data.columns,
        y=heatmap_data.index,
        color_continuous_scale="Blues",
        zmin=0,
        zmax=heatmap_data.values.max()
    )
    
    fig.update_layout(
        title="Heatmap of Hits by Weekday and Hour",
        xaxis_title="Hour of Day",
        yaxis_title="Weekday",
        coloraxis_colorbar_title="Hits",
        width=1000,
        height=600
    )
    
    # Ensure all hours are displayed
    fig.update_xaxes(dtick=1)
    
    # Save the heatmap to an HTML file
    fig.write_html(output_html)
    print(f"Heatmap saved to {output_html}")

def main():
    # Check if input file is provided
    if len(sys.argv) < 2:
        print("Usage: python heatmap_plot.py <input_file.txt>")
        print("Example: python heatmap_plot.py timeline_full.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Verify the input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    
    # Verify the input file is a .txt file
    if not input_file.endswith('.txt'):
        print("Error: Input file must be a .txt file.")
        sys.exit(1)
    
    # Get the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Generate output filename based on input filename (without extension)
    input_basename = os.path.splitext(os.path.basename(input_file))[0]
    output_html = os.path.join(script_dir, f"{input_basename}_heatmap.html")
    
    # Step 1: Parse timestamps from the input file
    print(f"Parsing file: {input_file}")
    dataframe = parse_timestamps(input_file)
    
    if dataframe.empty:
        print("Error: No valid timestamps found in the input file.")
        sys.exit(1)
    
    print(f"Successfully parsed {len(dataframe)} timestamps.")
    
    # Step 2: Generate the heatmap and save to HTML
    print("Generating heatmap...")
    generate_heatmap(dataframe, output_html)
    print("Process completed.")

if __name__ == "__main__":
    main()
