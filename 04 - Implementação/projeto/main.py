from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from app import app, db
from app.models import Professor


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nme_professor = request.form['nme_professor']
        senha_professor = request.form['senha_professor']
        matricula_professor = int(request.form['matricula_professor'])
        formacao_professor = request.form['formacao_professor']
        nasc_professor = request.form['nasc_professor']
        sangue_professor = request.form['sangue_professor']
        disc_professor = request.form['disc_professor']

        professor = Professor(nme_professor, senha_professor, matricula_professor, formacao_professor, nasc_professor, sangue_professor, disc_professor)
        db.session.add(professor)
        db.session.commit()
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/menu', methods=['GET', 'POST'])
def menu():
    if request.method == 'POST':
        matricula_professor = request.form['matricula_professor']
        senha_professor = request.form['senha_professor']

        professor = Professor.query.filter_by(matricula_professor=matricula_professor).first()

        if not professor or not professor.verify_password(senha_professor):
            return redirect(url_for('login'))

        login_user(professor)
        return redirect(url_for('home'))


@app.route('/alterar', methods=['GET', 'POST'])
def alterar():
    msg = "não entrou, não ha usuario nem senha"
    return render_template('alterar.html', msg=msg)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

app.run(debug=True)