# Hacktivity-Heatmap
Generates an interactive heatmap visualization of activity patterns by weekday and hour.

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


