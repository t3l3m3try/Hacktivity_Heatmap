# Hacktivity-Heatmap
Generates an interactive heatmap visualization of activity patterns by weekday and hour.

## Installation

```bash
pip install pandas plotly
```

## Usage

```bash
python heatmap_plot.py <input_file.txt>
```

This creates an HTML heatmap file in the same directory as the script.

## Input Format

Text file with ISO 8601 timestamps, one per line:

```
2025-10-05T09:21:59Z
2025-11-10T10:22:09Z
2025-12-23T12:26:23Z
```

## Output

Interactive HTML heatmap showing activity counts by weekday and hour. Darker blue indicates higher activity.

### Output Example:
<img width="1044" height="601" alt="1" src="https://github.com/user-attachments/assets/8e165b85-d38f-4442-9306-f39aa0828c79" />

