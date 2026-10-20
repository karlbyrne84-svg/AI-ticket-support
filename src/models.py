import joblib

cat_model = joblib.load("cat_model.pkl")
cat_vector = joblib.load("cat_vectorizer.pkl")

prior_model = joblib.load("prior_model.pkl")
prior_vector = joblib.load("prior_vectorizer.pkl")

def predict_category(query):
    category_prediction = cat_vector.transform([query])
    return cat_model.predict(category_prediction)[0]

def predict_priority(query):
    priority_prediction = prior_vector.transform([query])
    return prior_model.predict(priority_prediction)[0]

query = "every time i log into the website it crashes"

print("category", predict_category(query))
print("priority", predict_priority(query))