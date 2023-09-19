
<!DOCTYPE html>
<html lang="pt-BR">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Register Page</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='login-style.css') }}">
  <link rel="shortcut icon" href="/static/assets/logo invertida.png" type="image/x-icon">
  <script src="static/Database.js"></script>
  <link >
</head>

<body>
  <div class="container">
    <div class="card">
      <div class="col-md-6">
        <div class="imagem">
          <img class="login" src="{{url_for('static', filename='assets/Login.png')}}" alt="Login">
        </div>

      </div>
      <div class="col-md-6 text-section">
        <div class="logo-reg">
          <a href="{{ url_for('index') }}">
           <img src="{{url_for('static', filename='assets/logo invertida.png')}}" alt="Logo" />
          </a>
        </div>
        <p class="reg-text">Registro</p>
        <p class="reg-desc">Obrigado por entrar em nosso site!<br>Faça registro para começar a realizar seus pedidos.</p>
        <div class="section-inputs">
          <div class="inputs">
          <form action="processar_formulario.php" method="POST">
            
            <input class='imp-nome' type='text' placeholder='Nome' id="nm">
            
            <input class='imp-ra' type='text'placeholder='Registro Acadêmico'id="ra">
            <input class="imp-user" type="text" placeholder="Email" id="em">
            
            <input class="imp-pass" type="password" placeholder="Senha" id="ps">
     
          
          
          

            <div class="botao"
             <form id="form">
              <input class="btn-enter" type="submit" value="Entrar" id="inpu">
              </form>
            </div>
            <p class="registro">Já é membro? Efetue login clicando <a href="login">aqui.</a></p>
          </div>
        </div>
      </div>
    </div>
  </div>
</body>

</html>