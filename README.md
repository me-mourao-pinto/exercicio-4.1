Exercício 4.1 — API REST de uma aplicação de TODO list (POST/GET/PUT)
Aluno: Inácio Emiliano Melo Mourão Pinto Disciplina: IDP-TD 2026 Framework usado: FastAPI + Uvicorn

O que esta API faz
API REST que serve de backend de uma aplicação de TODO list — gerencia tarefas ({id, titulo, concluida}), com armazenamento em memória, rodando em http://localhost:8000. Implementa POST (criar), GET (ler) e PUT (atualizar), seguindo o contrato do tutorial_4.1.md.

Estrutura
app/main.py — implementação da API
requirements.txt — dependências (fastapi, uvicorn)
.autograde-exercise — marcador do autograder (conteúdo: 4.1)
Como rodar
pip install -r requirements.txt
uvicorn app.main:app --port 8000
Como validar
Com a API rodando (recém-reiniciada, store vazio), em outro terminal dentro do repo:

autograde validar 4.1
Endpoints
Método	Rota	Descrição
GET	/health	liveness — {"status":"ok"}
POST	/tarefas	cria tarefa a partir de {"titulo": "..."}
GET	/tarefas/{id}	lê uma tarefa (404 se não existe)
GET	/tarefas	lista todas
PUT	/tarefas/{id}	atualiza titulo e concluida
Decisões de implementação
Explique brevemente: Usei este framework porque foi o que o professor trouxe em seu exemplo. Modelei tudo com auxílido de ChatGPT e opencode. O erro 404 está tratado trazendo uma mensagem de erro motivacional. 
