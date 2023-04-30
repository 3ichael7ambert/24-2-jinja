from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def index():

    """Generate and show form to ask words."""

    prompts = story.prompts

    return render_template("index.html",prompts=prompts)


@app.route("/story")
def show_result():
    """Show story result."""

    text = story.generate(request.args)

    return render_template("result.html", text=text)



if __name__ == '__main__':
    app.run(debug=True)