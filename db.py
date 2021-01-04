from pyravendb.store import document_store
from models import Autor, Livro
import os


def init():
    ravendb_url = os.environ['RAVENDB_URL']
    urls = [ravendb_url]
    global store
    store = document_store.DocumentStore(urls=urls, database="Livros")
    store.initialize()


def get_autores():
    with store.open_session() as session:
        autores = list(session.query(
            collection_name="Autors").select("id() as id", "nome").order_by("nome"))
        return autores


def store_autor(nome):
    with store.open_session() as session:
        autor = Autor(nome)
        session.store(autor)
        session.save_changes()


def store_livro(titulo, ano, autor):
    with store.open_session() as session:
        livro = Livro(titulo, ano, autor)
        session.store(livro)
        session.save_changes()


def get_livros():
    with store.open_session() as session:
        livros = list(session.query(collection_name="Livroes").select(
            "id() as id", "titulo", "ano", "autor").order_by("titulo"))
        for l in livros:
            autor = session.load(l.autor)
            l.autor = {'id': l.autor, 'nome': autor.nome}
        return livros


def get_livros_autor(id_autor):
    with store.open_session() as session:
        autor = session.load(id_autor)
        autor.id = id_autor
        livros = list(session.query(collection_name="Livroes").select(
            "id() as id", "titulo", "ano").where(autor=id_autor).order_by("titulo"))
        return autor, livros


def delete_livro(id_livro):
    with store.open_session() as session:
        session.delete(id_livro)
        session.save_changes()


def delete_autor(id_autor):
    with store.open_session() as session:
        livros = list(session.query(collection_name="Livroes").select(
            "id() as id").where(autor=id_autor))
        for livro in livros:
            session.delete(livro.id)
        session.delete(id_autor)
        session.save_changes()


def edit_autor(id_autor, nome):
    with store.open_session() as session:
        autor = session.load(id_autor)
        autor.nome = nome
        session.save_changes()


def edit_livro(id_livro, titulo, ano):
    with store.open_session() as session:
        livro = session.load(id_livro)
        livro.titulo = titulo
        livro.ano = ano
        session.save_changes()