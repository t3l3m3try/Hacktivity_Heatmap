# Hacktivity-Heatmap
Generates an interactive heatmap visualization of activity patterns by weekday and hour.

## Features

- Creates interactive HTML heatmaps using Plotly
- Supports multiple timestamp formats
- Visualizes activity by weekday (Monday-Sunday) and hour (0-23)
- Clean, professional visualization with color-coded intensity
- Automatically handles invalid/malformed timestamps

The script accepts timestamps in two formats:

1. **ISO 8601 format:**
   ```
   2025-09-15T09:58:53
   2025-09-15T09:58:53.000
   2025-09-15T09:58:53.000Z
   ```

2. **DD/MM/YYYY format:**
   ```
   15/09/2025, 09:58:53.000
   15/09/2025, 09:58:53
   ```

Files can contain a mix of both formats.

## Requirements

```bash
pip install pandas plotly
```

Or install from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python heatmap_plot.py <input_file.txt>
```

This creates an HTML heatmap file in the same directory as the script.

## Output

Interactive HTML heatmap showing activity counts by weekday and hour. Darker blue indicates higher activity.

### Output Example:

<img width="1025" height="591" alt="1" src="https://github.com/user-attachments/assets/849503fa-ea82-42ec-9c27-59426ec87042" />


