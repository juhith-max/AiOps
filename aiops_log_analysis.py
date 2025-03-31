import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

try:
    # Read log file
    log_file_path = "system_logs.txt"
    print(f"Reading log file: {log_file_path}")
    with open(log_file_path, "r") as file:
        logs = file.readlines()
    print(f"Successfully read {len(logs)} log entries")

    # Parse logs into a structured DataFrame
    data = []
    for log in logs:
        parts = log.strip().split(" ", 3)  # Ensure the message part is captured fully
        if len(parts) < 4:
            print(f"Skipping malformed line: {log}")
            continue  # Skip malformed lines
        timestamp = parts[0] + " " + parts[1]
        level = parts[2]
        message = parts[3]
        data.append([timestamp, level, message])

    df = pd.DataFrame(data, columns=["timestamp", "level", "message"])
    print(f"Created DataFrame with {len(df)} rows")

    # Convert timestamp to datetime format for sorting
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Assign numeric scores to log levels
    level_mapping = {"INFO": 1, "WARNING": 2, "ERROR": 3, "CRITICAL": 4}
    df["level_score"] = df["level"].map(level_mapping)

    # Add message length as a new feature
    df["message_length"] = df["message"].apply(len)

    # AI Model for Anomaly Detection (Isolation Forest)
    model = IsolationForest(contamination=0.1, random_state=42)
    df["anomaly"] = model.fit_predict(df[["level_score", "message_length"]])

    # Mark anomalies in a readable format
    df["is_anomaly"] = df["anomaly"].apply(lambda x: "ANOMALY" if x == -1 else "Normal")

    # Get anomalies and write to file
    anomalies = df[df["is_anomaly"] == "ANOMALY"]
    print(f"Found {len(anomalies)} anomalies")
    
    with open("anomaly_report.txt", "w", encoding='utf-8') as f:
        f.write("=== Detected Anomalies ===\n")
        f.write(anomalies.to_string())
        f.write(f"\n\nTotal Anomalies Detected: {len(anomalies)}")
    
    print("Report has been written to anomaly_report.txt")

except Exception as e:
    print(f"An error occurred: {str(e)}")
    import traceback
    traceback.print_exc()


