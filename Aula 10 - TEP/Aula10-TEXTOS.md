# Aula 10

Instalação do N8n


## APIS do WhatsApp
### go-whatsapp-web-multidevice

- Send WhatsApp message via http API, 
- [docs/openapi.yml](https://github.com/aldinokemal/go-whatsapp-web-multidevice/blob/main/docs/openapi.yaml) for more details
- Compress image before send
- Compress video before send

Arquivo: docker-compose.yaml

```bash
version: '3.9'
services:
  whatsapp_go:
    logging:
      driver: "json-file"
      options:
        max-size: "200k"
        max-file: "10"
    image: "aldinokemal2104/go-whatsapp-web-multidevice:latest"
    build:
      context: .
      dockerfile: ./docker/golang.Dockerfile
    restart: 'always'
    ports:
      - "3100:3000"
    environment:
      - WEBHOOK="https://n8n.semcodigo.edu.pl/webhook-test/consultavendas"
    volumes:
      - whatsapp_data:/app/storages

volumes:
  whatsapp_data:
```




```bash
sudo docker run --detach --publish=3001:3000 --name=whatsapp2 --restart=always --volume=$(sudo docker volume create --name=whatsapp2):/app/storages aldinokemal2104/go-whatsapp-web-multidevice --autoreply="Don't reply this message please" --webhook="http://localhost:5678/webhook-test/whats"
```


### Evolution


A Evolution API v2 está pronta para o Docker e pode ser facilmente implantada com Docker no modo standalone ou swarm. O repositório oficial do Evolution API contém todos os arquivos de composição necessários para instalar e executar a API.

Originalmente, a **Evolution API** começou como uma API de controle de WhatsApp baseada no CodeChat, utilizando a biblioteca Baileys. Com o tempo, a plataforma se expandiu para suportar não apenas o WhatsApp, mas também integrações com serviços como **Typebot, Chatwoot, Dify e OpenAI**. Além disso, a Evolution API suporta tanto a API de WhatsApp baseada no Baileys quanto a API oficial do WhatsApp Business, com suporte futuro planejado para Instagram e Messenger.

Processo de Instalação: 
- https://doc.evolution-api.com/v2/pt/install/docker


O banco de dados é uma parte fundamental da Evolution API v2, responsável por armazenar todas as informações críticas da aplicação. A API suporta tanto PostgreSQL quanto MySQL, utilizando o Prisma como ORM (Object-Relational Mapping) para facilitar a interação com esses bancos de dados.

A maneira mais fácil e rápida de configurar um banco de dados para a Evolution API v2 é através do Docker. Abaixo estão as instruções para configurar tanto o PostgreSQL quanto o MySQL usando Docker Compose.

##### Instalação do Postgres

Para configurar o PostgreSQL via Docker, siga os passos abaixo:

1. Baixe o arquivo `docker-compose.yaml` para o PostgreSQL disponível [aqui](https://github.com/EvolutionAPI/evolution-api/blob/v2.0.0/Docker/postgres/docker-compose.yaml).

```bash
version: '3.3'

services:
  postgres:
    container_name: postgres
    image: postgres:15
    networks:
      - evolution-net
    command: ["postgres", "-c", "max_connections=1000"]
    restart: always
    ports:
      - 5432:5432
    environment:
      - POSTGRES_PASSWORD=PASSWORD
    volumes:
      - postgres_data:/var/lib/postgresql/data
    expose:
      - 5432

  pgadmin:
    image: dpage/pgadmin4:latest
    networks:
      - evolution-net
    environment:
      - PGADMIN_DEFAULT_EMAIL=EMAIL
      - PGADMIN_DEFAULT_PASSWORD=PASSWORD  
    volumes:
      - pgadmin_data:/var/lib/pgadmin
    ports:
      - 4000:80
    links:
      - postgres

volumes:
  postgres_data:
  pgadmin_data:


networks:
  evolution-net:
    name: evolution-net
    driver: bridge
```


No meu caso, com base nas listas de redes disponíveis no docker - já com outras ferramentas instanciadas, como n8n, Dify e Langflow tive que **alterar a porta e também a subrede**.

```bash
version: '3.3'

services:
postgres:
    container_name: postgres
    image: postgres:15
    networks:
      - evolution-net
    command: ["postgres", "-c", "max_connections=1000"]
    restart: always
    ports:
      - 5433:5432  # Mapeia a porta 5433 no host para a porta 5432 no contêiner
    environment:
      - POSTGRES_PASSWORD=8H4a10032024
    volumes:
      - postgres_data:/var/lib/postgresql/data
    expose:
      - 5432  # Mantém a porta 5432 para exposição interna

  pgadmin:
    image: dpage/pgadmin4:latest
    networks:
      - evolution-net
    environment:
      - PGADMIN_DEFAULT_EMAIL=benevid@unemat.br
      - PGADMIN_DEFAULT_PASSWORD=8H4a10032024  
    volumes:
      - pgadmin_data:/var/lib/pgadmin
    ports:
      - 4000:80
    links:
      - postgres

volumes:
  postgres_data:
  pgadmin_data:


networks:
  evolution-net:
    name: evolution-net
    driver: bridge
    ipam:
      config:
        - subnet: 172.22.0.0/16
```

No meu caso tive que rodar o seguinte comando para criar o banco de dados:

```bash
docker-compose up -d
docker exec -it postgres psql -U postgres -c "CREATE DATABASE evolution;"
```

Variáveis de ambiente para habilitar no `.env`

```bash
# Habilitar o uso do banco de dados
DATABASE_ENABLED=true

# Escolher o provedor do banco de dados: postgresql ou mysql
DATABASE_PROVIDER=postgresql

# URI de conexão com o banco de dados
DATABASE_CONNECTION_URI='postgresql://user:pass@localhost:5432/evolution?schema=public'

# Nome do cliente para a conexão do banco de dados
DATABASE_CONNECTION_CLIENT_NAME=evolution_exchange

# Escolha os dados que você deseja salvar no banco de dados da aplicação
DATABASE_SAVE_DATA_INSTANCE=true
DATABASE_SAVE_DATA_NEW_MESSAGE=true
DATABASE_SAVE_MESSAGE_UPDATE=true
DATABASE_SAVE_DATA_CONTACTS=true
DATABASE_SAVE_DATA_CHATS=true
DATABASE_SAVE_DATA_LABELS=true
DATABASE_SAVE_DATA_HISTORIC=true

```


### Instalação do Redis
O Redis é utilizado pela Evolution API v2 como um sistema de cache para otimizar o desempenho e a velocidade da aplicação. Ele pode ser configurado para armazenar informações temporárias e melhorar a eficiência das operações.

Para configurar o Redis via Docker, siga os passos abaixo:

1. Baixe o arquivo `docker-compose.yaml` para o Redis disponível [aqui](https://github.com/EvolutionAPI/evolution-api/blob/v2.0.0/Docker/redis/docker-compose.yaml).
2. Navegue até o diretório onde o arquivo foi baixado e execute o comando:

```bash
docker-compose up -d
```

```bash
version: '3.3'

services:
  redis:
    image: redis:latest
    container_name: redis
    command: >
      redis-server --port 6379 --appendonly yes
    volumes:
      - evolution_redis:/data
    ports:
      - 6380:6379

volumes:
  evolution_redis:

networks:
  evolution-net:
    name: evolution-net
    driver: bridge
```


Variáveis de ambiente para habilitar no `.env`

```bash
# Habilitar o cache Redis
CACHE_REDIS_ENABLED=true

# URI de conexão com o Redis
CACHE_REDIS_URI=redis://localhost:6379/6

# Prefixo para diferenciar os dados de diferentes instalações que utilizam o mesmo Redis
CACHE_REDIS_PREFIX_KEY=evolution

# Habilitar para salvar as informações de conexão no Redis ao invés do banco de dados
CACHE_REDIS_SAVE_INSTANCES=false

# Habilitar o cache local
CACHE_LOCAL_ENABLED=false
```


**Instalação da Evolution**


```bash
version: '3.9'
services:
  evolution-api:
    container_name: evolution_api
    image: atendai/evolution-api:v2.1.1
    restart: always
    ports:
      - "8080:8080"
    env_file:
      - .env
    volumes:
      - evolution_instances:/evolution/instances

volumes:
  evolution_instances:

```

No meu tive que mudar a porta de saída porque dava choque com outra ferramenta. Ficando assim:

```bash
version: '3.9'
services:
  evolution-api:
    container_name: evolution_api
    image: atendai/evolution-api:v2.0.9-rc
    restart: always
    ports:
      - "8081:8080" # Mapeia 8081 (host) p/ 8080 (contêiner)
    env_file:
      - .env
    volumes:
      - evolution_instances:/evolution/instances

volumes:
  evolution_instances:
```

Em seguida, crie um arquivo `.env` no mesmo diretório com o seguinte conteúdo mínimo:

```bash
AUTHENTICATION_API_KEY=mude-me
```


Arquivo final do `.env`

```bash
## ------------------- BANCO DE DADOS -----------------------
# Habilitar o uso do banco de dados
DATABASE_ENABLED=true

# Escolher o provedor do banco de dados: postgresql ou mysql
DATABASE_PROVIDER=postgresql

# URI de conexão com o banco de dados
DATABASE_CONNECTION_URI='postgresql://postgres:8H4a10032024@5.78.105.1:5433/evolution?schema=public'
# Nome do cliente para a conexão do banco de dados
DATABASE_CONNECTION_CLIENT_NAME=evolution_exchange

# Escolha os dados que você deseja salvar no banco de dados da aplicação
DATABASE_SAVE_DATA_INSTANCE=true
DATABASE_SAVE_DATA_NEW_MESSAGE=true
DATABASE_SAVE_MESSAGE_UPDATE=true
DATABASE_SAVE_DATA_CONTACTS=true
DATABASE_SAVE_DATA_CHATS=true
DATABASE_SAVE_DATA_LABELS=true
DATABASE_SAVE_DATA_HISTORIC=true

## ----------------------- REDIS -------------------

# Habilitar o cache Redis
CACHE_REDIS_ENABLED=true

# URI de conexão com o Redis
CACHE_REDIS_URI=redis://5.78.105.1:6380/6

# Prefixo para diferenciar os dados de diferentes instalações que utilizam o mesmo Redis
CACHE_REDIS_PREFIX_KEY=evolution

# Habilitar para salvar as informações de conexão no Redis ao invés do banco de dados
CACHE_REDIS_SAVE_INSTANCES=false

# Habilitar o cache local
CACHE_LOCAL_ENABLED=false

AUTHENTICATION_API_KEY=bccb5913-0ba2-41e9-b67c-05dca0be1791
```


Iniciar o evolution

```bash
docker compose up -d
docker logs evolution_api
```



```json
{ "slots": { "2024-10-28": [ { "time": "2024-10-28T12:00:00.000Z" }, { "time": "2024-10-28T13:00:00.000Z" }, { "time": "2024-10-28T14:00:00.000Z" }, { "time": "2024-10-28T15:00:00.000Z" }, { "time": "2024-10-28T16:00:00.000Z" }, { "time": "2024-10-28T17:00:00.000Z" }, { "time": "2024-10-28T18:00:00.000Z" }, { "time": "2024-10-28T19:00:00.000Z" }, { "time": "2024-10-28T20:00:00.000Z" } ], "2024-10-29": [ { "time": "2024-10-29T17:00:00.000Z" }, { "time": "2024-10-29T18:00:00.000Z" }, { "time": "2024-10-29T19:00:00.000Z" }, { "time": "2024-10-29T20:00:00.000Z" } ], "2024-10-30": [ { "time": "2024-10-30T12:00:00.000Z" }, { "time": "2024-10-30T13:00:00.000Z" }, { "time": "2024-10-30T14:00:00.000Z" }, { "time": "2024-10-30T15:00:00.000Z" }, { "time": "2024-10-30T16:00:00.000Z" }, { "time": "2024-10-30T17:00:00.000Z" }, { "time": "2024-10-30T18:00:00.000Z" }, { "time": "2024-10-30T19:00:00.000Z" }, { "time": "2024-10-30T20:00:00.000Z" } ] } }
```

Joao Carlos, joaoc@gmail.com, (66) 99233-0909