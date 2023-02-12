from flask import Flask, request,render_template,session

from magicspell import generate_random_letter_order, generate_random_word,find_valid_subset_words

app = Flask(__name__)

# The secret key is used to cryptographically-sign the cookies used for storing the session data
app.secret_key = "b'\x9a\\QE\xcb\x86@\xd2\x88\x8e\xa4w\x9b\x98\xa6\x86'"

@app.route("/")
def index():
    random_word=generate_random_word()
    print("Random Word: "+random_word)

    valid_words=find_valid_subset_words("wordlist.txt",random_word)
    
    print("Valid Words:")
    for valid_word in valid_words:    
        print("\t"+valid_word)

    letter_order=generate_random_letter_order()
    session['word_letter_middle']=random_word[letter_order[0]]
    session['word_letter_1']=random_word[letter_order[1]]
    session['word_letter_2']=random_word[letter_order[2]]
    session['word_letter_3']=random_word[letter_order[3]]
    session['word_letter_4']=random_word[letter_order[4]]
    session['word_letter_5']=random_word[letter_order[5]]
    session['word_letter_6']=random_word[letter_order[6]]
    session['display_error']="The word you entered is invalid"
    session['last_guess']="guess"
    session['guess_list']=[]
    session['random_word']=random_word
    return render_template('index.html')

@app.route("/submit_guess",methods=['GET','POST'])
def guess_submitted():
    if request.method=='POST':
        guess = request.form.get('guess').lower()
        session['guess_list'].append(guess)
        session.modified = True
        print(guess)
    return render_template('index.html')
