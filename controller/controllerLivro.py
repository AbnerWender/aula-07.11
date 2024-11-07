from model.livros import Livros
from config.database import Database

class ControllerLivros:
    def __init__(self):
        self.bd = Database("localhost", "root", "", "biblioteca2")

    def cadastrarLivro(self):
        self.bd.conectar()

        self.livro = Livros("Dom Casmurro", "Machado de Assis", "Suspense", 123)
        self.bd.cursor.execute(self.livro.create())
        self.bd.conexao.commit()
        self.bd.desconectar()

    def procurarLivro(self):
        self.bd.conectar()

        self.livro = Livros("Dom Casmurro", "Machado de Assis", "Suspense", 123)
        self.bd.conexao.execute(self.livro.read())
        resultado = self.bd.cursor.fetchall()
        self.bd.desconectar() 
        print(resultado)

        