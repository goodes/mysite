
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request, flash, g, session
import game

app = Flask(__name__)

app.config.update(dict(
        DEBUG=True,
        SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/',
    ))

LETTERS = [chr(ord('a') + i) for i in range(26)]


def reset():
    session['errors'] = 0
    session['word'] = game.choose_word()
    session['guessed'] = ['_'] * len(session['word'])
    session['letters'] = LETTERS


@app.route('/')
def index():
    reset()
    return render_template('game.j2', sesion=session) #word=word, letters=letters, errors=session['errors'])

@app.route('/choose/<letter>')
def choose(letter):
    if len(letter) != 1 or letter.lower() not in LETTERS:
        flash("Bad letter %s" % letter)
        return render_template('game.j2', sesion=session)

    letter = letter.lower()

    if letter not in session['letters']:
        flash("repeat")
    else:
        session['letters'][ord(letter) - ord('a')] = ' '
        if letter not in session['word']:
            session['errors'] += 1
        else:
            guessed = session['guessed']
            for pos, let in enumerate(list(session['word'])):
                if letter == let:
                    guessed[pos] = letter
            session['guessed'] = guessed

    if session['errors'] == 6:
        flash("You LOOSE, word was '%s'" % session['word'])
        session['letters'] = []

    if '_' not in session['guessed']:
        flash("You win, word was '%s'" % session['word'])
        session['letters'] = []

    return render_template('game.j2', sesion=session) #, word=word, letters=letters, errors=session['errors'])
    # return 'Hello %s' % username
