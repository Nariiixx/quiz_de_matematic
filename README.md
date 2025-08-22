# Quiz de Matemática

Um quiz interativo em Python para treinar operações matemáticas, como soma, subtração, multiplicação, divisão, potências e radiciação. O projeto também salva os resultados dos jogadores em um banco de dados MySQL e exibe rankings.

---

## Funcionalidades

- **Seis estágios de matemática:**
  1. Soma
  2. Subtração
  3. Multiplicação
  4. Divisão
  5. Potências
  6. Radiciação (raízes quadradas)
- **Pontuação automática**: cada resposta correta vale 2,777... pontos.
- **Tempo de execução** registrado para cada estágio.
- **Ranking**: os resultados são salvos no MySQL e podem ser exibidos em ordem decrescente de pontuação.
- **Menu interativo** para iniciar o quiz, ver pontuação ou sair.

---

## Pré-requisitos

- Python 3.10 ou superior
- MySQL instalado e rodando
- Biblioteca `mysql-connector-python`
- Biblioteca `tabulate`
- Biblioteca `python-dotenv` (para variáveis de ambiente, como credenciais do banco)

---

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/Nariiixx/quiz_de_matematic.git
cd quiz_de_matematic
