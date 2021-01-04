from flask import Flask, abort, make_response, render_template, jsonify, request
from flask_cors import CORS
import db

app = Flask(__name__)
cors = CORS(app)
db.init()


@app.route('/')
def hello_world():
    return render_template('base.html.j2')


@app.route('/autores')
def autores():
    autores = db.get_autores()
    return render_template('autores.html.j2', autores=autores)


@app.route('/livros')
def livros():
    livros = db.get_livros()
    autores = db.get_autores()
    return render_template('livros.html.j2', livros=livros, autores=autores)


@app.route('/autor/<id>')
def autor_livros(id):
    id = 'autors/' + id
    autor, livros = db.get_livros_autor(id_autor=id)
    return render_template('autor_livros.html.j2', autor=autor, livros=livros)


@app.route('/autor', methods=['POST', 'PUT'])
def autor():
    if not request.json:
        abort(400)

    nome = request.json['nome']

    if request.method == 'POST':
        try:
            db.store_autor(nome)
            return make_response(jsonify({'success': True}), 201)
        except:
            return make_response(jsonify({'success': False}), 500)
    elif request.method == 'PUT':
        id_autor = request.json['autor']
        try:
            db.edit_autor(id_autor, nome)
            return make_response(jsonify({'success': True}), 200)
        except:
            return make_response(jsonify({'success': False}), 500)


@app.route('/livro', methods=['POST', 'PUT'])
def livro():
    if not request.json:
        abort(400)

    titulo = request.json['titulo']
    ano = request.json['ano']

    if request.method == 'POST':
        autor = request.json['autor']
        try:
            db.store_livro(titulo, ano, autor)
            return make_response(jsonify({'success': True}), 201)
        except:
            return make_response(jsonify({'success': False}), 500)
    elif request.method == 'PUT':
        id_livro = request.json['livro']
        try:
            db.edit_livro(id_livro, titulo, ano)
            return make_response(jsonify({'success': True}), 200)
        except:
            return make_response(jsonify({'success': False}), 500)


@app.route('/livro/<id_livro>', methods=["DELETE"])
def delete_livro(id_livro):
    id_livro = 'livroes/' + id_livro
    try:
        db.delete_livro(id_livro)
        return make_response(jsonify({'deleted': True}), 200)
    except:
        return make_response(jsonify({'deleted': False}), 500)


@app.route('/autor/del/<id_autor>', methods=["DELETE"])
def delete_autor(id_autor):
    id_autor = 'autors/' + id_autor
    try:
        db.delete_autor(id_autor)
        return make_response(jsonify({'deleted': True}), 200)
    except:
        return make_response(jsonify({'deleted': False}), 500)
