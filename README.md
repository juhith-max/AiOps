# AIOps Log Analysis Tool

This tool uses machine learning (Isolation Forest) to detect anomalies in system logs. It analyzes log entries based on their severity levels and message lengths to identify potentially suspicious or unusual patterns.

## Features

- Automated log parsing and analysis
- Anomaly detection using Isolation Forest algorithm
- Support for different log levels (INFO, WARNING, ERROR, CRITICAL)
- Generates detailed anomaly reports
- Handles malformed log entries gracefully

## Prerequisites

- Python 3.8 or higher
- Required Python packages:
  - pandas
  - numpy
  - scikit-learn

## Installation

1. Clone this repository or download the source code
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows:
     ```bash
     .\venv\Scripts\Activate.ps1
     ```
   - Unix/MacOS:
     ```bash
     source venv/bin/activate
     ```
4. Install required packages:
   ```bash
   pip install requirements.txt
   ```

## Usage

1. Prepare your log file (`system_logs.txt`) in the following format:
   ```
   YYYY-MM-DD HH:MM:SS LEVEL Message
   ```
   Example:
   ```
   2025-03-27 10:00:00 INFO System startup
   2025-03-27 10:00:04 WARNING High CPU usage detected
   ```

2. Run the analysis script:
   ```bash
   python aiops_log_analysis.py
   ```

3. The script will generate an `anomaly_report.txt` file containing:
   - Detailed list of detected anomalies
   - Total count of anomalies found
   - Timestamps and log levels of anomalous entries

## How It Works

The tool uses the following features to detect anomalies:
- Log level severity (INFO=1, WARNING=2, ERROR=3, CRITICAL=4)
- Message length
- Isolation Forest algorithm with 10% contamination rate

## Output Format

The generated `anomaly_report.txt` will contain:
```
=== Detected Anomalies ===
[Detailed list of anomalies with timestamps, levels, and messages]

Total Anomalies Detected: [number]
```

## Error Handling

The script includes comprehensive error handling for:
- File reading errors
- Malformed log entries
- Data processing issues
- File writing errors

## Contributing

Feel free to submit issues and enhancement requests! 