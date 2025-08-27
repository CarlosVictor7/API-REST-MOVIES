# API REST MOVIES

Uma API completa em **Django REST Framework** para gerenciar filmes com funcionalidades de CRUD, busca, ordenação e paginação.

## 🚀 Funcionalidades

- ✅ **CRUD completo** para filmes
- ✅ **Busca** por título e gênero
- ✅ **Ordenação** por múltiplos campos
- ✅ **Paginação** automática (10 itens por página)
- ✅ **Validação** de dados (rating entre 0-10)
- ✅ **Interface web navegável** do Django REST Framework
- ✅ **Timestamps** automáticos (created_at, updated_at)

## 🛠️ Tecnologias

- Python 3.13+
- Django 5.2+
- Django REST Framework 3.16+
- SQLite (banco de dados padrão)

## 📦 Instalação

1. **Clone o repositório**
```bash
git clone <url-do-repositorio>
cd API-REST-MOVIES
```

2. **Crie e ative o ambiente virtual**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute as migrações**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Inicie o servidor**
```bash
python manage.py runserver
```

6. **Acesse a API**
- Interface web: http://127.0.0.1:8000/movies/
- API root: http://127.0.0.1:8000/

## 📚 Modelo de Dados

### Movie
```python
{
    "id": 1,
    "title": "Inception",
    "genre": "Sci-Fi",
    "release_year": 2010,
    "rating": 8.8,
    "created_at": "2025-08-26T23:54:25.123456Z",
    "updated_at": "2025-08-26T23:54:25.123456Z"
}
```

**Campos:**
- `title`: Título do filme (máx. 100 caracteres)
- `genre`: Gênero do filme (máx. 50 caracteres)
- `release_year`: Ano de lançamento (inteiro)
- `rating`: Avaliação (0.0 a 10.0)
- `created_at`: Data de criação (automático)
- `updated_at`: Data de atualização (automático)

## 🔗 Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/movies/` | Lista todos os filmes |
| POST | `/movies/` | Cria um novo filme |
| GET | `/movies/{id}/` | Obtém detalhes de um filme |
| PUT | `/movies/{id}/` | Atualiza um filme completo |
| PATCH | `/movies/{id}/` | Atualiza um filme parcialmente |
| DELETE | `/movies/{id}/` | Exclui um filme |

## 🔍 Parâmetros de Query

### Busca
```bash
GET /movies/?search=inception
GET /movies/?search=sci-fi
```

### Ordenação
```bash
GET /movies/?ordering=rating          # Crescente
GET /movies/?ordering=-rating         # Decrescente
GET /movies/?ordering=release_year    # Por ano
GET /movies/?ordering=-created_at     # Mais recentes primeiro
```

### Paginação
```bash
GET /movies/?page=1
GET /movies/?page=2
```

### Combinação
```bash
GET /movies/?search=crime&ordering=-rating&page=1
```

## 📝 Exemplos de Uso

### Criar um filme
```bash
curl -X POST http://127.0.0.1:8000/movies/ \
  -H "Content-Type: application/json" \
  -d '{"title":"Inception","genre":"Sci-Fi","release_year":2010,"rating":8.8}'
```

### Listar filmes
```bash
curl http://127.0.0.1:8000/movies/
```

### Buscar filmes por gênero
```bash
curl "http://127.0.0.1:8000/movies/?search=Crime"
```

### Atualizar rating
```bash
curl -X PATCH http://127.0.0.1:8000/movies/1/ \
  -H "Content-Type: application/json" \
  -d '{"rating":9.5}'
```

### Excluir filme
```bash
curl -X DELETE http://127.0.0.1:8000/movies/1/
```

## 🧪 Testes

Para mais exemplos de teste, consulte o arquivo `API_TESTS.md`.

## 📁 Estrutura do Projeto

```
API-REST-MOVIES/
├── api/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py          # Modelo Movie
│   ├── serializers.py     # Serializer para API
│   ├── tests.py
│   └── views.py           # ViewSet com CRUD
├── myproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py        # Configurações DRF
│   ├── urls.py            # URLs da API
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── API_TESTS.md
└── README.md
```

## ⚙️ Configurações

As principais configurações do Django REST Framework estão em `myproject/settings.py`:

```python
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_FILTER_BACKENDS": [
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ],
}
```

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.