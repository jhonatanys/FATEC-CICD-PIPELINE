# Pipeline CI/CD com CodeQL

**Trabalho Final** - FATEC Santana de Parnaíba  
**Disciplina:** Desenvolvimento de Sistemas - Segurança da Informação  
**Professor:** Idirley Soares  
**Aluno:** Jhonatan Santos Gomes


---

## Sobre o Projeto

Este repositório contém uma pipeline CI/CD completa com análise de segurança 
usando CodeQL, desenvolvida como trabalho final da disciplina.

### Estrutura da Pipeline (3 Jobs)

1. **Análise CodeQL** - Verifica vulnerabilidades de segurança no código
2. **Testes Automatizados** - Executa testes unitários com pytest e verificação com flake8
3. **Deploy para Stage** - Simula o envio para ambiente de homologação

---

## Evidências de Funcionamento

### Teste 1 - Pipeline com código seguro (todos os Jobs verdes)
<img width="1891" height="1020" alt="Captura de tela 2026-05-22 224125" src="https://github.com/user-attachments/assets/aa4816d5-bf4a-4498-a459-8edc67b51fe7" />


---

### Teste 2 - CodeQL detectou vulnerabilidade SQL Injection

**Pipeline após inserir código vulnerável:**

<img width="1919" height="1079" alt="Captura de tela 2026-05-22 230036" src="https://github.com/user-attachments/assets/04ee9349-325d-4de4-a7ad-af02a4c73a92" />


**Alerta de segurança detectado (severidade High):**

<img width="1885" height="953" alt="Captura de tela 2026-05-22 230319" src="https://github.com/user-attachments/assets/f88a91e4-930a-4ad6-b2a5-a56fb2b5e597" />


---

### Teste 3 - Pipeline após correção da vulnerabilidade

**Pipeline com todos os Jobs verdes novamente:**

<img width="1913" height="957" alt="Captura de tela 2026-05-22 230354" src="https://github.com/user-attachments/assets/7fc5aef3-32b8-43c9-9e68-a7a4660549b5" />


**Alerta resolvido automaticamente:**

<img width="1913" height="957" alt="Captura de tela 2026-05-22 230354" src="https://github.com/user-attachments/assets/b7fbd757-db6a-4af7-be3e-b2e45bdbc03f" />


---

## Tecnologias Utilizadas

1 - Python 3.11
2 - GitHub Actions (CI/CD)
3 - CodeQL (Análise de segurança)
4 - Pytest (Testes automatizados)
5 - Flake8 (Qualidade de código)
6 - Flask (Framework web)
