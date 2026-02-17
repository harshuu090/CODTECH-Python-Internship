import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load knowledge base
with open("knowledge.txt", "r", encoding="utf-8") as file:
    lines = file.read().strip().split("\n")

questions = []
answers = []

for i in range(0, len(lines)-1, 2):
    questions.append(lines[i].strip())
    answers.append(lines[i+1].strip())


# Clean text
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# Prepare vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform([clean_text(q) for q in questions])

def chatbot_response(user_input):
    user_input_clean = clean_text(user_input)
    user_vector = vectorizer.transform([user_input_clean])

    similarity = cosine_similarity(user_vector, X)
    best_match_index = similarity.argmax()
    best_score = similarity[0][best_match_index]

    # Debug print (optional)
    # print("Similarity score:", best_score)

    if best_score > 0.5:   # Increased threshold
        return answers[best_match_index]
    else:
        return "Sorry, I don't understand that."

print("Smart AI Chatbot is running! (type 'exit' to quit)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = chatbot_response(user_input)
    print("Bot:", response)

