def detect_anomalies(df):
    mean = df['temperature'].mean()
    std = df['temperature'].std()
    
    df['anomaly'] = abs(df['temperature'] - mean) > 2*std
    return df