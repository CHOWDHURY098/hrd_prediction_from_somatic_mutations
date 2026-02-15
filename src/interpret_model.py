import shap
import joblib
import pandas as pd

model = joblib.load("models/hrd_model.pkl")
X = pd.read_csv("features.csv").drop("hrd",axis=1)

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

shap.summary_plot(shap_values, X)
