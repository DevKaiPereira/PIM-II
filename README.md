# PIM-II - Sistema Triagem PREX

Projeto desenvolvido para a Faculdade UNIP (Universidade Paulista).

## Alunos

- Kaique Souza Pereira — RA: 2625068
- Edgar Parreira França — RA: 2625239
- Ana Luiza Morais Barbieri — RA: 2622005
- Theo Amaral da Silva — RA: 2626098

## Sobre o projeto

Este projeto implementa o sistema automatizado **Triagem PREX**. A aplicação processa documentos em PDF e gera relatórios estruturados, extraindo e organizando as informações relevantes de forma padronizada.

O objetivo é atuar como uma ferramenta de apoio à análise técnica de documentos relacionados às submissões de editais da Pró-Reitoria de Extensão e Cultura (PREX/IFB), reduzindo o trabalho manual e auxiliando a comissão avaliadora na tomada de decisão.

## Como funciona

O sistema segue este fluxo:

1. **Entrada**: recebe um arquivo PDF com a documentação da submissão ao edital.
2. **Processamento**: analisa o conteúdo do documento com base em uma biblioteca de termos (JSON) fundamentada nos editais da PREX e normativas vigentes.
3. **Saída**: gera relatórios estruturados individuais em formato TXT, além de exportar os resultados da análise técnica consolidados em PDF e CSV.

## Como usar

### Pré-requisitos

- Python 3.7 ou superior
- Dependências do projeto instaladas
- Arquivo PDF salvo na pasta de entrada do projeto

### Executando o sistema

Para processar um PDF e gerar o relatório, execute o comando abaixo na raiz do projeto:

```bash
python3 -m prex_triagem > resultado.txt
```

Ou, se preferir um comando fixo (macOS/Linux), use o `Makefile` do projeto:

```bash
make run-txt
```

### Explicação do comando

- `python3 -m prex_triagem`: executa o pacote usando o ponto de entrada em `prex_triagem/__main__.py`.
- `> resultado.txt`: redireciona a saída da execução para um arquivo TXT chamado `resultado.txt`.

### Resultado esperado

Após a execução, será criado o arquivo `resultado.txt` contendo o relatório com as informações extraídas do PDF processado.

O relatório consolidado em PDF e o CSV sumarizado serão salvos juntos na pasta `relatorios/`.

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
python3 -m prex_triagem > resultado.txt
```

### Executar e visualizar a saída no terminal

```bash
python3 -m prex_triagem
```

### Comandos prontos (opcional)

Se você estiver no macOS/Linux, também pode usar:

```bash
make run     
make run-txt 
```

Esse comando executa o processo de triagem e exibe o resultado diretamente no terminal. Para salvar a saída em arquivo, utilize o redirecionamento para `resultado.txt`.

## Observações

- Verifique se o PDF de entrada está no local correto antes de executar o sistema.
- Caso existam dependências adicionais, instale-as antes da execução.
- O arquivo de saída pode ser utilizado para consulta e conferência dos resultados da triagem.
