
## Workshop Fast API

### Iniciando o projeto

Clonar o projeto

```bash
  git clone https://github.com/Ecossistema-Conecta/ChallengeFastAPI
```

Acesse o diretório do projeto

```bash
  cd ChallengeFastAPI
```

Instale as dependências

```bash
  docker compose build
```

Suba o projeto

```bash
  docker compose up -d
```

### Instruções

Abra a url http://localhost:8000/challenge e leia as instruções para o desafio.

Para o envio de email de feedback funcionar corretamente é preciso cadastrar a chave do SENDGRID no arquivo app.utils.constants.
