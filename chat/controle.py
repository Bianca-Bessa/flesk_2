from aplicacao import app
from flask import render_template


@app.route('/')
def index():
    context = {'titulo': 'Pagina principal',
               'mensagens': ['Usuário: olá', 'Usuário: olá']}
    return render_template('index.html', **context)


app.run(debug=True)
