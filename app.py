from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', name='World')


@app.route('/atividade01')
@app.route('/atividade01/<number>')
def atividade01():
    return (render_template('atividade01.html'))


@app.route('/atividade02')
def atividade02():
    return (render_template('atividade02.html'))


@app.route('/atividade03')
def atividade03():
    return (render_template('atividade03.html'))


@app.post('/process_number')
def process_number():
    number = int(request.form['input'])

    mult_table = []
    for i in range(1, 10 + 1):
        mult = number * i
        mult_table.append((number, i, mult))

    return render_template('atividade01.html', result=number, mult_results=mult_table)


if __name__ == '__main__':
    app.run(debug=True)
