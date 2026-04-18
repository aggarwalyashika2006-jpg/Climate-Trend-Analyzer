import pandas as pd
import numpy as np

dates = pd.date_range(start="2015-01-01", periods=1500)

temp = 25 + np.sin(np.arange(1500)/365*2*np.pi)*10 + np.random.normal(0,2,1500)
rain = np.random.uniform(0,100,1500)

df = pd.DataFrame({
    "date": dates,
    "temperature": temp,
    "rainfall": rain
})

df.to_csv("data/raw/climate_data.csv", index=False)

print("Dataset created successfully!")