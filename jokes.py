import random
from flask import Flask

app = Flask(__name__)

# List of jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
    "Why don't skeletons fight each other? They don't have the guts!",
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "How does a penguin build its house? Igloos it together!",
    "What do you call fake spaghetti? An impasta!",
    "Why don't eggs tell jokes? Because they might crack up!",
]

@app.route('/')
def random_joke():
    # Choose a random joke from the list
    joke = random.choice(jokes)
    return f"<h1>{joke}</h1>"

if __name__ == '__main__':
    app.run()



