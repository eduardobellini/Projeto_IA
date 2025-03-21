import chromadb

# Inicializa o banco
db = chromadb.PersistentClient(path="./banco_ia")

# Cria uma coleção para armazenar os textos
colecao = db.get_or_create_collection("livros")

# Adiciona um exemplo
colecao.add(
    documents=["A inteligência artificial é um campo da ciência que..."],
    ids=["livro_1"]
)

# Buscar um livro pelo ID
print(colecao.get(ids=["livro_1"]))
