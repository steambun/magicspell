from flask import Flask, request,render_template,session

app = Flask(__name__)

# The secret key is used to cryptographically-sign the cookies used for storing the session data
app.secret_key = "b'\x9a\\QE\xcb\x86@\xd2\x88\x8e\xa4w\x9b\x98\xa6\x86'"

@app.route("/")
def index():
    session['word_letter_middle']="a"
    session['word_letter_1']="b"
    session['word_letter_2']="c"
    session['word_letter_3']="d"
    session['word_letter_4']="e"
    session['word_letter_5']="f"
    session['word_letter_6']="g"
    session['display_error']="The word you entered is invalid"
    return render_template('index.html')

@app.route("/submit_guess",methods=['GET','POST'])
def guess_submitted():
    if request.method=='POST':
        guess = request.form.get('guess').lower()
        print(guess)
    return render_template('index.html')
