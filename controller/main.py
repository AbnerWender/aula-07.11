from model.livros import Livros
from model.usuario import Usuario
from model.biblioteca import Biblioteca
from controller.controllerLivro import ControllerLivros

controladora = ControllerLivros()

controladora.cadastrarLivro()