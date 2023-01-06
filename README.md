# CRUD simples com FastAPI rodando em container Docker com Uvicorn + Testes Unitários com Pytest.
Esta é uma API bem simples com as funções básicas do processo de cadastro e manutenção de pessoas.</br>
Não utilizei nenhum banco de dados para armazenamento dos dados, apenas usei o BaseModel para criar uma classe do modelo de dados.</br>
Não implementei nenhuma verificação de segurança ou validação de usuário ou de dados, apenas quis demonstrar a facilidade para se criar uma API básica com poucas linhas e publicando e executando a app em um container **Docker**.

<div align="center">
<img width="455" src="https://i.imgur.com/UgfxPCg.png">
</div>

## Este projeto utiliza:

* [Python](https://www.python.org/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Pytest](https://docs.pytest.org/)
* [Uvicorn](https://www.uvicorn.org/)
* [Docker](https://www.docker.com/)

## Como executar este projeto localmente?

* Clone esse repositório: **git clone https://github.com/fspjonny/pessoas_fastapi_docker.git**<br>
* Baixe e instale o **Docker** no seu computador
* Tenha certeza que o Docker está executando em seu computador.
* Tenha certeza que os comandos `docker --version` e `docker-compose --version` estão funcionando no terminal do seu computador, conforme está abaixo.
<div align="center">
<img width="455" src="https://i.imgur.com/F55l9FY.png">
</div>


* O terminal de comando deve estar aberto no mesmo lugar onde estão os arquivos da aplicação:</br>
> - Dockerfile
> - docker-compose.yml
</br>

* Então na pasta raiz desta aplicação execute esta linha de comando abaixo:
</br>

`docker-compose up -d`
<div align="center">
<img width="455" src="https://i.imgur.com/uHD5BmR.png">
</div>

O processo de instalação do app e suas dependências no Docker se inicia.
<div align="center">
<img width="455" src="https://i.imgur.com/z3eAuz8.png">
</div>

</br>Ainda no mesmo terminal de comando execute o comando:
</br>

`docker container ps`
<div align="center">
<img width="455" src="https://i.imgur.com/QHRmBSi.png">
</div>

* Observe que a imagem acima mostra neste exemplo que a aplicação está rodando no localhost **(0.0.0.0:53320)**, este é o endereço e a porta disponibilizados e que deve se usado agora no seu navegador preferido, para executar a aplicação!</br>
O resultado é esta página inicial vista abaixo!
<div align="center">
<img width="455" src="https://i.imgur.com/ePGJWQu.png">
</div>

## Para executar os testes via Docker Desktop:
Com o container da aplicação em execução, abra um terminal de comandos e vá para pasta `proj` dentro do container e execute a linha de comando: `pytest -vv`.
</br>Os testes serão executados conforme a figura mostra abaixo.
<div align="center">
<img width="455" src="https://i.imgur.com/DcoCg8a.png">
</div>