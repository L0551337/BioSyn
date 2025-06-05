import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import random
from datetime import datetime, date

app = Flask(__name__)
app.secret_key = 'chave_secreta'

app.config.from_pyfile('config.py')
mysql = MySQL(app)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        existente = cursor.fetchone()
        if existente:
            flash('Email já cadastrado.')
            return redirect(url_for('cadastro'))

        cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)", (nome, email, senha))
        mysql.connection.commit()
        cursor.close()
        flash('Cadastro realizado com sucesso!')
        return redirect(url_for('login'))
    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id, nome, email FROM usuarios WHERE nome = %s AND senha = %s", (nome, senha))
        usuario = cursor.fetchone()
        cursor.close()

        if usuario:
            session['usuario_id'] = usuario[0]
            session['usuario_nome'] = usuario[1]
            session['usuario_email'] = usuario[2]
            return redirect(url_for('painel'))
        else:
            flash('Nome ou senha incorretos.')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/painel')
def painel():
    if 'usuario_email' not in session or 'usuario_nome' not in session:
        flash('Você precisa estar logado para acessar o painel.')
        return redirect(url_for('login'))
    return render_template('painel.html', nome=session['usuario_nome'], email=session['usuario_email'])

@app.route('/perfil')
def perfil():
    if 'usuario_email' not in session or 'usuario_nome' not in session:
        flash("Você precisa estar logado para acessar o perfil.")
        return redirect(url_for('login'))
    return render_template('perfil.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Você foi desconectado.')
    return redirect(url_for('login'))

@app.route('/atividades')
def atividades():
    if 'usuario_id' not in session:
        flash('Você precisa estar logado para acessar as atividades.')
        return redirect(url_for('login'))

    usuario_id = session['usuario_id']
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    cursor.execute("SELECT * FROM atividades WHERE usuario_id = %s AND DATE(data_geracao) = CURDATE()", (usuario_id,))
    atividades = cursor.fetchall()

    pode_gerar = len(atividades) == 0
    todas_concluidas = all(atividade['concluida'] for atividade in atividades) if atividades else False

    if todas_concluidas:
        cursor.execute("DELETE FROM atividades WHERE usuario_id = %s AND DATE(data_geracao) = CURDATE()", (usuario_id,))
        mysql.connection.commit()
        atividades = []

    cursor.close()
    return render_template('atividades.html', atividades=atividades, pode_gerar=pode_gerar, todas_concluidas=todas_concluidas)

@app.route('/gerar_atividades', methods=['POST'])
def gerar_atividades():
    if 'usuario_id' not in session:
        flash('Você precisa estar logado para gerar atividades.')
        return redirect(url_for('login'))

    usuario_id = session['usuario_id']
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    cursor.execute("SELECT COUNT(*) as total FROM atividades WHERE usuario_id = %s AND DATE(data_geracao) = CURDATE()", (usuario_id,))
    resultado = cursor.fetchone()
    if resultado['total'] > 0:
        flash('Você já gerou atividades hoje.')
        cursor.close()
        return redirect(url_for('atividades'))

    atividades_possiveis = {
        'Roseiras': [
            'Regar roseiras pela manhã',
            'Podar galhos secos das roseiras',
            'Adubar roseiras com composto orgânico'
        ],
        'Íris Azuis': [
            'Verificar umidade das íris azuis',
            'Expor íris azuis ao sol por 4 horas',
            'Limpar folhas das íris azuis'
        ],
        'Heras': [
            'Podar heras para controlar crescimento',
            'Regar heras em pouca quantidade',
            'Verificar presença de pragas nas heras'
        ],
        'Orquídeas': [
            'Regar orquídeas com moderação',
            'Expor orquídeas à luz indireta',
            'Fertilizar orquídeas a cada 15 dias'
        ],
        'Lavandas': [
            'Podar lavandas para estimular crescimento',
            'Regar lavandas quando o solo estiver seco',
            'Colher flores de lavandas para secagem'
        ],
        'Samambaias': [
            'Pulverizar água nas folhas das samambaias',
            'Evitar luz solar direta nas samambaias',
            'Verificar se as samambaias estão saudáveis'
        ]
    }

    hoje = datetime.now().date()
    for planta, tarefas in atividades_possiveis.items():
        descricao = random.choice(tarefas)
        cursor.execute("INSERT INTO atividades (usuario_id, descricao, data_geracao, concluida) VALUES (%s, %s, %s, %s)", (usuario_id, descricao, hoje, False))

    mysql.connection.commit()
    cursor.close()
    flash('Atividades geradas com sucesso!')
    return redirect(url_for('atividades'))

@app.route('/concluir_atividade/<int:id>', methods=['POST'])
def concluir_atividade(id):
    if 'usuario_id' not in session:
        flash('Você precisa estar logado para concluir atividades.')
        return redirect(url_for('login'))

    usuario_id = session['usuario_id']
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE atividades SET concluida = TRUE WHERE id = %s AND usuario_id = %s", (id, usuario_id))
    cursor.execute("SELECT COUNT(*) FROM atividades WHERE usuario_id = %s AND DATE(data_geracao) = CURDATE() AND concluida = FALSE", (usuario_id,))
    pendentes = cursor.fetchone()[0]

    if pendentes == 0:
        cursor.execute("DELETE FROM atividades WHERE usuario_id = %s AND DATE(data_geracao) = CURDATE()", (usuario_id,))
        flash('Todas as atividades foram concluídas e removidas!')

    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('atividades'))

@app.route('/guias')
def guias():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT id, nome, descricao, imagem_url, valor_vaso FROM plantas")
    plantas = cursor.fetchall()
    cursor.close()
    return render_template('guias.html', plantas=plantas)


@app.route('/guia/<int:planta_id>')
def guia_detalhes(planta_id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT nome, descricao, imagem_url FROM plantas WHERE id = %s", (planta_id,))
    planta = cursor.fetchone()
    cursor.close()
    if not planta:
        flash("Planta não encontrada.")
        return redirect(url_for('guias'))
    return render_template('guia_detalhes.html', planta=planta)

@app.route('/adicionar_planta', methods=['GET', 'POST'])
def adicionar_planta():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        valor_vaso = request.form['valor_vaso']
        imagem = request.files['imagem']
        
        if imagem:
            imagem_filename = imagem.filename
            imagem_path = os.path.join('C:/Users/enzol/OneDrive/Documentos/vscode/webdev/Unialfa/BioSyn/BioSyn/static/images', imagem_filename)
            imagem.save(imagem_path)

            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO plantas (nome, descricao, imagem_url, valor_vaso) VALUES (%s, %s, %s, %s)",
                           (nome, descricao, imagem_filename, valor_vaso))
            mysql.connection.commit()
            cursor.close()

            return redirect(url_for('guias'))

    return render_template('adicionar_planta.html')

@app.route('/excluir_planta/<int:planta_id>', methods=['POST'])
def excluir_planta(planta_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM plantas WHERE id = %s", (planta_id,))
    mysql.connection.commit()
    cursor.close()
    flash("Planta excluída com sucesso.")
    return redirect(url_for('guias'))


if __name__ == '__main__':
    app.run(debug=True)

