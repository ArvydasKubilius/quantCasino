from flask import Flask
import qDeck

app = Flask(__name__)

@app.route("/cards/draw")
def draw():
    return qDeck.draw()
	
@app.route("/cards/shuffle")
def shuffle():
    return qDeck.shuffle()

if __name__ == "__main__":
    app.run(debug=True)