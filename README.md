#Odin Project

Projeto de estudo colaborativo dos amigos do trabalho.
Aprendizado de lógica de programação utilizando Python.

#Inicialição do Projeto
git clone git@github.com:washingtonnuness/odin.git

cd odin

criar nova branch 
git checkout -b 'nova_branch'

Codar

#adicionar todos os arquivos alterados
git add .

#commitar as alterações
git commit -m 'Meu commit'

#enviar as alteração para repositorio remoto(origin) da branch nova_branch

git push origin nova_branch


#############################################
#			Configurando o Ambiente			#
#############################################

Instalação do pyenv

Executar no powershell(admin) os comandos:

Set-ExecutionPolicy RemoteSigned

#Documentação do pyenv
$https://pyenv-win.github.io/pyenv-win/

Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"

Fechar o terminal e executar novamente.

$ Execução no terminal
pyenv install --list #Lista ultima versão do python disponível.
pyenv install 3.12:latest ou pyenv install 3.12.4

#Seta como padrão a versão instalada acima.
pyenv global 3.12.4

python --version

gerenciador de pacotes python

pip install pipx

#Não lembro o que faz

pipx install poetry

#Adicionar as poetry as variáves de ambiente do Windows
pipx ensurepath

#ferramenta para criação de git ignor (opcional)
pipx install ignr


Criação do Projeto FastAPI e Instalação das Dependências
Agora que temos o Python e o Poetry prontos, podemos começar a criar nosso projeto FastAPI.

Inicialmente criaremos um novo projeto python usando o Poetry, com o comando poetry new e em seguida navegaremos até o diretório criado:

$ Execução no terminal!
poetry new fast_odin
cd fast_odin

#Define uma versão padrão que pode ser diferente ou não da global para o projeto local.
$ Execução no terminal!
pyenv local 3.12.4

Cria o ambiente virtual (venv)
$ Execução no terminal!
poetry install
poetry add fastapi


Ele criará uma estrutura de arquivos e pastas como essa:
.
├── fast_odin
│  └── __init__.py
├── pyproject.toml
├── README.md
└── tests
   └── __init__.py
   
Para que a versão do python que instalamos via pyenv seja usada em nosso projeto criado com poetry, devemos dizer ao pyenv qual versão do python será usada nesse diretório:

$ Execução no terminal!
pyenv local 3.12.4

Em conjunto com essa instrução, devemos dizer ao poetry que usaremos exatamente a versão 3.12 em nosso projeto. 
Para isso alteraremos o arquivo de configuração do projeto o pyproject.toml na raiz do projeto:

pyproject.toml
[tool.poetry.dependencies]
python = "3.12.*"

Em seguida, inicializaremos nosso ambiente virtual com Poetry e instalaremos o FastAPI:
$ Execução no terminal!
poetry install 

Adiciona o FastAPI no nosso ambiente virtual
poetry add fastapi

Instalando as ferramentas de desenvolvimento
As escolhas de ferramentas de desenvolvimento, de forma geral, são escolhas bem particulares. Não costumam ser consensuais nem mesmo em times de desenvolvimento. Dito isso, selecionei algumas ferramentas que gosto de usar e alinhadas com a utilidade que elas apresentam no desenvolvimento do projeto.

As ferramentas escolhidas são:

taskipy: ferramenta usada para criação de comandos. Como executar a aplicação, rodar os testes, etc.
pytest: ferramenta para escrever e executar testes
ruff: Uma ferramenta que tem duas funções no nosso código:
Um analisador estático de código (um linter), para dizer se não estamos infringido alguma boa prática de programação;
Um formatador de código. Para seguirmos um estilo único de código. Vamos nos basear na PEP-8.
Para instalar essas ferramentas que usaremos em desenvolvimento, podemos usar um grupo (--group dev) do poetry focado nelas, para não serem instaladas quando nossa aplicação estiver em produção:

$ Execução no terminal!

poetry add --group dev pytest pytest-cov taskipy ruff httpx
O HTTPX foi incluído, pois ele é uma dependência do cliente de testes do FastAPI.

Configurando as ferramentas de desenvolvimento
Após a instalação das ferramentas de desenvolvimento, precisamos definir as configurações de cada uma individualmente no arquivo pyproject.toml.

Ruff
O Ruff é uma ferramenta moderna em python, escrita em rust, compatível2 com os projetos de análise estática escritos e mantidos originalmente pela comunidade no projeto PYCQA3 e tem duas funções principais:

Analisar o código de forma estática (Linter): Efetuar a verificação se estamos programando de acordo com boas práticas do python.
Formatar o código (Formatter): Efetuar a verificação do código para padronizar um estilo de código pré-definido.
Para configurar o ruff montamos a configuração em 3 tabelas distintas no arquivo pyproject.toml. Uma para as configurações globais, uma para o linter e uma para o formatador.

Configuração global

Na configuração global do Ruff queremos alterar somente duas coisas. O comprimento de linha para 79 caracteres (conforme sugerido na PEP-8) e em seguida, informaremos que o diretório de migrações de banco de dados será ignorado na checagem e na formatação:

pyproject.toml

[tool.ruff]
line-length = 79
extend-exclude = ['migrations']
Nota sobre "migrations"
Nessa fase de configuração, excluiremos a pasta migrations, isso pode não fazer muito sentido nesse momento. Contudo, quando iniciarmos o trabalho com o banco de dados, a ferramenta Alembic faz geração de código automático. Por serem códigos gerados automaticamente, não queremos alterar a configuração feita por ela.

Linter

Durante a análise estática do código, queremos buscar por coisas específicas. No Ruff, precisamos dizer exatamente o que ele deve analisar. Isso é feito por códigos. Usaremos estes:

I (Isort): Checagem de ordenação de imports em ordem alfabética
F (Pyflakes): Procura por alguns erros em relação a boas práticas de código
E (Erros pycodestyle): Erros de estilo de código
W (Avisos pycodestyle): Avisos de coisas não recomendadas no estilo de código
PL (Pylint): Como o F, também procura por erros em relação a boas práticas de código
PT (flake8-pytest): Checagem de boas práticas do Pytest
pyproject.toml

[tool.ruff.lint]
preview = true
select = ['I', 'F', 'E', 'W', 'PL', 'PT']
Para mais informações sobre a configuração e sobre os códigos do ruff e dos projetos do PyCQA, você pode checar a documentação do ruff ou as documentações originais dos projetos PyQCA.

Formatter

A formatação do Ruff praticamente não precisa ser alterada. Pois ele vai seguir as boas práticas e usar a configuração global de 79 caracteres por linha. A única alteração que farei é o uso de aspas simples ' no lugar de aspas duplas ":

pyproject.toml

[tool.ruff.format]
preview = true
quote-style = 'single'
Lembrando que a opção de usar aspas simples é totalmente pessoal, você pode usar aspas duplas se quiser.

pytest
O Pytest é uma framework de testes, que usaremos para escrever e executar nossos testes. O configuraremos para reconhecer o caminho base para execução dos testes na raiz do projeto .:

pyproject.toml

[tool.pytest.ini_options]
pythonpath = "."
addopts = '-p no:warnings'
Na segunda linha dizemos para o pytest adicionar a opção no:warnings. Para ter uma visualização mais limpa dos testes, caso alguma biblioteca exiba uma mensagem de warning, isso será suprimido pelo pytest.

Taskipy
A ideia do Taskipy é ser um executor de tarefas (task runner) complementar em nossa aplicação. No lugar de ter que lembrar comandos como o do fastapi, que vimos na execução da aplicação, que tal substituir ele simplesmente por task run?

Isso funcionaria para qualquer comando complicado em nossa aplicação. Simplificando as chamadas e também para não termos que lembrar de como executar todos os comandos de cabeça.

Alguns comandos que criaremos agora no início:

pyproject.toml

[tool.taskipy.tasks]
lint = 'ruff check . && ruff check . --diff'
format = 'ruff check . --fix && ruff format .'
run = 'fastapi dev server/app.py'
pre_test = 'task lint'
test = 'pytest -s -x --cov=api_odin -vv'
post_test = 'coverage html'
Os comandos definidos fazem o seguinte:

lint: Executa duas variações da checagem:

ruff check --diff: Mostra o que precisa ser alterado no código para que as boas práticas sejam seguidas
ruff check: Mostra os códigos de infrações de boas práticas
&&: O duplo & faz com que a segunda parte do comando só seja executada se a primeira não der erro. Sendo assim, enquanto o --diff apresentar erros, ele não executará o check
format: Executa duas variações da formatação:

ruff check --fix: Faz algumas correções de boas práticas automaticamente
ruff format: Executa a formatação do código em relação as convenções de estilo de código
run: executa o servidor de desenvolvimento do FastAPI
pre_test: executa a camada de lint antes de executar os testes
test: executa os testes com pytest de forma verbosa (-vv) e adiciona nosso código como base de cobertura
post_test: gera um report de cobertura após os testes
Para executar um comando, é bem mais simples, precisando somente passar a palavra task <comando>.

Caso precise ver o arquivo todo
Os efeitos dessas configurações de desenvolvimento
Caso você tenha copiado o código que usamos para definir fast_zero/app.py, pode testar os comandos que criamos para o taskipy:

$ Execução no terminal!

task lint
Dessa forma, veremos que cometemos algumas infrações na formatação da PEP-8. O ruff nos informará que deveríamos ter adicionado duas linhas antes de uma definição de função:


fast_odin/app.py:5:1: E302 [*] Expected 2 blank lines, found 1
Found 1 error.
[*] 1 fixable with the `--fix` option.
--- fast_zero/app.py
+++ fast_zero/app.py
@@ -2,6 +2,7 @@

 app = FastAPI()

+
 @app.get('/')
 def read_root():
     return {'message': 'Olá Mundo!'}

Would fix 1 error.
Para corrigir isso, podemos usar o nosso comando de formatação de código:


Comando
Resultado
$ Execução no terminal!

task format
Found 1 error (1 fixed, 0 remaining).
3 files left unchanged

Introdução ao Pytest: Testando o "Hello, World!"
Antes de entendermos a dinâmica dos testes, precisamos entender o efeito que eles têm no nosso código. Podemos começar analisando a cobertura (o quanto do nosso código está sendo efetivamente testado). Vamos executar os testes:

$ Execução no terminal!

task test
Teremos uma resposta como essa:

$ Execução no terminal!

=========================== test session starts ===========================
platform linux -- Python 3.11.7, pytest-7.4.4, pluggy-1.3.0
cachedir: .pytest_cache
rootdir: api_odin
configfile: pyproject.toml
plugins: cov-4.1.0, anyio-4.2.0
collected 0 items

---------- coverage: platform linux, python 3.11.7-final-0 -----------
Name                    Stmts   Miss  Cover
-------------------------------------------
server/__init__.py       0      0   100%
server/app.py            5      5     0%
-------------------------------------------
TOTAL                       5      5     0%
As linhas no terminal são referentes ao pytest, que disse que coletou 0 itens. Nenhum teste foi executado.

Caso não tenha muita experiência com Pytest
A parte importante dessa Mensagem está na tabela gerada pelo coverage. Que diz que temos 5 linhas de código (Stmts) no arquivo fast_zero/app.py e nenhuma delas está coberta pelos nossos testes. Como podemos ver na coluna Miss.

Por não encontrar nenhum teste, o pytest retornou um "erro". Isso significa que nossa tarefa post_test não foi executada. Podemos executá-la manualmente:

$ Execução no terminal!

task post_test
Wrote HTML report to htmlcov/index.html
Isso gera um relatório de cobertura de testes em formato HTML. Podemos abrir esse arquivo em nosso navegador e entender exatamente quais linhas do código não estão sendo testadas.
