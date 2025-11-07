from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'clave_secreta_segura'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gastos', methods=['GET', 'POST'])
def gastos():
    if 'gastos' not in session:
        session['gastos'] = [['', ''] for _ in range(8)]
    if request.method == 'POST':
        if 'reiniciar' in request.form:
            session.pop('gastos', None)
            return redirect(url_for('gastos'))
        for i in range(8):
            session['gastos'][i][0] = request.form.get(f'categoria_{i}', '')
            session['gastos'][i][1] = request.form.get(f'monto_{i}', '')
        session.modified = True
    total = sum(float(row[1]) for row in session['gastos'] if row[1])
    return render_template('gastos.html', gastos=session['gastos'], total=total)

@app.route('/ahorro', methods=['GET', 'POST'])
def ahorro():
    if 'ahorro' not in session:
        session['ahorro'] = [['', ''] for _ in range(8)]
    if request.method == 'POST':
        if 'reiniciar' in request.form:
            session.pop('ahorro', None)
            return redirect(url_for('ahorro'))
        for i in range(8):
            session['ahorro'][i][0] = request.form.get(f'habito_{i}', '')
            session['ahorro'][i][1] = request.form.get(f'ahorro_{i}', '')
        session.modified = True
    total = sum(float(row[1]) for row in session['ahorro'] if row[1])
    return render_template('ahorro.html', ahorro=session['ahorro'], total=total)

@app.route('/tips')
def tips():
    return render_template('tips.html', title='Tips para Ahorrar')

if __name__ == '__main__':
    app.run(debug=True)
