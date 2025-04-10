# 📝 Gerenciador de Tarefas (Task Manager)

Este é um projeto simples em Python que permite gerenciar tarefas diretamente pelo terminal.  
Você pode adicionar tarefas, marcar como concluídas e visualizar o que está pendente ou já foi feito.

---

## 🚀 Funcionalidades

- ✅ Adicionar novas tarefas
- 🕒 Marcar tarefas como concluídas
- 📋 Listar tarefas pendentes
- ✔️ Listar tarefas concluídas
- 💾 Armazenamento das tarefas em um arquivo `.txt`

---

## 🛠 Tecnologias utilizadas

- Python 3

---

## 📂 Estrutura de dados

As tarefas são armazenadas no arquivo `gerenciador.txt` no seguinte formato:

nome_da_tarefa: status


Onde `status` pode ser:
- `pending` → tarefa ainda não concluída
- `completed` → tarefa já finalizada

### 🧾 Exemplo:

Estudar Python: pending Lavar roupa: completed


O programa lê esse arquivo toda vez que é executado, garantindo que suas tarefas permaneçam salvas entre os usos.

---

## 💻 Como usar

1. Clone este repositório ou copie o arquivo Python para sua máquina.
2. Execute o programa com:
   ```bash
   python nome_do_arquivo.py
3. Use o menu interativo para gerenciar suas tarefas! 

## ✨ Exemplo de uso

Welcome to your task manager
1. Add new task:
2. Which task did you complete?
3. List pending tasks
4. List completed tasks
5. Exit

## 📌 Aprendizados

Este projeto me ajudou a praticar:  

Leitura e escrita em arquivos (.txt)  

Uso de listas, strings e dicionários  

Laços de repetição e condicionais  

Organização de código e validação de entrada do usuário  

