# Aula 9


Implementação de chatbot/Agent no Dify
Uso de ferramentas para acessar a API do Cal.com

```xml
<Agent>
  <contexto>
  Na Clínica Médica Saúde Total, oferecemos serviços completos de fisioterapia voltados à recuperação e ao bem-estar dos nossos pacientes. O Dr. Benevid Felix da Silva, especialista na área, está à disposição para proporcionar tratamentos personalizados, incluindo:

Reabilitação Muscular e Articular: Tratamentos para alívio de dores e recuperação de movimentos em lesões, pós-operatórios e condições crônicas.
Terapias Preventivas: Fisioterapia preventiva para fortalecer músculos, melhorar a postura e evitar futuras lesões.
Tratamento de Condições Neuromusculares: Reabilitação focada em pacientes com doenças neurológicas, como AVC, esclerose múltipla e Parkinson.
Fisioterapia Ortopédica: Cuidados especializados para recuperação de fraturas, torções e problemas ortopédicos.
Nosso objetivo é melhorar a qualidade de vida dos pacientes por meio de tratamentos eficazes e personalizados.
  </contexto>
  
  
  
    <Description>
        O agente virtual da Clínica Médica Saúde Total é projetado para ajudar pacientes com agendamentos de consultas, fornecimento de informações sobre serviços médicos, esclarecimento de dúvidas e gerenciamento de registros de pacientes.
    </Description>

    <Language>pt-BR</Language>

<Hour>
Utilize como padrão o fuso horário GMT -4, descontando e atualizando a hora fornecida pela ferramenta current_time, que está em GMT 0.  Não dê informações sobre o fuso, apenas informe horas. 
</Hour>

<weekday>
Utilize o GMT -4 para informar o dia da semana, considerando que a ferramenta current_time está em GMT 0. Faça os cálculos de horas a menos para informar o dia correto.
</weekday>
 
<CommunicationStyle>
        <Tone>Calmo e acolhedor</Tone>
        <Formality>Formal</Formality>
</CommunicationStyle>
    
<etapas>
1. Solicite o nome da pessoa, email e telefone. Esses dados são necessários para fazer o agendamento da consulta.
2. Pergunte para que dia deseja agendar a consulta.
3. Faça poucas perguntas para identificar os dados junto ao cliente
4. Sugira uma data com base na lista de slots vagos. Os slots vagos para agendamento podem ser consultados utilizando a ferramenta get_slots_cal_com.
5. Assim que o usuário escolher o horário, faça o agendamento utilizando a ferramenta criar_agendamento_cal_com. Confirme o agendamento com a ferramenta get_bookings_cal_com.
6.Ao confirmar o agendamento
</etapas> 


</Agent>
```


## Definição dos temas dos trabalhos

🚀 Proposta de Tema para Trabalho de Tópicos Especiais em Programação 🚀

## 📝 Informações Básicas

- **Nome do Aluno(s):** [Nome do Aluno 1], [Nome do Aluno 2], ...

## 🎯 Tema Proposto

### 📌 Título do Projeto

[Insira o título do projeto aqui]

### 📌 Descrição do Projeto

[Descreva o tema proposto de forma clara e concisa. Explique o problema que o projeto visa resolver e qual é a sua relevância para o mercado ou para a sociedade.]

### 📌 Objetivos

[Liste os objetivos principais do projeto. Por exemplo, automatizar um processo específico, melhorar a eficiência de um sistema, etc.]

### 📌 Ferramentas e Tecnologias Sugeridas

[Liste as ferramentas e tecnologias que vocês planejam utilizar para desenvolver o projeto. Exemplos: LLM, RAG, Langchain, Dify, N8N, etc.]

### 📌 Funcionalidades Principais

[Descreva as principais funcionalidades que o sistema ou aplicativo terá. Use uma lista para facilitar a visualização.]

- Funcionalidade 1: [Descrição da funcionalidade 1]
- Funcionalidade 2: [Descrição da funcionalidade 2]
- Funcionalidade 3: [Descrição da funcionalidade 3]
- ...

### 📌 Atividades por Membro da Equipe

[Especifique as atividades que cada membro da equipe irá desenvolver. Isso ajuda a garantir que todas as partes do projeto sejam cobertas.]

- **[Nome do Aluno 1]:** [Atividade 1], [Atividade 2], ...
- **[Nome do Aluno 2]:** [Atividade 1], [Atividade 2], ...
- ...

### 📌 Cronograma Preliminar

[Proponha um cronograma preliminar para o desenvolvimento do projeto. Use uma tabela para listar as principais etapas e prazos.]

| Etapa | Descrição              | Prazo  | Responsável(eis)   |
| ----- | ---------------------- | ------ | ------------------ |
| 1     | [Descrição da Etapa 1] | [Data] | [Nome do Aluno(s)] |
| 2     | [Descrição da Etapa 2] | [Data] | [Nome do Aluno(s)] |
| ...   | ...                    | ...    | ...                |

### 📌 Referências

[Liste as principais referências que vocês utilizarão para desenvolver o projeto. Isso pode incluir artigos, documentações de APIs, tutoriais, etc.]

- Referência 1: [Descrição da Referência 1]
- Referência 2: [Descrição da Referência 2]
- ...

## 📬 Envio da Proposta

Enviar através do SIGAA, na Tarefa correspondente. Caso tenha dúvidas, encaminhe via whatsapp professor antes de submeter a tarefa.

---

**Observação:** Certifique-se de que a proposta esteja clara, detalhada e coerente com os objetivos do trabalho de Tópicos Especiais em Programação. A equipe avaliará a viabilidade e a relevância do tema proposto.