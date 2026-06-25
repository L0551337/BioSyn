 * BioSyn *

* Sistema de gerenciamento para floriculturas, viveiros, estufas e jardins botânicos.

# Sobre o Projeto

O BioSyn é uma plataforma desenvolvida para auxiliar na gestão de estabelecimentos que trabalham com plantas, permitindo o controle de funcionários, atividades periódicas, catálogo de espécies e acompanhamento das operações diárias.O sistema foi criado para automatizar processos rotineiros, reduzir falhas operacionais e garantir que os cuidados necessários para cada planta sejam realizados dentro dos períodos estabelecidos.

------------------------

# Objetivo

Desenvolver uma solução capaz de organizar e automatizar as atividades de manutenção de plantas, além de centralizar informações importantes sobre funcionários, tarefas e catálogo botânico.

------------------------

# Principais Funcionalidades

* Gestão de Funcionários

- Cadastro de funcionários.
- Edição e exclusão de funcionários.
- Controle de cargos e responsabilidades.
- Associação de tarefas aos funcionários.

* Gestão de Tarefas

- Criação de atividades periódicas.
- Definição da frequência de execução.
- Atribuição automática para funcionários.
- Registro de conclusão das atividades.
- Histórico de tarefas realizadas.

* Automatização de Atividades

O administrador pode cadastrar atividades recorrentes.

**Exemplo:**

Atividade: Regar Orquídeas  
Periodicidade: A cada 3 dias

Após o funcionário concluir a atividade, ela será automaticamente reagendada para ficar disponível novamente após o período definido.

* Catálogo Botânico

- Cadastro de plantas.
- Informações detalhadas sobre cada espécie.
- Valor comercial.
- Cuidados específicos.
- Observações gerais.

* Painel Administrativo

- Visualização geral das atividades.
- Controle dos funcionários.
- Gerenciamento das plantas cadastradas.
- Monitoramento das tarefas pendentes e concluídas.

---

# Tecnologias Utilizadas

* Back-end

- Python
- Flask

* Front-end

- HTML5
- CSS3
- JavaScript

* Banco de Dados

- MySQL

* Testes

- Cypress

* Controle de Versão

- GitHub

---

# Arquitetura do Sistema

O sistema segue a arquitetura cliente-servidor.

* Front-end

Responsável pela interface do usuário.

* Back-end

Responsável pelas regras de negócio, autenticação, geração automática de tarefas e comunicação com o banco de dados.

* Banco de Dados

Responsável pelo armazenamento persistente das informações.

---

# Requisitos Funcionais:

* 01
O sistema deve permitir o cadastro de funcionários.

* 02
O sistema deve permitir editar informações dos funcionários.

* 03
O sistema deve permitir excluir funcionários.

* 04
O sistema deve permitir cadastrar plantas.

* 05
O sistema deve permitir editar informações das plantas.

* 06
O sistema deve permitir excluir plantas.

* 07
O sistema deve permitir cadastrar tarefas.

* 08
O sistema deve permitir definir periodicidade para as tarefas.

* 09
O sistema deve permitir associar tarefas a funcionários.

* 10
O sistema deve registrar a conclusão de tarefas.

* 11
O sistema deve gerar automaticamente novas tarefas com base na periodicidade definida.

* 12
O administrador deve visualizar todas as tarefas do sistema.

* 13
O sistema deve armazenar informações de cuidados específicos das plantas.

* 14
O sistema deve exibir um catálogo das plantas cadastradas.

---

# Requisitos Não Funcionais:

* 01
O sistema deve possuir interface intuitiva.

* 02
O sistema deve responder às requisições em tempo adequado.

* 03
Os dados devem ser armazenados de forma segura.

* 04
O sistema deve ser compatível com os principais navegadores modernos.

* 05
O sistema deve utilizar autenticação para acesso administrativo.

* 06
O sistema deve manter a integridade das informações armazenadas.

---

# Casos de Uso

* Administrador

- Gerenciar funcionários.
- Gerenciar plantas.
- Criar tarefas.
- Configurar periodicidade.
- Visualizar relatórios.
- Acompanhar execução das atividades.

* Funcionário

- Visualizar tarefas atribuídas.
- Marcar tarefas como concluídas.
- Consultar informações das plantas.

---


# Testes

Os testes automatizados são realizados utilizando Cypress.


# Verificação e Validação

* Verificação

Processo utilizado para garantir que o sistema foi desenvolvido corretamente.

Atividades realizadas:

- Revisão dos requisitos.
- Revisão do banco de dados.
- Revisão do código-fonte.

* Validação

Processo utilizado para garantir que o sistema atende às necessidades dos usuários.

Atividades realizadas:

- Testes funcionais.
- Testes de interface.
- Testes de usabilidade.
- Testes automatizados com Cypress.
- Validação dos fluxos de tarefas periódicas.

---

# Benefícios do Sistema

- Automatização de processos repetitivos.
- Melhor organização operacional.
- Redução de falhas humanas.
- Acompanhamento do desempenho dos funcionários.
- Centralização das informações sobre plantas.
- Maior eficiência na manutenção de viveiros e floriculturas.

---

# Futuras Implementações

- Aplicativo mobile.
- Notificações em tempo real.
- Relatórios avançados.
- Dashboard com indicadores.
- Controle de estoque.
- Integração com vendas.
- QR Code para identificação das plantas.

---

# Equipe de Desenvolvimento

Projeto acadêmico desenvolvido para a disciplina de Fábrica de Software 2.

* Discentes: - Bruno Gonçalves do Santos
	     - Enzo Lustosa Pacheco Tosta de Almeida
             - Rafael Graciano
             - Messias Ribeiro Lima

Sistema: BioSyn  
Tecnologias: Flask, Python, MySQL, HTML, CSS, JavaScript e Cypress.

---

# Licença

Este projeto possui finalidade acadêmica e educacional.