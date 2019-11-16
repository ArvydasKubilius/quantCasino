from flask import Flask
import qDeck
import qSpin

app = Flask(__name__)

@app.route("/cards/draw")
def draw():
    return qDeck.draw()
	
@app.route("/cards/shuffle")
def shuffle():
    return qDeck.shuffle()
	
@app.route("/spin/spin")
def shuffle():
    return qSpin.spin()

if __name__ == "__main__":
    app.run(debug=True)