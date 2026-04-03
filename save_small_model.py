import pickle
import pandas as pd
import numpy as np
import os
from sklearn.tree import DecisionTreeClassifier

# Load your existing data
df = pd.read_csv('Final_data.csv')

print("Columns:", df.columns.tolist())
print("Shape:", df.shape)

# Add week_num column
if 'week_num' not in df.columns:
    df['week_num'] = (df['day'] // 7) + 1

# Define feature columns
feature_cols = ['year', 'mon', 'Cases', 'Deaths', 'preci', 'LAI', 'Temp', 'Latitude', 'Longitude', 'week_num']

# Clean all feature columns - convert to numeric, replace errors with 0
for col in feature_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    else:
        df[col] = 0

# Prepare X and y
X = df[feature_cols]
y = df['Disease'].fillna('Unknown')

print("Training data shape:", X.shape)
print("Unique diseases:", y.nunique())
print("Features:", feature_cols)
print("Sample X:\n", X.head())

# Train small lightweight model
small_model = DecisionTreeClassifier(max_depth=10, random_state=42)
small_model.fit(X, y)

# Save the small model
with open('disease_model.pkl', 'wb') as f:
    pickle.dump(small_model, f)

# Save the model columns
with open('model_columns.pkl', 'wb') as f:
    pickle.dump(feature_cols, f)

size_mb = os.path.getsize('disease_model.pkl') / 1024 / 1024
print(f"✅ Done! New model size: {size_mb:.2f} MB")
print("Classes:", small_model.classes_.tolist())