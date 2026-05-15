# PIM-II - Sistema de Triagem de Edital

Projeto desenvolvido para a Faculdade UNIP (Universidade Paulista).

## Alunos

- Kaique Souza Pereira — RA: 2625068
- Edgar Parreira França — RA: 2625239
- Ana Luiza Morais Barbieri — RA: 2622005
- Melissa Maria Galvão de Oliveira — RA: 2625411
- Theo Amaral da Silva — RA: 2626098

## Sobre o projeto

Este projeto implementa um sistema automatizado de triagem de editais. A aplicação processa documentos em PDF e gera relatórios estruturados em TXT, extraindo e organizando as informações relevantes de forma padronizada.

O objetivo é apoiar a análise de documentos relacionados às submissões de editais da Pró-Reitoria de Extensão e Cultura, reduzindo o trabalho manual e tornando a leitura dos dados mais clara.

## Como funciona

O sistema segue este fluxo:

1. **Entrada**: recebe um arquivo PDF com a documentação da submissão ao edital.
2. **Processamento**: analisa o conteúdo do documento com base em uma estrutura JSON montada a partir de editais anteriores da PREX e de suas normativas.
3. **Saída**: gera um relatório estruturado em formato TXT com os resultados da análise.

## Como usar

### Pré-requisitos

- Python 3.7 ou superior
- Dependências do projeto instaladas
- Arquivo PDF salvo na pasta de entrada do projeto

### Executando o sistema

Para processar um PDF e gerar o relatório, execute o comando abaixo na raiz do projeto:

```bash
export PYTHONPATH=$(pwd) && python3 prex_triagem/main.py > resultado.txt
```

### Explicação do comando

- `export PYTHONPATH=$(pwd)`: adiciona o diretório atual ao caminho de importação do Python, permitindo que os módulos do projeto sejam encontrados.
- `python3 prex_triagem/main.py`: executa o script principal do sistema.
- `> resultado.txt`: redireciona a saída da execução para um arquivo TXT chamado `resultado.txt`.

### Resultado esperado

Após a execução, será criado o arquivo `resultado.txt` contendo o relatório com as informações extraídas do PDF processado.

## Estrutura do projeto

```text
PIM-II/
├── prex_triagem/
│   ├── main.py          # Ponto de entrada da aplicação
│   └── ...              # Demais módulos de processamento
├── README.md            # Documentação do projeto
└── resultado.txt        # Arquivo de saída gerado
```

## Exemplos de uso

### Copiar um PDF para a pasta de entrada

```bash
# Copia um arquivo PDF da pasta Downloads para a pasta de entrada do projeto
cp ~/Downloads/nome_do_arquivo.pdf ./prex_triagem/data/pdfs_entrada/
```

### Processar a triagem e salvar o resultado

```bash
export PYTHONPATH=$(pwd) && python3 prex_triagem/main.py > resultado.txt
```

### Executar e visualizar a saída no terminal

```bash
export PYTHONPATH=$(pwd) && python3 prex_triagem/main.py
```

Esse comando executa o processo de triagem e exibe o resultado diretamente no terminal. Para salvar a saída em arquivo, utilize o redirecionamento para `resultado.txt`.

## Observações

- Verifique se o PDF de entrada está no local correto antes de executar o sistema.
- Caso existam dependências adicionais, instale-as antes da execução.
- O arquivo de saída pode ser utilizado para consulta e conferência dos resultados da triagem.
