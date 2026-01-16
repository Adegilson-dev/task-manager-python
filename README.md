# 📝 Gerenciador de Tarefas em Python (Terminal)

Projeto simples em Python para gerenciamento de tarefas via terminal, com persistência de dados em arquivo JSON.
Desenvolvido com foco em aprendizado, organização de código e boas práticas.

---

## 📌 Funcionalidades

* Adicionar tarefas
* Listar tarefas
* Marcar tarefas como concluídas
* Remover tarefas
* Salvamento automático em arquivo JSON
* Tratamento de erros de entrada do usuário

---

## 🛠 Tecnologias utilizadas

* Python 3
* JSON (persistência de dados)
* Execução via terminal

---

## 📂 Estrutura do projeto

```
task-manager-python/
│
├─ app.py          # Ponto de entrada e menu principal
├─ models.py       # Classe Tarefa
├─ services.py     # Regras de negócio
├─ storage.py      # Salvamento e carregamento em JSON
├─ tarefas.json    # Arquivo de dados (gerado automaticamente)
└─ README.md
```

---

## ⚙️ Como funciona

O programa roda no terminal e apresenta um menu interativo.
As tarefas são armazenadas no arquivo `tarefas.json`, garantindo que os dados não sejam perdidos ao fechar o programa.

Cada tarefa possui:

* ID único
* Nome
* Status (pendente ou concluída)

---

## ▶️ Como executar

1. Clone o repositório:

```bash
git clone https://github.com/Adegilson-dev/task-manager-python.git
```

2. Entre na pasta do projeto:

```bash
cd task-manager-python
```

3. Execute o programa:

```bash
python app.py
```

---

## 📖 Exemplo de uso

```
Menu
1- Adicionar tarefa
2- Exibir tarefas
3- Remover tarefa
4- Concluir tarefa
5- Sair
```

---

## 🧠 Boas práticas aplicadas

* Separação de responsabilidades em módulos
* Código limpo e organizado
* Validação de entradas do usuário
* Histórico de commits organizado
* `.gitignore` para arquivos desnecessários

---

## 🔮 Próximos passos

* Versão web utilizando Flask
* Interface gráfica
* Filtros de tarefas (pendentes / concluídas)
* Edição de tarefas
* Testes automatizados

---

## 📌 Observações

* Projeto desenvolvido para fins de aprendizado
* Interface via terminal
* Serve como base para evolução futura (versão web)

---

## 👨‍💻 Autor

Desenvolvido por **Adegilson Silva**
