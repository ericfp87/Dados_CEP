# Dados_CEP
 Obtenção de dados de CEP via API


# 📦 Enriquecimento de Dados de CEP com API

Bem-vindo ao repositório **Enriquecimento de Dados de CEP com API**! Este projeto em Python automatiza a coleta de informações detalhadas sobre CEPs, utilizando a API do `AwesomeAPI`, e organiza os resultados em um arquivo CSV pronto para análise ou integração em outros sistemas.

## 🚀 Funcionalidades

- **Consulta Automática de CEPs**: Faz requisições a uma API externa para obter dados completos de CEPs.
- **Criação de DataFrame**: Organiza os dados recebidos em um DataFrame do Pandas para fácil manipulação e análise.
- **Exportação de Resultados**: Salva os dados enriquecidos em um arquivo CSV delimitado por ponto e vírgula (`;`).

## 🛠️ Requisitos

Antes de começar, certifique-se de ter os seguintes requisitos:

- **Python 3.x**
- **Bibliotecas Python**: `pandas`, `requests`

## 🚀 Como Usar

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/ericfp87/Dados_CEP.git
    ```

2. **Instale as dependências**:
    ```bash
    pip install pandas requests
    ```

3. **Prepare seu arquivo CSV de entrada**:
   - O arquivo CSV deve conter uma coluna chamada `CEP` com os CEPs a serem consultados.

4. **Execute o script**:
    - Certifique-se de que o caminho do arquivo CSV de entrada (`CEP.csv`) esteja correto no script.
    - Execute o script:
    ```bash
    python enriquecimento_cep.py
    ```

5. **Verifique os arquivos de saída**:
   - O arquivo de saída será salvo no caminho especificado, contendo os dados de CEPs enriquecidos, prontos para uso.

## 📂 Estrutura do Projeto

```plaintext
├── enriquecimento_cep.py                # Script principal
├── data/                                # Pasta para armazenar os arquivos CSV de entrada
│   └── CEP.csv                          # Arquivo CSV contendo os CEPs a serem consultados
└── OUTPUT/                              # Pasta para armazenar o arquivo de saída
    └── LOGRADOUROS_MG.csv               # Arquivo de saída com os dados enriquecidos
```

## 🔍 Dicas e Sugestões

- **Limitação de Requisições**: A API utilizada possui um limite de requisições por segundo. O script inclui um `time.sleep(2)` para evitar sobrecarga e respeitar as limitações da API.
- **Formatos de Saída**: O script pode ser adaptado para salvar os resultados em outros formatos, como JSON ou Excel, com pequenas modificações no código.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um *pull request* ou relatar problemas na aba de *Issues*.

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.