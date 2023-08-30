## Imagem Docker do MySQL
Este README fornece informações sobre como usar a imagem oficial do MySQL Docker.
Para iniciar uma instância do servidor MySQL, você pode usar o seguinte comando:

```
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:tag
```

Onde _some-mysql_ é o nome que você deseja atribuir ao seu contêiner, _my-secret-pw_ é a senha a ser definida para o usuário root do MySQL e _tag_ é a tag especificando a versão do MySQL que você deseja.

Conectando ao MySQLVocê pode se conectar ao servidor MySQL a partir do cliente de linha de comando do MySQL usando o seguinte comando:
```
docker run -it --network some-network --rm mysql mysql -hsome-mysql -uexample-user -p
```
Onde _some-mysql_ é o nome do seu contêiner MySQL original (conectado à rede Docker some-network).
Esta imagem também pode ser usada como cliente para instâncias não-Docker ou remotas:
```
docker run -it --rm mysql mysql -hsome.mysql.host -usome-mysql-user -p
```
Mais informações sobre o cliente de linha de comando do MySQL podem ser encontradas na https://dev.mysql.com/doc/refman/8.1/en/mysql.html.

Você também pode usar o ```docker-compose``` para iniciar uma instância do servidor MySQL.

Para obter mais informações sobre como usar a imagem oficial do MySQL Docker, consulte a https://hub.docker.com no Docker Hub.

## Programa

Este repositório contém um código que demonstra uma interação entre cliente e servidor, envolvendo a requisição de informações de um banco de dados. 
O objetivo é fornecer um sistema simples em que um cliente envia solicitações ao servidor para obter questões armazenadas no banco de dados. Após receber as questões, o cliente as responde, e em seguida, apresenta os resultados com base nas respostas fornecidas pelo cliente.

### Funcionalidades
- O cliente se conecta ao servidor para requisitar questões armazenadas no banco de dados.
- O servidor processa a solicitação do cliente e envia as questões requisitadas.
- O cliente responde às questões recebidas do servidor.
- Após receber as respostas do cliente, são avaliadas as respostas e apresentados os resultados.