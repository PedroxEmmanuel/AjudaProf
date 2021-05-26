from Facul.Projeto_Engenharia import bd
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def primeira_tela():
    return render_template('primeira_tela.html')


# rotas do prof começam aqui
@app.route('/login_p')
def login_professor():
    return render_template('login_p.html')


@app.route('/menu_principal_prof', methods=['POST'])
def menu_principal_prof():
    # pega oq o prof digitou no usuario e senha
    usuario_p = int(request.form['usuario_p'])
    senha_p = request.form['senha_p']

    # abre o banco de dados
    mysql = bd.SQL("08ezYU3bp0", "owSllN0RD4", "remotemysql.com", "08ezYU3bp0")

    # puxa do banco de dados daquele usuário(idt) o usuario e senha para validar
    comando = f"SELECT matricula_professor AS usuario, senha_professor AS senha FROM tb_professor " \
              f"WHERE matricula_professor=%s;"
    cs = mysql.consultar(comando, [usuario_p])

    # se existir a matricula no banco de dados que o usuario digitou, esta ficará armazenada em dados, se n, vai entra
    # na primeira condiçao onde retornará dados invalidos
    dados = cs.fetchone()
    if dados is None:
        msg = "não entrou, não ha usuario nem senha"
        return render_template('menu_principal_prof.html', msg=msg)
    usuario = dados[0]
    senha = dados[1]
    cs.close()

    # abaixo haverá a validação: comparando oq o usuario digitou e oq está no banco de dados
    if usuario == usuario_p and senha == senha_p:
        msg = "entrou"
        return render_template('menu_principal_prof.html', msg=msg)
    elif usuario != usuario_p or senha != senha_p:
        msg = "não entrou"
        return render_template('menu_principal_prof.html', msg=msg)


@app.route('/alterar_notas')
def alterar_notas():
    pass


@app.route('/alterar_presença')
def alterar_presenca():
    pass


@app.route('/editar_perfil')
def editar_perfil():
    pass


# rotas do prof acabam aqui
# rotas do aluno começam aqui

@app.route('/login_a')
def login_aluno():
    return render_template('login_a.html')


@app.route('/menu_principal_aluno', methods=['POST'])
def menu_principal_aluno():
    # pega oq o aluno digitou no usuario e senha
    usuario_a = int(request.form['usuario_a'])
    senha_a = request.form['senha_a']

    # abre o banco de dados
    mysql = bd.SQL("08ezYU3bp0", "owSllN0RD4", "remotemysql.com", "08ezYU3bp0")

    # puxa do banco de dados daquele usuário(idt) o usuario e senha para validar
    comando = f"SELECT matricula_aluno AS usuario, senha_aluno AS senha FROM tb_aluno " \
              f"WHERE matricula_aluno=%s;"
    cs = mysql.consultar(comando, [usuario_a])

    # se existir a matricula no banco de dados que o usuario digitou, esta ficará armazenada em dados,
    # se n, vai entra na primeira condiçao onde retornará dados invalidos
    dados = cs.fetchone()
    if dados is None:
        msg = "não entrou, não ha usuario nem senha"
        return render_template('menu_principal_prof.html', msg=msg)
    usuario = dados[0]
    senha = dados[1]

    # abaixo haverá a validação: comparando oq o usuario digitou e oq está no banco de dados
    if usuario == usuario_a and senha == senha_a:
        msg = "entrou"
        return render_template('menu_principal_prof.html', msg=msg)
    elif usuario != usuario_a or senha != senha_a:
        msg = "não entrou"
        return render_template('menu_principal_prof.html', msg=msg)


@app.route('/')
def a():
    pass


@app.route('/')
def b():
    pass


# rotas do aluno acabam aqui
# rotas do responsavel começam aqui

@app.route('/login_r')
def login_responsaveis():
    return render_template('login_r.html')


@app.route('/menu_principal_resp', methods=['POST'])
def menu_principal_resp():
    # pega oq o prof digitou no usuario e senha
    usuario_r = int(request.form['usuario_r'])

    # abre o banco de dados
    mysql = bd.SQL("08ezYU3bp0", "owSllN0RD4", "remotemysql.com", "08ezYU3bp0")

    # puxa do banco de dados daquele usuário(idt) o usuario e senha para validar
    comando = f"SELECT cpf_responsavel AS cpf FROM tb_responsavel " \
              f"WHERE cpf_responsavel=%s;"
    cs = mysql.consultar(comando, [usuario_r])

    # se existir a matricula no banco de dados que o usuario digitou, esta ficará armazenada em dados,
    # se n, vai entra na primeira condiçao onde retornará dados invalidos
    dados = cs.fetchone()
    if dados is None:
        msg = "não entrou, não ha usuario nem senha"
        return render_template('menu_principal_prof.html', msg=msg)
    usuario = dados[0]

    # abaixo haverá a validação: comparando oq o usuario digitou e oq está no banco de dados
    if usuario == usuario_r:
        msg = "entrou"
        return render_template('menu_principal_prof.html', msg=msg)
    elif usuario != usuario_r:
        msg = "não entrou"
        return render_template('menu_principal_prof.html', msg=msg)


# rotas do responsavel acabam aqui

if __name__ == '__main__':
    app.run(host="localhost", port=25565)
