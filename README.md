# Kixikila 💰

O **Kixikila** é um projeto inspirado na prática cultural angolana de contribuições coletivas.  
Ele ainda está em fase inicial, mas já implementa funcionalidades básicas de um sistema financeiro.

---

## 📌 Funcionalidades atuais
- Debitar uma conta
- Creditar uma conta
- Transferir entre contas
- Consultar saldo

---

## 🚀 Como funciona
Por enquanto, o sistema roda apenas no **terminal**.  
Não há interface gráfica implementada ainda.

---

## 🎯 Objetivo
O objetivo é evoluir esse projeto para aplicações **web ou desktop**, adicionando interface amigável, banco de dados e autenticação.

---

## ⚡ Tecnologias utilizadas
- Python 3.x

---

## 📥 Como baixar
1. Clique no botão verde **Code** aqui no GitHub.  
2. Escolha a opção **Download ZIP**.  
3. Extraia o arquivo no seu computador.

Ou, se preferir, clone o repositório direto:
```bash
git clone https://github.com/JoshuaDaCosta/kixikila.git

```
```bash
python main.py
```
## ▶️ Como usar
1. Abra o terminal na pasta raiz do projeto (onde está o `conta.py`).  
2. Execute:
```bash
python conta.py
```
⚠️ Obs.:
- O arquivo conta.py está dentro da pasta classes, deve importar assim:
```bash
from classes.CONTA import Conta
```
- A estrutura de pastas deve ser assim:
```kixikila/
│── main.py
│── classes/
│     └── conta.py
```

- O menu será exibido no terminal e você poderá escolher:

1 para debitar

2 para creditar

3 para transferir

4 para consultar saldo
