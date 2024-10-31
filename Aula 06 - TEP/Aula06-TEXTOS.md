# Aula 06 - Chatbots com base de conhecimento - Dify

## Instalação do Dify

Clonando o respositório

```bash
git clone https://github.com/langgenius/dify.git
cd dify/docker
```

Criando um cópia do ENV file e alterando a porta do NGINX

```bash
cp .env.example .env
# Password for admin user initialization.
# If left unset, admin user will not be prompted for a password
# when creating the initial admin account.
INIT_PASSWORD=sk-9f73s3ljTX
EXPOSE_NGINX_PORT=8080
```

Executando o Docker compose

```bash
docker compose up -d
```

Se precisar atualizar 

```bash
cd dify/docker
docker compose down
git pull origin main
docker compose pull

```

## Introdução ao Dify

## Instalação do N8n

Criar uma pasta n8n

```bash
mkdir n8n
cd n8n/
```

Criar um arquivo docker-compose.yaml

```bash
version: "3.2"
services:
  n8n:
    image: n8nio/n8n
    ports:
      - "5678:5678"
    environment:
      - N8N_BASIC_AUTH_USER=admin
      - N8N_BASIC_AUTH_PASSWORD=8H4a10032024
    volumes:
      - n8n_data:/home/node/.n8n
    networks:
      - n8n-net

volumes:
  n8n_data:

networks:
  n8n-net:
    name: n8n-net
    driver: bridge
```

Subir o container

```bash
docker compose up -d
```

## Criação de uma ferramenta
