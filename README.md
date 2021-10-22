# Curso Django

##Repositório criado para acompanhar os exercícios do módulo Django do Bootcamp DevPro.

### Objetivos

* Criar uma aplicação web aplicando os "_twelve factor app_", que são as boas práticas
de desenvolvimento.

###Metodologia

1. **Base de código**:
GitHub e Heroku para controle de versão e deploys.
2. **Dependências**:
Declaramos e configuramos com o a biblioteca [pip-tools](https://github.com/jazzband/pip-tools) e para isolarmos o ambiente
utilizamos o pyenv.
3. **Configurações**: Personalizamos algumas configurações como o usuário padrão do Django. 
Também utilizamos a ferramenta python-decouple para as nossas configurações de instância deixando
ela no nosso .env ou nas variáveis de ambiente.
4. **Serviços de Apoio**: Utilizamos algumas ferramentas como o GitHub Actions,
log do Heroku e do Sentry para verificar erros no sistema.
5. **Build, release, run**: Ferramenta para linter - flake8; testes com o pytest e
build com o Heroku e GitHub Actions.
6. **Processos**: Execute a aplicação com um ou mais processos que não armazenam estado - 
nosso banco de dados está isolado da aplicação.
7. **Vínculo de porta**: Configuramos uma porta específica para o nosso Postgres.
8. **Concorrência**: Instalamos o servidor de aplicação gunicorn que vai gerenciar os processos.
9. **Descartabilidade**: Maximizar a robustez com inicialização e desligamento rápido.
10. **Desenvolver para semelhantes**: Separamos as configurações em arquivos diferentes, conectamos com
S3 e imulamos esse composto no sistema arquivo local.
11. **Logs**: Tratando logs como fluxo de eventos delegados para o Sentry.
12. **Processos de Admin:** Executar tarefas de administração e gerenciamento com processos pontuais
buscando sempre automatizar ao máximo.

Aplicação disponível em https://rhsmdjango.herokuapp.com/

[![codecov](https://codecov.io/gh/rafael-hsm/curso-django/branch/main/graph/badge.svg?token=T8fmwqVzY7)](https://codecov.io/gh/rafael-hsm/curso-django)
[![Updates](https://pyup.io/repos/github/rafael-hsm/curso-django/shield.svg)](https://pyup.io/repos/github/rafael-hsm/curso-django/)
[![Python 3](https://pyup.io/repos/github/rafael-hsm/curso-django/python-3-shield.svg)](https://pyup.io/repos/github/rafael-hsm/curso-django/)

