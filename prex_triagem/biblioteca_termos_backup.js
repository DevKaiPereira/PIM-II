const knowledgeLibrary = {
  pillars: [
    {
      id: "P1",
      name: "Admissibilidade e Vínculo",
      definition: "Validação da legitimidade do proponente e sua situação funcional perante o IFB.",
      regra: "PREX 42/2020 Art. 15 e Editais Vigentes",
      processes: [
        {
          id: "PROC1",
          name: "Vínculo Permanente",
          concepts: [
            {
              termo_principal: "proponente",
              sinonimos: [
                "autor", 
                "coordenador-geral", 
                "servidor proponente",
                "coordenador da proposta",
                "responsável pelo projeto",
                "propositor",
                "coordenador titular",
                "requerente"
              ],
              contexto_obrigatorio: [
                "efetivo", 
                "permanente", 
                "siape", 
                "ativo",
                "quadro permanente",
                "servidor do quadro",
                "vínculo efetivo",
                "cargo permanente",
                "lotação definitiva",
                "concurso público"
              ],
              contexto_negacao: [
                "substituto", 
                "temporário", 
                "colaboração técnica",
                "professor substituto",
                "contrato temporário",
                "visitante",
                "cedido",
                "requisitado",
                "colaborador eventual",
                "prestador de serviço",
                "estagiário",
                "bolsista externo"
              ],
              peso_relevancia: 2.0
            },
            {
              termo_principal: "exercício pleno",
              sinonimos: [
                "pleno exercício", 
                "assiduidade", 
                "em exercício",
                "exercício ativo",
                "atividade presencial",
                "frequência regular",
                "disponibilidade integral",
                "carga horária compatível",
                "sem restrições funcionais",
                "aptidão para coordenar"
              ],
              contexto_obrigatorio: [
                "não afastado", 
                "sem licença",
                "disponível",
                "sem impedimentos",
                "comparecimento regular",
                "carga horária preservada",
                "sem restrições médicas",
                "sem afastamentos legais"
              ],
              contexto_negacao: [
                "afastado", 
                "licença prêmio", 
                "capacitação integral",
                "afastamento para pós-graduação",
                "licença para tratar de interesses particulares",
                "licença saúde",
                "licença maternidade",
                "afastamento integral",
                "licença para acompanhar cônjuge",
                "licença para atividade política",
                "afastamento para missão oficial",
                "cedido a outro órgão",
                "licença capacitação",
                "licença gestante"
              ],
              peso_relevancia: 1.8
            },
            {
              termo_principal: "categoria funcional",
              sinonimos: [
                "carreira",
                "cargo",
                "função",
                "enquadramento",
                "classe funcional",
                "nível de classificação"
              ],
              contexto_obrigatorio: [
                "docente",
                "técnico-administrativo",
                "professor",
                "servidor público federal"
              ],
              contexto_negacao: [
                "terceirizado",
                "voluntário",
                "colaborador externo",
                "sem vínculo"
              ],
              peso_relevancia: 1.5
            }
          ]
        },
        {
          id: "PROC_ADIM",
          name: "Status de Adimplência",
          concepts: [
            {
              termo_principal: "nada consta",
              sinonimos: [
                "certidão de adimplência", 
                "sem pendências", 
                "relatório homologado",
                "adimplente",
                "regularidade comprovada",
                "declaração de nada consta",
                "certidão negativa",
                "regularidade fiscal",
                "quitação de débitos",
                "situação regular",
                "conformidade documental",
                "adimplência verificada"
              ],
              contexto_obrigatorio: [
                "prex", 
                "suap", 
                "prestação de contas",
                "relatório final",
                "comprovante de entrega",
                "protocolo de submissão",
                "validação automática",
                "sistema de projetos",
                "módulo de extensão",
                "certidão emitida"
              ],
              contexto_negacao: [
                "pendente",
                "em débito",
                "relatório atrasado",
                "prestação de contas pendente",
                "inadimplente",
                "irregular",
                "não homologado",
                "relatório rejeitado",
                "com pendências",
                "diligência em aberto"
              ],
              peso_relevancia: 2.0
            }
          ]
        }
      ]
    },
    {
      id: "P2",
      name: "Configuração de Equipe",
      definition: "Regras de composição da força de trabalho e protagonismo discente.",
      regra: "PREX 42/2020 Art. 19 e 20",
      processes: [
        {
          id: "PROC_DISC",
          name: "Participação Discente",
          concepts: [
            {
              termo_principal: "estudante",
              sinonimos: [
                "discente", 
                "aluno matriculado", 
                "estudante do IFB",
                "aluno regular",
                "corpo discente",
                "graduando",
                "aluno bolsista",
                "estudante extensionista",
                "discente participante",
                "educando",
                "aprendiz"
              ],
              contexto_obrigatorio: [
                "regularmente matriculado", 
                "bolsista", 
                "voluntário",
                "matrícula ativa",
                "curso regular",
                "formação técnica",
                "graduação",
                "ensino médio integrado",
                "matrícula confirmada",
                "participação comprovada",
                "frequência escolar",
                "coeficiente de rendimento"
              ],
              contexto_negacao: [
                "egresso",
                "ex-aluno",
                "desistente",
                "matrícula trancada",
                "desligado",
                "transferido",
                "jubilado"
              ],
              peso_relevancia: 1.9
            },
            {
              termo_principal: "protagonismo estudantil",
              sinonimos: [
                "participação ativa",
                "liderança discente",
                "autonomia estudantil",
                "envolvimento discente",
                "protagonismo juvenil",
                "empoderamento estudantil"
              ],
              contexto_obrigatorio: [
                "tomada de decisão",
                "planejamento participativo",
                "execução compartilhada",
                "avaliação coletiva",
                "construção conjunta"
              ],
              peso_relevancia: 1.7
            }
          ]
        },
        {
          id: "PROC_ORIENT",
          name: "Orientação Técnica",
          concepts: [
            {
              termo_principal: "orientação docente",
              sinonimos: [
                "docente orientador", 
                "professor orientador", 
                "supervisão",
                "tutoria acadêmica",
                "orientação pedagógica",
                "acompanhamento docente",
                "mentoria",
                "orientador responsável",
                "professor supervisor",
                "orientador técnico"
              ],
              contexto_obrigatorio: [
                "obrigatório", 
                "técnico-administrativo", 
                "bolsistas",
                "supervisão obrigatória",
                "acompanhamento pedagógico",
                "orientação de projetos",
                "coordenação compartilhada",
                "equipe multidisciplinar",
                "formação complementar",
                "aprendizagem supervisionada"
              ],
              peso_relevancia: 1.8
            },
            {
              termo_principal: "equipe executora",
              sinonimos: [
                "membros da equipe",
                "colaboradores",
                "participantes",
                "integrantes",
                "força de trabalho",
                "recursos humanos",
                "equipe do projeto",
                "grupo de trabalho"
              ],
              contexto_obrigatorio: [
                "multidisciplinar",
                "interdisciplinar",
                "complementar",
                "diversidade de formação"
              ],
              peso_relevancia: 1.4
            }
          ]
        },
        {
          id: "PROC_COORD",
          name: "Estrutura de Coordenação",
          concepts: [
            {
              termo_principal: "coordenador único",
              sinonimos: [
                "coordenação singular",
                "líder do projeto",
                "gestor responsável",
                "coordenador exclusivo",
                "titular da coordenação",
                "coordenador-geral"
              ],
              contexto_obrigatorio: [
                "único",
                "exclusivo",
                "individual",
                "centralizado"
              ],
              contexto_negacao: [
                "co-coordenador",
                "coordenação compartilhada",
                "dupla coordenação",
                "coordenadores múltiplos",
                "coordenação colegiada",
                "mais de um coordenador"
              ],
              peso_relevancia: 1.6
            }
          ]
        }
      ]
    },
    {
      id: "P3",
      name: "Dimensão Pedagógica",
      definition: "Integração das funções finalísticas e impacto social.",
      regra: "PREX 42/2020 Art. 4 e 5",
      processes: [
        {
          id: "PROC_INDISS",
          name: "Indissociabilidade",
          concepts: [
            {
              termo_principal: "indissociabilidade",
              sinonimos: [
                "articulação ensino-pesquisa", 
                "interdisciplinaridade", 
                "formação integral",
                "integração acadêmica",
                "tripé universitário",
                "articulação teórico-prática",
                "convergência formativa",
                "integração ensino-extensão-pesquisa",
                "formação holística",
                "educação integrada"
              ],
              contexto_obrigatorio: [
                "estudantes", 
                "aprendizagem", 
                "prática", 
                "pesquisa aplicada",
                "inovação",
                "produção científica",
                "metodologia ativa",
                "saberes acadêmicos",
                "conhecimento teórico",
                "aplicação prática",
                "desenvolvimento científico",
                "produção tecnológica"
              ],
              peso_relevancia: 1.8
            },
            {
              termo_principal: "interdisciplinaridade",
              sinonimos: [
                "multidisciplinar",
                "transdisciplinar",
                "diálogo de saberes",
                "integração disciplinar",
                "convergência de áreas",
                "abordagem integrada"
              ],
              contexto_obrigatorio: [
                "diferentes áreas",
                "múltiplos conhecimentos",
                "saberes diversos",
                "integração curricular"
              ],
              peso_relevancia: 1.6
            }
          ]
        },
        {
          id: "PROC_EXT",
          name: "Interação Dialógica",
          concepts: [
            {
              termo_principal: "público-alvo",
              sinonimos: [
                "comunidade externa", 
                "beneficiários", 
                "público misto",
                "população atendida",
                "público beneficiário",
                "comunidade participante",
                "segmento social",
                "grupo focal",
                "destinatários",
                "atores sociais"
              ],
              contexto_obrigatorio: [
                "impacto social", 
                "sociedade", 
                "demandas sociais",
                "transformação social",
                "inclusão social",
                "cidadania",
                "direitos humanos",
                "vulnerabilidade social",
                "desenvolvimento comunitário",
                "participação social",
                "controle social",
                "protagonismo comunitário"
              ],
              contexto_negacao: [
                "somente servidores", 
                "comunidade interna exclusiva",
                "restrito ao campus",
                "apenas alunos",
                "público interno",
                "exclusivamente IFB"
              ],
              peso_relevancia: 1.7
            },
            {
              termo_principal: "impacto social",
              sinonimos: [
                "relevância social",
                "alcance comunitário",
                "benefício público",
                "retorno à sociedade",
                "transformação comunitária",
                "engajamento social"
              ],
              contexto_obrigatorio: [
                "resultados mensuráveis",
                "indicadores sociais",
                "mudança social",
                "desenvolvimento local",
                "melhoria da qualidade de vida"
              ],
              peso_relevancia: 1.7
            }
          ]
        },
        {
          id: "PROC_AVAL",
          name: "Avaliação e Aprendizagem",
          concepts: [
            {
              termo_principal: "avaliação formativa",
              sinonimos: [
                "avaliação contínua",
                "feedback processual",
                "avaliação dialógica",
                "monitoramento",
                "acompanhamento avaliativo"
              ],
              contexto_obrigatorio: [
                "processo ensino-aprendizagem",
                "desenvolvimento de competências",
                "reflexão crítica",
                "autoavaliação"
              ],
              peso_relevancia: 1.5
            }
          ]
        }
      ]
    },
    {
      id: "P4",
      name: "Enquadramento Estratégico",
      definition: "Classificação temática e tipológica da ação.",
      regra: "PREX 42/2020 Art. 8 (Áreas Temáticas)",
      processes: [
        {
          id: "PROC_TEMA",
          name: "Áreas Temáticas",
          concepts: [
            {
              termo_principal: "áreas de extensão",
              sinonimos: [
                "comunicação", 
                "cultura", 
                "direitos humanos", 
                "educação", 
                "meio ambiente", 
                "saúde", 
                "tecnologia", 
                "trabalho",
                "áreas temáticas",
                "eixos temáticos",
                "campos de atuação",
                "linhas de extensão",
                "temáticas extensionistas",
                "áreas prioritárias",
                "campos temáticos"
              ],
              contexto_obrigatorio: [
                "vinculação", 
                "área prioritária", 
                "pdi",
                "plano de desenvolvimento institucional",
                "convergência institucional",
                "alinhamento estratégico",
                "política de extensão",
                "missão institucional",
                "objetivos estratégicos",
                "consonância temática"
              ],
              peso_relevancia: 1.5
            },
            {
              termo_principal: "abrangência territorial",
              sinonimos: [
                "alcance geográfico",
                "cobertura territorial",
                "local de realização",
                "área de abrangência",
                "localização estratégica"
              ],
              contexto_obrigatorio: [
                "local",
                "regional",
                "nacional",
                "internacional",
                "território de abrangência"
              ],
              peso_relevancia: 1.4
            }
          ]
        },
        {
          id: "PROC_TIPO",
          name: "Tipologia da Ação",
          concepts: [
            {
              termo_principal: "classificação",
              sinonimos: [
                "programa de extensão", 
                "projeto de extensão", 
                "curso", 
                "evento", 
                "prestação de serviço",
                "modalidade",
                "natureza da ação",
                "tipo de atividade",
                "categoria extensionista",
                "formato da ação",
                "tipologia extensionista"
              ],
              contexto_obrigatorio: [
                "modalidade", 
                "suap", 
                "natureza",
                "eixos de trabalho",
                "módulo de extensão",
                "classificação sistêmica",
                "categoria no sistema",
                "registro acadêmico",
                "certificação"
              ],
              peso_relevancia: 1.6
            },
            {
              termo_principal: "modalidade específica",
              sinonimos: [
                "oficina",
                "minicurso",
                "palestra",
                "workshop",
                "seminário",
                "congresso",
                "feira",
                "exposição",
                "apresentação cultural",
                "intervenção artística"
              ],
              contexto_obrigatorio: [
                "carga horária",
                "público previsto",
                "metodologia específica"
              ],
              peso_relevancia: 1.3
            }
          ]
        }
      ]
    },
    {
      id: "P5",
      name: "Recursos e Viabilidade",
      definition: "Governança financeira e infraestrutura de execução.",
      regra: "PREX 42/2020 Art. 29 (VIII, IX e X)",
      processes: [
        {
          id: "PROC_FIN",
          name: "Planejamento Financeiro",
          concepts: [
            {
              termo_principal: "orçamento",
              sinonimos: [
                "planilha orçamentária", 
                "financeiro", 
                "ajuda de custo", 
                "bolsas",
                "recursos financeiros",
                "dotação orçamentária",
                "previsão de gastos",
                "planejamento financeiro",
                "quadro de desembolso",
                "levantamento de custos",
                "orçamento detalhado",
                "estrutura de custos"
              ],
              contexto_obrigatorio: [
                "memória de cálculo", 
                "plano de aplicação", 
                "desembolso",
                "justificativa de gastos",
                "cronograma financeiro",
                "rubricas",
                "fontes de recurso",
                "contrapartida",
                "valor global",
                "custo total",
                "detalhamento de despesas",
                "natureza da despesa"
              ],
              peso_relevancia: 1.5
            },
            {
              termo_principal: "auxílio financeiro",
              sinonimos: [
                "bolsa de extensão",
                "bolsa estudantil",
                "auxílio ao extensionista",
                "recurso para custeio",
                "fomento",
                "financiamento",
                "apoio financeiro"
              ],
              contexto_obrigatorio: [
                "edital de fomento",
                "termo de compromisso do bolsista",
                "plano de trabalho do bolsista",
                "frequência do bolsista"
              ],
              peso_relevancia: 1.4
            }
          ]
        },
        {
          id: "PROC_INFRA",
          name: "Infraestrutura e Logística",
          concepts: [
            {
              termo_principal: "infraestrutura disponível",
              sinonimos: [
                "recursos materiais",
                "espaço físico",
                "equipamentos",
                "instalações",
                "recursos audiovisuais",
                "laboratórios"
              ],
              contexto_obrigatorio: [
                "disponibilidade",
                "adequação",
                "acessibilidade",
                "capacidade de atendimento",
                "viabilidade técnica"
              ],
              peso_relevancia: 1.4
            }
          ]
        }
      ]
    },
    {
      id: "P6",
      name: "Conformidade Documental",
      definition: "Verificação da completude e validade dos documentos obrigatórios.",
      regra: "Editais PREX (Anexos e Formulários)",
      processes: [
        {
          id: "PROC_DOC",
          name: "Documentação Obrigatória",
          concepts: [
            {
              termo_principal: "declaração de apoio",
              sinonimos: [
                "termo de aceite",
                "apoio institucional",
                "declaração da direção-geral",
                "carta de anuência do campus",
                "autorização institucional",
                "assinatura direção-geral",
                "aval do campus",
                "concordância da direção"
              ],
              contexto_obrigatorio: [
                "anexo i",
                "formulário assinado",
                "documento digitalizado",
                "assinatura eletrônica",
                "carimbo institucional",
                "papel timbrado"
              ],
              peso_relevancia: 1.9
            },
            {
              termo_principal: "termo de compromisso",
              sinonimos: [
                "declaração de anuência",
                "anuência da chefia",
                "termo de responsabilidade",
                "compromisso do extensionista",
                "termo de parceria",
                "carta de compromisso"
              ],
              contexto_obrigatorio: [
                "assinatura",
                "identificação do servidor",
                "carga horária dedicada",
                "período de vigência",
                "atribuições definidas"
              ],
              peso_relevancia: 1.8
            }
          ]
        }
      ]
    }
  ]
};