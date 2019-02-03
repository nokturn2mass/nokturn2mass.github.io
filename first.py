from flask import Flask,render_template
from flask import request, redirect
from searching_module import search_letter


app =Flask("__name__")






@app.route('/search', methods=['POST', 'GET'])
def searching():
    phrase = request.form['phrase']
    letters = request.form['letters']
    title='Вот ваши результаты:'
    results=str(search_letter(phrase, letters))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_title=title,
                           the_results=results,
                           the_letters=letters,
                           )

@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html',
                           the_title='Добро пожаловать на searching.letter!')


if __name__=='__main__':
    app.run(debug=True)


app.run(debug=True)