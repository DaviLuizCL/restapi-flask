# REST API FLASK

Uma REST API desenvolvida em Flask, integrada ao MongoDB e totalmente containerizada. Este projeto inclui um banco de dados mockado para desenvolvimento e utiliza o MongoDB Atlas para produção. O ambiente de desenvolvimento é gerenciado com Docker Compose, e a CI/CD é implementada usando Makefile e GitHub Actions, com o deploy realizado no Heroku.

## Tecnologias Utilizadas

- **Flask**: Para construção da REST API.
- **MongoDB Atlas**: Para banco de dados externo, permitindo escalabilidade e segurança.
- **Docker**: Para containerização da aplicação, garantindo que ela funcione em qualquer ambiente.
- **Docker Compose**: Para simplificar o gerenciamento do ambiente de desenvolvimento.
- **Makefile**: Para automação de tarefas e gerenciamento do fluxo de trabalho.
- **GitHub Actions**: Para integração e entrega contínua (CI/CD), facilitando o desenvolvimento e deployment da aplicação.
- **Heroku**: Para deployment da aplicação, permitindo acesso público e escalabilidade.

## Aprendizados

Durante o desenvolvimento deste projeto, aprendi:

- A criar uma API RESTful robusta utilizando Flask e integrar com MongoDB.
- A implementar práticas de CI/CD, utilizando GitHub Actions para automatizar o processo de build e deploy, o que aumentou a eficiência do fluxo de trabalho.
- A utilizar Docker e Docker Compose para containerizar a aplicação, o que facilita o desenvolvimento e a execução em ambientes isolados.
- A gerenciar um banco de dados em nuvem com MongoDB Atlas, permitindo um armazenamento seguro e acessível de dados.

## Como Rodar o Projeto

Para rodar o projeto localmente, siga os passos abaixo:

1. Clone o repositório:

   ```bash
   git clone https://github.com/DaviLuizCL/restapi-flask.git
   cd restapi-flask

2. Crie o ambiente virtual para as dependencias:

   ```bash
   python -m venv .venv

3. Instale as dependencias:

   ```bash
   pip3 install -r requirements.txt

4. Rode em ambiente de desenvolvimento:
    ```bash
    make compose
- Fique a vontade para entrar em contato!





