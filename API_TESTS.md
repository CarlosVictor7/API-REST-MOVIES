# API REST MOVIES - Comandos de Teste

## Endpoints disponíveis:
- GET /movies/ → listar filmes
- POST /movies/ → criar filme
- GET /movies/{id}/ → detalhe do filme
- PUT /movies/{id}/ → atualizar filme completo
- PATCH /movies/{id}/ → atualizar filme parcialmente
- DELETE /movies/{id}/ → excluir filme

## Exemplos de uso com cURL:

### 1. Criar um novo filme
```bash
curl -X POST http://127.0.0.1:8000/movies/ \
  -H "Content-Type: application/json" \
  -d '{"title":"Inception","genre":"Sci-Fi","release_year":2010,"rating":8.8}'
```

### 2. Criar mais filmes para teste
```bash
curl -X POST http://127.0.0.1:8000/movies/ \
  -H "Content-Type: application/json" \
  -d '{"title":"The Matrix","genre":"Sci-Fi","release_year":1999,"rating":8.7}'

curl -X POST http://127.0.0.1:8000/movies/ \
  -H "Content-Type: application/json" \
  -d '{"title":"Pulp Fiction","genre":"Crime","release_year":1994,"rating":8.9}'

curl -X POST http://127.0.0.1:8000/movies/ \
  -H "Content-Type: application/json" \
  -d '{"title":"The Godfather","genre":"Crime","release_year":1972,"rating":9.2}'
```

### 3. Listar todos os filmes
```bash
curl http://127.0.0.1:8000/movies/
```

### 4. Buscar filmes por título ou gênero
```bash
# Buscar por "Matrix"
curl "http://127.0.0.1:8000/movies/?search=Matrix"

# Buscar por gênero "Crime"
curl "http://127.0.0.1:8000/movies/?search=Crime"
```

### 5. Ordenar filmes
```bash
# Ordenar por rating (crescente)
curl "http://127.0.0.1:8000/movies/?ordering=rating"

# Ordenar por rating (decrescente)
curl "http://127.0.0.1:8000/movies/?ordering=-rating"

# Ordenar por ano de lançamento
curl "http://127.0.0.1:8000/movies/?ordering=release_year"
```

### 6. Obter detalhes de um filme específico
```bash
curl http://127.0.0.1:8000/movies/1/
```

### 7. Atualizar rating de um filme (PATCH)
```bash
curl -X PATCH http://127.0.0.1:8000/movies/1/ \
  -H "Content-Type: application/json" \
  -d '{"rating":9.3}'
```

### 8. Atualizar filme completo (PUT)
```bash
curl -X PUT http://127.0.0.1:8000/movies/1/ \
  -H "Content-Type: application/json" \
  -d '{"title":"Inception","genre":"Sci-Fi","release_year":2010,"rating":9.0}'
```

### 9. Excluir um filme
```bash
curl -X DELETE http://127.0.0.1:8000/movies/1/
```

## Funcionalidades implementadas:

✅ **Modelo Movie** com validação de rating (0-10)
✅ **CRUD completo** (Create, Read, Update, Delete)
✅ **Paginação** (10 itens por página)
✅ **Busca** por título e gênero
✅ **Ordenação** por vários campos
✅ **Django REST Framework** com interface web navegável
✅ **Validação de dados** automática
✅ **Timestamps** automáticos (created_at, updated_at)

## Para testar via interface web:
Acesse http://127.0.0.1:8000/movies/ no navegador para usar a interface gráfica do Django REST Framework.
