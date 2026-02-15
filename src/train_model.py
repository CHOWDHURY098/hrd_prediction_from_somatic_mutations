import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import joblib

df = pd.read_csv("features.csv")

X = df.drop("hrd", axis=1)
y = df["hrd"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = XGBClassifier(
    n_estimators=300,
    max_depth=4,
    learning_rate=0.05
)

model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test,y_test))

joblib.dump(model,"models/hrd_model.pkl")

