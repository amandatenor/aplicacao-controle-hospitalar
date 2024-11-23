# 🏥 Aplicativo de Hospital

## Visão Geral
Este aplicativo de hospital oferece um sistema de gerenciamento abrangente que permite aos usuários controlar entidades-chave: **Paciente**, **Procedimento** e **Consulta**. Com foco na facilidade de uso e no manuseio eficiente de dados, o aplicativo oferece funcionalidades para inserção, edição, exclusão e consulta dessas entidades. Além disso, mantém registros de todos os eventos para garantir rastreabilidade detalhada.

---

## Funcionalidades

### Gerenciamento de Entidades
- **Gerenciamento de Pacientes**:
  - Adicionar, atualizar, excluir e pesquisar pacientes.
- **Gerenciamento de Procedimentos**:
  - Adicionar, atualizar, excluir e pesquisar procedimentos.
- **Gerenciamento de Consultas**:
  - Registrar consultas vinculando um paciente a uma lista de procedimentos realizados e à data da consulta.
  - Editar e remover consultas conforme necessário.
  - Garantir atualizações automáticas em consultas relacionadas quando pacientes ou procedimentos forem excluídos.

### Sistema de Logs
- **Registro abrangente de eventos**:
  - Captura de operações como criação, modificação, exclusão e pesquisa de entidades.
  - Garante rastreabilidade das ações dos usuários e das alterações nos dados.

### Armazenamento de Dados
- Os dados são armazenados em arquivos de formato .csv (Comma Separated Values) referentes às suas respectivas classes e funcionalidades.


---

## Considerações Importantes
- **Consistência de Dados**:
  - A exclusão de um **Paciente** ou **Procedimento** aciona atualizações em qualquer **Consulta** relacionada, garantindo consistência no banco de dados.
- **Integridade dos Registros**:
  - O sistema de logs aprimora a observabilidade e mantém a integridade do histórico de operações do aplicativo.
