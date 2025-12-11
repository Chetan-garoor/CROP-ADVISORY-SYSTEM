import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# ----------------------------------------------------------
# 1. Load Your Dataset
# ----------------------------------------------------------
df = pd.read_csv("crop_recommendation_dataset.csv")  # change file name if needed

print("\n✅ Dataset Loaded:")
print(df.head())

# ----------------------------------------------------------
# 2. Split Features and Label
# ----------------------------------------------------------
X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']

# ----------------------------------------------------------
# 3. Encode Labels
# ----------------------------------------------------------
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

print("\n🌱 Encoded Crops:")
for idx, crop in enumerate(label_encoder.classes_):
    print(f"{idx} → {crop}")

# ----------------------------------------------------------
# 4. Train/Test Split
# ----------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# ----------------------------------------------------------
# 5. Train Model
# ----------------------------------------------------------
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=20,
    random_state=42
)

model.fit(X_train, y_train)

# ----------------------------------------------------------
# 6. Evaluate Model
# ----------------------------------------------------------
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print("\n📊 Model Accuracy:", acc)
print("\n📌 Classification Report:")
print(classification_report(y_test, y_pred))

# ----------------------------------------------------------
# 7. Save Model + Encoder
# ----------------------------------------------------------
joblib.dump(model, "crop_recommender_model.joblib")
joblib.dump(label_encoder, "crop_label_encoder.joblib")

print("\n🎉 Model Training Complete!")
print("➡ crop_recommender_model.joblib")
print("➡ crop_label_encoder.joblib")
