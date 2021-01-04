const baseUrlAutor = 'http://localhost:5000/';

function novoAutor() {
    let nome = document.getElementById('nome_autor').value;
    axios.post(baseUrlAutor + 'autor', {nome: nome})
        .then(res => {
            if(res.status == 201) {
                window.location.reload();
            }
        }).catch(err => console.log(err));
}

function excluirAutor(id_autor) {
    axios.delete(baseUrlAutor + 'autor/del/' + id_autor)
        .then(res => {
            if(res.status == 200) {
                window.location.reload();
            }
        }).catch(err => console.log(err));
}

function modalAutor(id_autor, nome) {
    document.getElementById('edit-autor').value = id_autor;
    document.getElementById('edit-nome').value = nome;
}

function editarAutor() {
    let id_autor = document.getElementById('edit-autor').value;
    let nome = document.getElementById('edit-nome').value;

    const autor = {
        autor: id_autor,
        nome: nome,
    };

    axios.put(baseUrlAutor + 'autor', autor)
        .then(res => {
                if(res.status == 200) {
                    window.location.reload();
                }
            }).catch(err => console.log(err));
}