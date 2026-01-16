# Gerenciador de Tarefas em Python (Terminal)

Projeto simples em Python para gerenciamento de tarefas via terminal, com persistência de dados em arquivo JSON.

## Funcionalidades
- Adicionar tarefas
- Listar tarefas
- Marcar tarefas como concluídas
- Remover tarefas
- Salvar e carregar tarefas automaticamente

## Tecnologias utilizadas
- Python 3
- JSON (para persistência de dados)

## Como funciona
O programa roda no terminal e apresenta um menu interativo.  
As tarefas são armazenadas em um arquivo `tarefas.json`, garantindo que os dados não sejam perdidos ao fechar o programa.

Cada tarefa possui:
- ID único
- Nome
- Status (pendente ou concluída)

## Como executar
1. Clone este repositório:
   ```git clone https://github.com/Adegilson-dev/task-manager-python.git```
2. Acesse a pasta do projeto:
  cd task-manager-python
Execute o programa:
  python app.py

## Observações
- Projeto desenvolvido para fins de aprendizado.
- Interface via terminal.
- Código simples e organizado, focado em lógica e persistência de dados.

## Próximos passos (planejados)
- Versão web utilizando Flask
- Interface gráfica
- Melhor tratamento de erros
