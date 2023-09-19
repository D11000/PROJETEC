from flask import Flask, render_template

app = Flask(__name__)

# Rotas

@app.route('/')
def index():
  return render_template('index.html', livros=livros, titulo='Página principal')

@app.route('/login')
def login():
  return render_template('login.html', titulo='Login')

@app.route('/register')
def register():
  return render_template('register.html', titulo='registro')

@app.route('/usuario')
def usuario():
  return render_template('usuario.html', titulo='Página do usuário')

@app.route('/cadastro')
def cadastro():
  return render_template('cadastro.html', titulo='Cadastro de livros')

@app.route('/hamburguer')
def hamburguer():
  return render_template('hamburguer.html')

@app.route('/sobre')
def sobre():
  return render_template('sobre.html')

@app.route('/recuperarsenha')
def recuperar():
  return render_template('rec_senha.html')
@app.route('/resultados')
def resultado():
  return render_template('Processa.php')


# - - - - - - - - - - - - - - - - - - - - - - - - - - -


# Criar novos livros


class livro:

  def __init__(self, titulo, sinopse, img, img2):
    self.titulo = titulo
    self.sinopse = sinopse
    self.img = img
    self.img2 = img2


def livrosemalta(arquivo):
  with open('emalta.txt', 'r' ,encoding="utf8") as arquivo:
    linhas = arquivo.readlines()

  num_linhas = len(linhas)
  num_livros = num_linhas // 4

  livros = []
  i = 0
  for _ in range(num_livros):
    titulo = linhas[i].strip()
    sinopse = linhas[i + 1].strip()
    img = linhas[i + 2].strip()
    img2 = linhas[i + 3].strip()
    livro_obj = livro(titulo, sinopse, img, img2)
    livros.append(livro_obj)
    i += 4

  return livros



def livrosrecentes(arquivo):
  with open('recentes.txt', 'r',encoding="utf8") as arquivo:
    linhas = arquivo.readlines()

  num_linhas = len(linhas)
  num_livros = num_linhas // 4

  livros = []
  l = 0
  for _ in range(num_livros):
    titulo = linhas[l].strip()
    sinopse = linhas[l + 1].strip()
    img = linhas[l + 2].strip()
    img2 = linhas[l + 3].strip()
    livro_obj = livro(titulo, sinopse, img, img2)
    livros.append(livro_obj)
    l += 4

  return livros



def livrosfamosos(arquivo):
  with open('famosos.txt', 'r',encoding="utf8") as arquivo:
    linhas = arquivo.readlines()

  num_linhas = len(linhas)
  num_livros = num_linhas // 4

  livros = []
  k = 0
  for _ in range(num_livros):
    titulo = linhas[k].strip()
    sinopse = linhas[k + 1].strip()
    img = linhas[k + 2].strip()
    img2 = linhas[k + 3].strip()
    livro_obj = livro(titulo, sinopse, img, img2)
    livros.append(livro_obj)
    k += 4

  return livros

livrosemalta = livrosemalta('emalta.txt')
livrosrecentes = livrosrecentes('recentes.txt')
livrosfamosos = livrosfamosos('famosos.txt')

livros = {
  'emalta': livrosemalta,
  'recentes': livrosrecentes,
  'famosos': livrosfamosos
}

# - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Dialog dinâmico









if __name__ == "__main__":

  app.run()