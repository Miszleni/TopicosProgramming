# Aula 2

Finalizar os Testes práticos:

Tools.

Exemplos: **Search Tools** **GPTs**

VPS, Docker, Domínio e DNS (Cloudflare)?
1. VPS, domínios (Registrar dominio)
2. Criar conta na cloudflare e registrar domínio


username:tep
senha:tep123


## Docker

Docker é uma plataforma open source que possibilita o empacotamento de uma aplicação dentro de um container. Uma aplicação consegue se adequar e rodar em qualquer máquina que tenha essa tecnologia instalada.

### Porque usar WSL 2 + Docker para desenvolvimento

Configurar ambientes de desenvolvimento no Windows sempre foi burocrático e complexo, além do desempenho de algumas ferramentas não serem totalmente satisfatórias.

Com o nascimento do Docker este cenário melhorou bastante, pois podemos montar nosso ambiente de desenvolvimento baseado em Unix, de forma independente e rápida, e ainda unificada com outros sistemas operacionais.

## Modos de usar Docker no Windows

### Docker Desktop com WSL2

Roda em cima do **Virtual Machine Platform** que é um componente do Hyper-V e se integra com o WSL2 permitindo rodar o Docker dentro do ambiente do Linux.

Não é necessário adquirir licença PRO do Windows 10/11.

Tem um grande desempenho e consome menos recursos quando comparado ao Docker Toolbox ou Docker Desktop com Hyper-V.

#### Algumas Vantagens

- Tem uma ferramenta visual para administrar o Docker.
- Permite instalar extensões para usar ferramentas diretas no Docker.
- Permite rodar um cluster Kubernetes localmente de forma fácil.
- Simplifica a configuração do Docker tanto no Windows quanto no WSL 2.

#### Algumas Desvantagens

- Uso de memória inicial sem rodar nenhum container Docker é de 1GB ou mais.
- Pode ser necessário reiniciar o Docker Desktop para que ele funcione corretamente em algumas situações.
- Tende a consumir mais recursos da máquina que o Docker Engine diretamente instalado no WSL 2.
- 
### Docker Engine (Docker Nativo) diretamente instalado no WSL2


O Docker Engine é o Docker nativo (como foi criado) que roda no ambiente Linux e completamente suportado para WSL 2. Sua instalação é idêntica a descrita para as próprias distribuições Linux disponibilizadas no site do [Docker](https://docs.docker.com/engine/install/ubuntu/).

É a maneira pura de usar o Docker no Linux.

#### Algumas Vantagens

- Consume menos memória para rodar o Docker Daemon (servidor do Docker) quando comparado ao Docker Desktop.
- Traz a experiência mais pura de usar o Docker no Linux.
#### Algumas Desvantagens

- Se necessitar executar o Docker em outra instância do WSL 2, é necessário instalar novamente o Docker nesta instância ou configurar o acesso ao socket do Docker desejado para compartilhar o Docker entre as instâncias.

### 2 - Instalar o Docker com Docker Engine (Docker Nativo)


A instalação do Docker no WSL 2 é idêntica a instalação do Docker em sua própria distribuição Linux, portanto se você tem o Ubuntu é igual ao Ubuntu, se é Fedora é igual ao Fedora. A documentação de instalação do Docker no Linux por distribuição está [aqui](https://docs.docker.com/engine/install/), mas vamos ver como instalar no Ubuntu.

![[Pasted image 20240822100956.png]]

## Instalar/Atualizar o WSL

Com a versão 2004 do Windows 10 ou Windows 11, o WSL já estará presente em sua máquina, execute o comando para pegar a versão mais recente do WSL:

```shell
wsl --update
```

### Atribuir a versão default do WSL para a versão 2

A versão 2 normalmente é a default, mas a versão 1 do WSL pode estar como default, execute o comando abaixo para definir como default a versão 2:

```shell
wsl --set-default-version 2
```

### Instale o Ubuntu

Execute o comando:

```shell
wsl --install
```

Este comando irá instalar o `Ubuntu` como o Linux padrão.

Se você quiser instalar uma versão diferente do Ubuntu, execute o comando `wsl -l -o`. Será listado todas as versões de Linux disponíveis. Instale a versão escolhida com o comando `wsl --install -d nome-da-distribuicao`.

## O que o WSL 2 pode usar de recursos da sua máquina

Podemos dizer que o WSL 2 tem acesso quase que total ao recursos de sua máquina. Ele tem acesso por padrão:

- A 1TB de disco rígido. É criado um disco virtual de 1TB para armazenar os arquivos do Linux (este limite pode ser expandido, ver a área de dicas e truques).
- A usar completamente os recursos de processamento.
- A usar 50% da memória RAM disponível.
- A usar 25% da memória disponível para SWAP (memória virtual).

Se você quiser personalizar estes limites, crie um arquivo chamado `.wslconfig` na raiz da sua pasta de usuário `(C:\Users\<seu_usuario>)` e defina estas configurações:

```
[wsl2]
memory=8GB
processors=4
```

## Instalando Docker

https://docs.docker.com/engine/install/ubuntu/

### [Install using the `apt` repository](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

Before you install Docker Engine for the first time on a new host machine, you need to set up the Docker repository. Afterward, you can install and update Docker from the repository.

1. Set up Docker's `apt` repository.
    
    ```bash
    # Add Docker's official GPG key:
    sudo apt-get update
    sudo apt-get install ca-certificates curl
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc
    
    # Add the repository to Apt sources:
    echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
      $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
      sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
    ```
    
1. Install the Docker packages.
    
    Latest Specific version  
    To install the latest version, run:
    
    ```console
    $ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ```
    
2. Verify that the Docker Engine installation is successful by running the `hello-world` image.
    
    ```console
    $ sudo docker run hello-world
    ```

**Fazer Ate aqui**

```
https://github.com/codeedu/wsl2-docker-quickstart
https://learn.microsoft.com/pt-br/windows/terminal/install
```



### Como Containerizar uma Aplicação Node.js ?

A containerização de aplicativos é uma técnica poderosa que permite isolar e empacotar aplicativos com todas as suas dependências em contêineres(containers). O Docker é uma das ferramentas mais populares para realizar essa tarefa, e vamos ter fornecer um guia onde você aprenderá como containerizar uma aplicação Node.js usando o Docker. Vamos explorar o processo passo a passo, desde os pré-requisitos até a execução da aplicação no Docker.

#### Pré-requisitos

Antes de mergulharmos na containerização, é importante garantir que você tenha algumas coisas em ordem:

1. **Docker Desktop**: Certifique-se de ter a versão mais recente do Docker Desktop instalada em seu sistema. Você pode baixá-lo em [Docker Desktop](https://www.docker.com/products/docker-desktop).
2. **Cliente Git**: Os exemplos deste guia usam um cliente Git baseado em linha de comando. Certifique-se de ter um cliente Git instalado em seu sistema. Você pode usar qualquer cliente Git de sua preferência.

#### Passo 1: Obtenha a amostra da aplicação

A primeira etapa é obter a aplicação de amostra. Vamos usar um exemplo que o próprio docker nos fornece.

Abra um terminal, vá para o diretório onde deseja trabalhar e execute o seguinte comando para clonar o repositório:

```bash
git clone https://github.com/docker/docker-nodejs-sample
apt install nodejs
apt install npm
```


#### Passo 2: Teste a aplicação sem o Docker (opcional)

Antes de prosseguir com a containerização, é uma boa prática testar a aplicação localmente sem o Docker. Para fazer isso, siga estas etapas:

- Certifique-se de ter o Node.js 18 instalado em sua máquina. Você pode baixá-lo em [Node.js](https://nodejs.org/).
- Abra um terminal, vá para o diretório 'docker-nodejs-sample' e execute o seguinte comando para instalar as dependências:

```
$ npm install

```

- Quando as dependências terminarem de instalar, execute o seguinte comando para iniciar a aplicação:

```
$ node src/index.js

```

- Abra um navegador e acesse a aplicação em [http://localhost:3000](http://localhost:3000/). Você deverá ver uma aplicação de lista de tarefas simples.
- No terminal, pressione Ctrl+C para parar a aplicação.

## Passo 3: Inicialize os recursos do Docker

Agora que você tem uma aplicação, podemos iniciar o processo de containerização. Dentro do diretório 'docker-nodejs-sample', execute o comando 'docker init' em um terminal e siga as instruções:


### Crie um Dockerfile
Crie um arquivo chamado `Dockerfile` na pasta principal do seu projeto. Este arquivo irá conter as instruções para construir a imagem Docker do seu projeto.

```bash
# Use uma imagem base oficial do Node.js
FROM node:14

# Defina o diretório de trabalho dentro do container
WORKDIR /usr/src/app

# Copie o arquivo package.json e package-lock.json (se existir)
COPY package*.json ./

# Instale as dependências do projeto
RUN npm install

# Copie o restante do código do projeto
COPY . .

# Exponha a porta que o aplicativo Node.js estará escutando
EXPOSE 3000

# Comando para rodar o aplicativo
CMD ["node", "src/index.js"]
```

### **Crie um arquivo `.dockerignore`**


```bash
node_modules
npm-debug.log
Dockerfile
.dockerignore
```

### Construa a Imagem Docker

No terminal, navegue até a pasta principal do seu projeto e execute o seguinte comando para construir a imagem Docker:

```bash
docker images
docker build -t meu-app-node .
```

### **Execute o Container**:  
Após a construção da imagem, você pode executar um container a partir dela com o seguinte comando:

```bash
docker images
docker run -p 3000:3000 meu-app
docker run -p 3000:3000 -d meu-app
docker ps
docker stop
docker rm CONTAINERID
docker rmi -f meu-app
```

Isso mapeará a porta 3000 do container para a porta 3000 do seu host, permitindo que você acesse o aplicativo Node.js em `http://localhost:3000`

### Utilizando o Docker compose

Utilizar o Docker Compose é uma ótima maneira de gerenciar múltiplos containers Docker de forma orquestrada, especialmente útil para aplicativos que dependem de vários serviços, como bancos de dados, servidores de cache, etc. Aqui estão os passos para configurar e usar o Docker Compose com seu projeto Node.js:

Certifique-se de que o Docker Compose está instalado no seu sistema. Você pode verificar isso com o comando:

```bash
docker compose version
```

**Crie um arquivo `docker-compose.yml`**:

```d
version: '3'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    volumes:
      - .:/usr/src/app
    environment:
      - NODE_ENV=production
```


**Construa e Execute os Serviços**:  
No terminal, navegue até a pasta principal do seu projeto e execute o seguinte comando para construir e iniciar os serviços definidos no `docker-compose.yml`:

```
docker compose up --build
```

**Verifique os Serviços**:

```bash

docker compose ps
#parar serviço
docker compose down
```

- Use `docker-compose up -d` quando quiser iniciar os serviços usando as imagens já construídas, sem reconstruir as imagens.
    
- Use `docker-compose up --build -d` quando quiser garantir que as imagens sejam reconstruídas antes de iniciar os serviços, o que é útil após fazer alterações no código-fonte ou no Dockerfile.


### Exemplo de um arquivo com dois serviços

```d
version: '3'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    volumes:
      - .:/usr/src/app
    environment:
      - NODE_ENV=production

  db:
    image: mysql:8
    ports:
      - "3306:3306"
    environment:
      - MYSQL_ROOT_PASSWORD=mysecretpassword
      - MYSQL_DATABASE=mydatabase
      - MYSQL_USER=myuser
      - MYSQL_PASSWORD=mypassword
```

As variáveis de ambiente correspondem às necessidades do MySQL:

- `MYSQL_ROOT_PASSWORD`: Define a senha do usuário root.
    
- `MYSQL_DATABASE`: Define o nome do banco de dados que será criado.
    
- `MYSQL_USER`: Define o nome de um usuário não-root que será criado.
    
- `MYSQL_PASSWORD`: Define a senha para o usuário não-root.

#### Referência:
https://blog.rocketseat.com.br/containerizando-uma-aplicacao-node-js-com-docker-um-guia-passo-a-passo/