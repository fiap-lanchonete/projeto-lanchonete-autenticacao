[![Deploy CD](https://github.com/fiap-lanchonete/projeto-lanchonete-pedido/actions/workflows/deploy.yaml/badge.svg)](https://github.com/fiap-lanchonete/projeto-lanchonete-autenticacao/actions/workflows/deploy.yaml)

# Tech Challenge - Pós-Tech SOAT - FIAP

Alunos:

* Pedro Henrique de Marins da Silva - RM348617
* Gustavo Jorge Franco Teles dos Santos - RM349553

## O PROBLEMA

Há uma lanchonete de bairro que está expandindo devido seu grande sucesso. Porém, com a expansão e sem um sistema de controle de pedidos, o atendimento aos clientes pode ser caótico e confuso. Por exemplo, imagine que um cliente faça um pedido complexo, como um hambúrguer personalizado com ingredientes específicos, acompanhado de batatas fritas e uma bebida. O atendente pode anotar o pedido em um papel e entregá-lo à cozinha, mas não há garantia de que o pedido será preparado corretamente.

Sem um sistema de controle de pedidos, pode haver confusão entre os atendentes e a cozinha, resultando em atrasos na preparação e entrega dos pedidos. Os pedidos podem ser perdidos, mal interpretados ou esquecidos, levando à insatisfação dos clientes e a perda de negócios.

Em resumo, um sistema de controle de pedidos é essencial para garantir que a lanchonete possa atender os clientes de maneira eficiente, gerenciando seus pedidos e estoques de forma adequada. Sem ele, expandir a lanchonete pode acabar não dando certo, resultando em clientes insatisfeitos e impactando os negócios de forma negativa.

Para solucionar o problema, a lanchonete irá investir em um sistema de autoatendimento de fast food, que é composto por uma série de dispositivos e interfaces que permitem aos clientes selecionar e fazer pedidos sem precisar interagir com um atendente, com as seguintes

## REPOSITÓRIOS:
  - [Repositório do serviço de autenticação](https://github.com/fiap-lanchonete/projeto-lanchonete-autenticacao)
  - [Repositório para Infra Kubernetes](https://github.com/fiap-lanchonete/projeto-lanchonete-infra)
  - [Repositório para infra do banco de dados](https://github.com/fiap-lanchonete/infra-db)
  - [Repositório do serviço de pagamento](https://github.com/fiap-lanchonete/fiap-payment)
  - [Repositório do serviço de pedido](https://github.com/fiap-lanchonete/projeto-lanchonete-pedido)
  - [Repositório do serviço de produção](https://github.com/fiap-lanchonete/projeto-lanchonete-producao)

## SONAR

![Sonar](https://i.imgur.com/yBf7jI7.png)

O SonarQube será integrado ao pipeline de Integração Contínua (CI) para garantir a qualidade do código e a cobertura de testes. A cada novo commit no repositório, o pipeline será acionado, realizando automaticamente a análise do código com o SonarQube. Esta análise inclui a verificação de bugs, vulnerabilidades de segurança, dívida técnica e, claro, a cobertura de testes.

Para garantir um padrão elevado de qualidade, configuraremos o SonarQube para falhar a build caso a cobertura de testes seja inferior a 80%. Isso significa que, se o código submetido não atender a esse critério, a equipe será notificada para fazer as devidas correções antes que o código possa ser integrado à base principal.

## BANCO DE DADOS

Para esta fase, foram utilizados os seguintes bancos de dados:

* Autenticação - PostgreSQL
* Pagamento - MongoDB
* Pedido - PostgreSQL
* Produção - PostgreSQL

### Estrutura dos Bancos

#### Serviço de Pedido
![ERD](https://i.imgur.com/dYDdQDp.png)

#### Serviço de Produção
![ERD](https://i.imgur.com/FpVB43m.png)

#### Serviço de Pagamento
![ERD](https://i.imgur.com/wdyexbz.png)

## AUTENTICAÇÃO
![Authentication Diagram](https://i.imgur.com/6Qjckdd.png)

O diagrama acima ilustra o fluxo de autenticação do nosso sistema. O usuário inicia o processo fornecendo o CPF, ou de forma anônima. Em seguida, o sistema valida essas credenciais e, se estiverem corretas, gera um token de acesso. Este token é então usado para autenticar todas as solicitações subsequentes do usuário. Isso garante que apenas usuários autenticados possam acessar recursos protegidos (criação de pedido).

### FLUXO DE PAGAMENTO COM MERCADO PAGO
<img  src="https://i.imgur.com/Df8C9c6.png" />

### ROTAS DA API

#### Autenticação

- **POST /registration** Cadastro de usuário, é necessário preencher nome, cpf e email

- **POST /login** Rota onde é necessário preencher o cpf para realizar o login.

- **POST /login_anonymous** Realizar login sem fazer cadastro.

#### Pagamento

- **POST /webhook/event** Receber eventos do mercado pago.

- **GET /status/:id** Verificar status do pagamento.

- **GET /:id** Buscar pagamento pelo id.

#### Pedido

- **POST /v1/category:** Esta rota permite criar uma nova categoria.

- **GET /v1/category:** Esta rota permite obter a lista de categorias disponíveis.

- **GET /v1/category/:id:** Esta rota permite obter informações sobre uma categoria específica identificada pelo parâmetro `id`.

- **PUT /v1/category/:id:** Esta rota permite atualizar informações de uma categoria específica identificada pelo parâmetro `id`.

- **DELETE /v1/category/:id:** Esta rota permite excluir uma categoria específica identificada pelo parâmetro `id`.

- **POST /v1/product:** Esta rota permite criar um novo produto.

- **GET /v1/product:** Esta rota permite obter a lista de produtos disponíveis.

- **GET /v1/product/:id:** Esta rota permite obter informações sobre um produto específico identificado pelo parâmetro `id`.

- **PUT /v1/product/:id:** Esta rota permite atualizar as informações de um produto específico identificado pelo parâmetro `id`.

- **DELETE /v1/product/:id:** Esta rota permite excluir um produto específico identificado pelo parâmetro `id`.

- **POST /v1/order** Está rota permite criar um pedido.

- **GET /v1/order/:id** Consultar um pedido pelo parâmetro `id`.

- **PUT /v1/order/:id** Modificar os produtos do pedido pelo `id`.

- **PUT /v1/order/start-payment/:id** Mandar pedido para o serviço de pagamentos.

#### Produção

- **GET /v1/order/queue:** Esta rota permite obter informações sobre a fila de pedidos, geralmente usada para listar os pedidos pendentes.

- **POST /v1/order** Está rota permite criar um pedido.

- **POST /v1/in_preparation** Receber um pedido no serviço de Produção e mover o status para Em Preparo.

- **POST /v1/ready/:id** Mover o pedido status pronto para ser retirado.

- **POST /v1/finished/:id** Mover o pedido para concluído após a retirada.

## ARQUITETURA

A arquitetura dessa API segue os princípios de Arquitetura Hexagonal (Ports and Adapters). Essa arquitetura pode ser dividida em duas partes:

  - Condutores: (ou atores primários): Podem ser definidos como atores que iniciam a interação. Por exemplo, um condutor pode ser um controller que recebe um input de um usuário e redireciona a aplicação utilizando uma Port(interface).
  - Conduzidos: (também conhecido como atores secundários): São parte da camada de infrasctructure da aplicação. Podem ser utilizados para adicionar funcionalidades para o domínio da aplicação. Exemplos: Banco de dados, APIs externas.

![Untitled Diagram drawio](https://github.com/rickwalking/projeto-lanchonete/assets/25574889/12ddab40-97ec-4157-a1ae-803d258654ea)

  * Esquema de Domain Driven Design (DDD) no [Miro](https://miro.com/welcomeonboard/TG9pRTJMU1BNb2d4WUZvdE9PVHd1cEZudmpaczNhdDNMOVVmeDE0S0VOZkVDSmFDSG5uaU0waUZzdFV5Q1h5aXwzNDU4NzY0NTU1MDkxMDI0MTAxfDI=?share_link_id=171801921364)

## PADRÃO SAGA

O padrão Saga foi escolhido para esta implementação devido à sua capacidade de gerenciar transações distribuídas complexas, garantindo a consistência dos dados em microserviços. A coreografia do Saga, em particular, permite que cada serviço execute suas operações de forma independente e comunique o resultado através de eventos, o que aumenta a resiliência e a escalabilidade do sistema.

Neste caso, o processo começa com o Serviço de Autenticação, que é responsável por verificar a identidade do usuário e conceder permissões para realizar operações. Uma vez autenticado, uma chave de idempotência é criada e publicada na fila.
Então, o pedido é criado pelo Serviço de Pedido, que então publica um evento indicando a criação do pedido.

O Serviço de Pagamento escuta esse evento e, em seguida, processa o pagamento do pedido. Se o pagamento for bem-sucedido, ele publica um evento de sucesso de pagamento, que é capturado pelo Serviço de Produção. O Serviço de Produção, ao receber a confirmação do pagamento, inicia a preparação do pedido.

Cada etapa do processo é realizada de forma assíncrona e independente, permitindo que o sistema seja mais tolerante a falhas e facilmente escalável. Além disso, a coreografia do Saga facilita a adição de novos serviços ou a modificação de processos existentes sem afetar significativamente os outros serviços, mantendo a integridade e a consistência dos dados em toda a aplicação.

A chave de idempotência será uma referência única para cada pedido, garantindo que o pedido seja processado apenas uma vez, mesmo que o evento seja processado mais de uma vez.

A escolha do Amazon MQ foi feita para garantir a confiabilidade e a escalabilidade do sistema. O Amazon MQ é um serviço de mensageria gerenciado que oferece suporte a mensagens de fila e tópico usando o protocolo de mensagens padrão do setor.

![SAGA](https://i.imgur.com/EL9j6oH.png)

## RELATÓRIO DE IMPACTO E PROTEÇÃO DE DADOS (RIPD) - Sistema Lanchonete
[Link para o documento](https://docs.google.com/document/d/1C5Dg6JXd4F31ERT-66dxdwzVbRlQYMRUye0u9dnHn2Q/edit)

## KUBERNETES E DEPLOY

Este projeto utiliza Kubernetes para orquestrar os serviços de Cadastro, Pagamento, Pedido e Produção. O processo de deploy é realizado através pipeline de Integração Contínua (CI) que é ativada sempre que um novo código é enviado para a branch principal do repositório.

A pipeline de CI realiza as seguintes etapas:

- Verificação do código: O código é verificado para garantir que não haja erros de sintaxe ou problemas de estilo de código.
- Construção da imagem Docker: Uma nova imagem Docker é construída para cada serviço (Cadastro, Pagamento, Pedido e Produção). Esta imagem contém tudo o que o serviço precisa para ser executado, incluindo o código do serviço e todas as suas dependências.
- Push da imagem para Docker Hub: A imagem Docker construída é enviada para um repositório de imagens Docker.
- Atualização do Kubernetes: O Kubernetes é informado sobre a nova imagem Docker. Ele então atualiza os serviços em execução para usar a nova imagem. Isso é feito de maneira a minimizar o tempo de inatividade do serviço.

Este processo garante que o código mais recente esteja sempre em execução nos serviços e que qualquer problema seja detectado e corrigido o mais rápido possível.

## PROJETOS USANDO DOCKER

Os serviços de Pagamento, Autenticação, Pedido e Produção utilizam o Docker. Por este motivo, será necessária apenas a instalação do Docker, não sendo necessária a instalação manual do projeto. Também não será necessária a instalação manual do banco de dados.

Caso não tenha o Docker instalado, siga as instruções para seu sistema operacional na [documentação oficial do Docker](https://docs.docker.com/get-docker/).

### PARA EXECUTAR EM AMBIENTE DE DESENVOLVIMENTO

* Clone este repositório em seu computador;
* Entre no diretório local onde o repositório foi clonado;
* Altere o arquivo .env.example para .env
* Preencha os campos dentro arquivo
* Utilize o comando ` docker compose up --build` para "build" e subir o servidor local e expor a porta 3000 em `localhost`. Além de `dev` também subirá o serviço `db` com o banco de dados de desenvolvimento.

**IMPORTANTE:** Esta API está programada para ser acessada a partir de `http://localhost:3000` e o banco de dados utiliza a porta `5432`. Certifique-se de que não existam outros recursos ocupando as portas acima.

Para desativar os serviços, execute o comando `docker-compose down`.

## DOCUMENTAÇÃO UTILIZANDO O SWAGGER

Para acessar a documentação do Swagger, inicie o servidor e acesse a rota `/api` no seu navegador. Por exemplo, se o servidor estiver rodando localmente na porta 3000, você pode acessar a documentação do Swagger em `http://localhost:3000/api`.

## EVIDÊNCIAS DO DEPLOY
A seguir, serão apresentadas o link para um vídeo com as evidências do processo de deploy. Os vídeos demonstram as etapas concluídas com sucesso e garantem que o sistema está configurado e operando conforme esperado. A visualização destas evidências é crucial para a verificação e validação do processo de implantação dos serviços (como foi requisitado no desafio).

[Link para o vídeo](https://www.youtube.com/watch?v=8LHHZUPsQ8s&ab_channel=PedroMarins)
