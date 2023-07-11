from flask import Flask

app = Flask("My First App")

@app.route('/')
def Hello():
    return "Hello Mehran"

if __name__ == "__main__":
    app.run(debug=True)