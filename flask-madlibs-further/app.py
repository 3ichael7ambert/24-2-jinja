from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def choose_story():
    """Show list-of-stories form."""

    return render_template("choose-story.html",
                           stories=stories.values())


@app.route('/question')
def index():

    """Generate and show form to ask words."""

    story_id = request.args["story_id"]
    story = stories[story_id]

    prompts = story.prompts

    return render_template("questions.html",
                           story_id=story_id,
                           title=story.title,
                           prompts=prompts)


@app.route("/story")
def show_result():
    """Show story result."""

    text = story.generate(request.args)

    return render_template("result.html", text=text)



if __name__ == '__main__':
    app.run(debug=True)