//Importar o modulo MongoClient

const { MongoClient } = require("mongodb");

//Função principal

async function main() {
  //Definir a URL de conexão com o MongoDB

  const uri = "mongodb://127.0.0.1:27017";

  //Criar instancia do cliente mongoDB

  const client = new MongoClient(uri);

  try {
    //Conecta com o servidor MongoDB

    await client.connect();

    //Seleciona o banco de dados "biblioteca"

    const database = client.db("biblioteca");

    //Selecione a coleção "livros"

    const livros = database.collection("livros");

    // await livros.insertMany([
    //   { titulo: "1984", autor: "George Orwell", ano: 1949, genero: "Distopia" },

    //   {
    //     titulo: "Dom Casmurro",
    //     autor: "Machado de Assis",
    //     ano: 1899,
    //     genero: "Romance",
    //   },

    //   {
    //     titulo: "Senhor dos Aneis",
    //     autor: "J.R.R. Tolkein",
    //     ano: 1954,
    //     genero: "Fantasia",
    //   },
    // ]);

    //Atualização de Documento
   // await livros.updateOne({titulo: "1984"},{$set: {ano:1950}})

   //Excluir um documento do Banco de Dados
    //await livros.deleteOne({titulo: "Dom Casmurro"})


    const todosLivros = await livros.find().toArray()
    console.log('Livros: ',todosLivros);
  } finally {
    await client.close();
  }
}

//Chama a função principal e captura o erro, se houver

main().catch(console.error);
