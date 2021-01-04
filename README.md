# Flask-RavenDB-CRUD

## Introdução

Aplicação web para demonstrar operações CRUD no banco de dados NoSQL [RavenDB](https://ravendb.net).

Nesta aplicação, temos duas "entidades", autores e livros. O objetivo é listar os conteúdos salvos no banco, além de adicionar, editar e excluir autores e livros. Também é possível realizar uma consulta com cláusula where, na qual são listados todos os livros de um dado autor.

## Instalação e configuração

A aplicação é feita em Python utilizando o microframework Flask e o cliente oficial do RavenDB para a linguagem. Portanto, além de uma instância do banco de dados, é necessário ter o Python 3 e o gerenciador de pacotes pip instalado na máquina.

### Banco de dados

O [site oficial do RavenDB](https://ravendb.net/download) oferece todas as instruções para instalação e configuração do banco de dados, além de download gratuito para Windows, Linux, macOS, Raspberry Pi e Docker.

De qualquer maneira, é preciso fazer o download para a sua plataforma e, após extrair os dados (eles vem compactados em .zip), executar o script `run.ps1` no Windows (Powershell) ou `run.sh` no Linux (bash). Alternativamente, é possível utilizar o banco através de uma imagem do Docker:

```bash
docker run -d -p 8080:8080 -p 38888:38888 ravendb/ravendb
```

Após isso, basta acessar `localhost:8080` no navegador e concluir a configuração do servidor através da interface web.

Após ter configurado o servidor, utilize o [Management Studio](https://ravendb.net/docs/article-page/5.1/csharp/studio/overview) para criar um novo banco de dados chamado Livros, que pode ficar vazio por enquanto.

### Dependências e ambiente

Para instalar as packages necessárias para executar o projeto, execute o comando:

```bash
pip install -r requirements.txt
```

Após a instalação das packages, configure o Flask para rodar a aplicação localmente em modo de desenvolvimento. No Linux:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```

Outro detalhe que deve receber atenção é a url para conexão com o banco de dados. Se a sua configuração manteve a porta padrão do RavenDB (`localhost:8080`), não precisa modificar nada. Mas, caso tenha utilizado uma porta diferente ou esteja utilizano o ip de outra máquina na rede, defina a variável de ambiente `RAVENDB_URL` com o endereço no formato `http://<ip>:<porta>`. Por exemplo:

```bash
export RAVENDB_URL=http://192.168.1.100:9000
```

### Executando

Finalmente, para executar a aplicação:

```bash
flask run
```

Por padrão, ela deverá estar disponível no endereço http://127.0.0.1:5000.