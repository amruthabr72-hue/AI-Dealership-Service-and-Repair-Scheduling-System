import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("issues.csv")

# Input text
X = df['text']

# Output labels
y = df['label']

# Convert text into numerical vectors
vectorizer = TfidfVectorizer()

X_vectors = vectorizer.fit_transform(X)

# Create ML model
model = RandomForestClassifier()

# Train model
model.fit(X_vectors, y)

# Prediction function
def predict_issue(text):

    # Convert new text into vectors
    text_vector = vectorizer.transform([text])

    # Predict issue
    prediction = model.predict(text_vector)

    return prediction[0]