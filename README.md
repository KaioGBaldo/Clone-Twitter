# 🐦 Twitter Clone (Django + Tailwind CSS)

Este projeto é uma aplicação web completa que replica a arquitetura e as principais mecânicas do **Twitter (X)**. Desenvolvido em Python com o ecossistema **Django**, o projeto utiliza renderização no servidor (SSR), estilização moderna com **Tailwind CSS**, requisições assíncronas (AJAX) para interações fluidas e uma camada otimizada de consultas ao banco de dados relacional.

---

## 🚀 Principais Funcionalidades

### 1. Linha do Tempo Dinâmica & Otimização SQL

* **Feed Personalizado:** A página inicial (`home`) renderiza cronologicamente as postagens do próprio usuário e dos perfis que ele segue.

* **Performance Garantida ($N+1$ Prevenido):** A lógica de busca no banco faz o uso de `.select_related()` (para chaves estrangeiras como autores) e `.prefetch_related()` (para relações de muitos-para-muitos como curtidas e comentários). Isso reduz dezenas de consultas redundantes no banco de dados para apenas poucas operações combinadas.


### 2. Postagens Avançadas com Suporte de Mídia

* **Validação Inteligente:** O modelo de `Post` valida e aceita textos de até 280 caracteres. Arquitetonicamente, ele permite publicações sem texto, desde que o usuário anexe uma imagem (`ImageField`) ou um vídeo (`FileField`).


* **Isolamento de Uploads:** Arquivos de mídia enviados são tratados e guardados automaticamente em diretórios organizados (`post_images/`, `post_videos/`).



### 3. Interações Dinâmicas (Toggle Engine via AJAX)

* **Sistema de Likes:** Endpoint inteligente que intercepta requisições. Se o usuário já curtiu, remove o vínculo; caso contrário, adiciona e cria uma notificação para o autor. Com o suporte a AJAX, o JavaScript atualiza os contadores na tela instantaneamente sem dar *refresh* na página inteira.


* **Retweets Autênticos:** Mecânica que identifica se o post selecionado já é um retweet. Se for, o sistema extrai a referência do *post original verdadeiro* para evitar retweets em cadeia infinita.



### 4. Grafo de Relacionamentos & Notificações

* **Seguidores Assimétricos:** Implementação de `ManyToManyField` auto-referenciada com `symmetrical=False`. Garante que seguir um perfil não force o outro a te seguir de volta automaticamente.


* **Notificações Unificadas:** Sistema categorizado por tipos: Curtidas (`L`), Comentários (`C`), Seguidores (`F`) e Retweets (`R`). A leitura de alertas executa uma atualização em massa (`.update(is_read=True)`) direto a nível de banco de dados.



---

## 📂 Visão Geral da Arquitetura

```text
├── core/                           # Configurações globais do ecossistema Django
│   ├── settings.py                 # Middlewares, uploads, localização e WhiteNoise
│   ├── urls.py                     # Roteador central e mapeador global
│   └── wsgi.py / asgi.py           # Interfaces síncronas/assíncronas de servidor
├── twitter/                        # Núcleo da aplicação da Rede Social
│   ├── models.py                   # Esquema relacional (User, Post, Comment, Notification)
│   ├── views.py                    # Lógica de negócio, retornos JSON e consultas SQL
│   ├── forms.py                    # Formulários customizados injetados com Tailwind
│   └── urls.py                     # Endpoints e capturadores dinâmicos de IDs
├── templates/                      # Camada de apresentação em HTML5 estruturado
└── manage.py                       # Utilitário de gerenciamento do framework Django

```

---

## 🔧 Como Executar o Projeto Localmente

### 1. Clonar o Repositório e Isolar o Ambiente

```bash
git clone https://github.com/seu-usuario/nome-do-seu-repositorio.git
cd nome-do-seu-repositorio

# Criar e ativar o ambiente virtual (Virtualenv)
python -m venv venv
# No Windows:
.\venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate

```

### 2. Instalar Dependências e Preparar o Banco

```bash
# Instala os pacotes necessários (Django, Pillow para imagens e WhiteNoise)
pip install django whitenoise pillow

# Executar as migrações estruturais para criar as tabelas
python manage.py makemigrations
python manage.py migrate

```

### 3. Criar Administrador e Iniciar o Sistema

```bash
# Gerar credenciais para o painel de moderação (Django Admin)
python manage.py createsuperuser

# Iniciar o servidor local de desenvolvimento
python manage.py runserver

```

Acesse no seu navegador: [http://127.0.0.1:8000/](https://www.google.com/search?q=http://127.0.0.1:8000/)

---

## ☁️ Configurações de Produção (Deploy Pronto)

O repositório já conta com ajustes cruciais necessários para hospedagem direta na nuvem (como a plataforma **Render**):

1. **Gerenciador WhiteNoise:** O `WhiteNoiseMiddleware` está acoplado no pipeline global para servir, compactar e armazenar em cache os arquivos estáticos de design (Tailwind) sem depender de servidores HTTP adicionais[cite: 10].
2. **Ambiente Seguro:** O arquivo `settings.py` possui a variável `STATIC_ROOT` mapeada e suporte para uploads via caminhos de mídia dinâmicos[cite: 10].

---

## 📝 Licença

Este projeto foi desenvolvido com caráter puramente didático, educacional e demonstrativo para fins de estudo e composição de portfólio .
