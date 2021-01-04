const baseUrl = 'http://localhost:5000/';

const postLivro = (livro) => {
    axios.post(baseUrl + 'livro', livro)
        .then(res => {
            if(res.status == 201) {
                window.location.reload();
            }
        }).catch(err => console.log(err));
}

function novoLivro() {
    let titulo = document.getElementById('titulo').value;
    let ano = parseInt(document.getElementById('ano').value);
    let autor = document.getElementById('select-autor').value;

    let livro = {
        titulo: titulo,
        ano: ano,
        autor: autor
    };
    postLivro(livro);
}

function novoLivroAutor() {
    let titulo = document.getElementById('tituloA').value;
    let ano = parseInt(document.getElementById('anoA').value);
    let autor = document.getElementById('autorA').value;

    let livro = {
        titulo: titulo,
        ano: ano,
        autor: autor
    };
    postLivro(livro);
}

function excluirLivro(id_livro) {
    axios.delete(baseUrl + 'livro/' + id_livro)
        .then(res => {
            if(res.status == 200) {
                window.location.reload();
            }
        }).catch(err => console.log(err));
}

function modalLivro(id_livro, titulo, ano) {
    document.getElementById('edit-livro').value = id_livro;
    document.getElementById('edit-titulo').value = titulo;
    document.getElementById('edit-ano').value = ano;
}

function editarLivro() {
    let id_livro = document.getElementById('edit-livro').value;
    let titulo = document.getElementById('edit-titulo').value;
    let ano = parseInt(document.getElementById('edit-ano').value);

    const livro = {
        livro: id_livro,
        titulo: titulo,
        ano: ano
    };

    axios.put(baseUrl + 'livro', livro)
        .then(res => {
                if(res.status == 200) {
                    window.location.reload();
                }
            }).catch(err => console.log(err));
}