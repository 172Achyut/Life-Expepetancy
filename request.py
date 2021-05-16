import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={"country": "Afghanistan", "year": 2015, "status": "Developing", "ad_mora": 263.00000, "inf_dth": 62, "alcohol": 0.01000, "per_exp": 71.27962, "hepa": 65.00000, "measles": 1154, "bmi": 19.10000, "v_dth": 83, "polio": 6.00000, "t_exp": 8.16000, "dthr": 65.00000, "hiv": 0.10000, "gdp": 584.25921, "population": 33736494.00000, "thn_1_19_yr": 17.20000, "thn_5_9_yr": 17.30000, "in_cm_yr": 0.47900, "schooling": 10.10000})

print(r.json())