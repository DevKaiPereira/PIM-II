const bibliotecaTermosBackup = {
  "pillars": [
    {
      "id": "P1",
      "name": "Admissibilidade e Vínculo",
      "definition": "Validação da legitimidade do proponente e sua situação funcional perante o IFB.",
      "regra": "PREX 42/2020 Art. 15 e Editais Vigentes",
      "processes": [
        {
          "id": "PROC1",
          "name": "Vínculo Permanente",
          "concepts": [
            {
              "termo_principal": "proponente",
              "sinonimos": [
                "autor",
                "coordenador-geral",
                "servidor proponente",
                "coordenador da proposta",
                "responsável pelo projeto",
                "propositor",
                "coordenador titular",
                "requerente"
              ],
              "contexto_obrigatorio": [
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
              "contexto_negacao": [
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
              "peso_relevancia": 2.0
            },
            {
              "termo_principal": "exercício pleno",
              "sinonimos": [
                "pleno exercício",
                "assiduidade",
                "em exercício",
                "exercício ativo",
                "atividade presencial",
                "frequência regular",
                "disponibilidade integral",
                "carga horária compatível",
                "sem restrições funcionais",
                "aptidão para coordenar",
                "servidor ativo",
                "docente efetivo",
                "professor efetivo",
                "técnico administrativo",
                "em atividade",
                "lotado no campus",
                "quadro permanente",
                "instituto federal de brasilia",
                "ifb",
                "cnpj 10.724.560",
                "servidor concursado",
                "servidor de carreira",
                "servidor do quadro",
                "servidor estável",
                "efetivo no cargo",
                "titular do cargo",
                "ocupante de cargo efetivo",
                "funcionário de carreira",
                "servidor vitalício",
                "agente público efetivo",
                "corpo funcional permanente",
                "força de trabalho institucional",
                "no desempenho da função",
                "em plena atividade",
                "em efetivo exercício",
                "na ativa",
                "servindo à instituição",
                "lotação definitiva",
                "sede funcional",
                "unidade de exercício",
                "designação funcional",
                "alocado no órgão",
                "quadro de pessoal",
                "corpo de servidores",
                "plantel efetivo",
                "estabilidade funcional",
                "vínculo efetivo",
                "regime estatutário",
                "servidor estatutário",
                "servidor público federal",
                "agente da administração pública",
                "funcionário público",
                "serventuário",
                "agente estatal",
                "servidor estatal"
              ],
              "contexto_obrigatorio": [
                "não afastado",
                "sem licença",
                "disponível",
                "sem impedimentos",
                "comparecimento regular",
                "carga horária preservada",
                "sem restrições médicas",
                "sem afastamentos legais",
                "nomeação publicada em diário oficial",
                "termo de posse assinado",
                "portaria de lotação",
                "ato de designação",
                "frequência regular",
                "assiduidade comprovada",
                "comparecimento integral",
                "jornada de trabalho cumprida",
                "registro funcional ativo",
                "cadastro atualizado no siape",
                "ficha funcional sem pendências",
                "avaliação de desempenho em dia",
                "estágio probatório concluído"
              ],
              "contexto_negacao": [
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
                "licença gestante",
                "exonerado",
                "aposentado",
                "redistribuído",
                "outra instituição",
                "instituição parceira exclusiva",
                "sem vínculo",
                "contrato temporário",
                "professor substituto",
                "docente substituto",
                "servidor temporário",
                "cargo em comissão exclusivo",
                "requisitado",
                "licença paternidade",
                "licença por motivo de doença em pessoa da família",
                "afastamento para estudo no exterior",
                "suspensão disciplinar",
                "disponibilidade",
                "aposentadoria compulsória",
                "demissão",
                "vacância",
                "desligamento",
                "rescisão contratual",
                "término de mandato",
                "fim de designação",
                "reintegração pendente",
                "readaptação provisória",
                "remoção não autorizada",
                "transferência externa",
                "colaboração técnica",
                "visitante",
                "prestador de serviço",
                "terceirizado",
                "estagiário",
                "bolsista externo",
                "voluntário não institucional"
              ],
              "peso_relevancia": 1.8
            },
            {
              "termo_principal": "categoria funcional",
              "sinonimos": [
                "carreira",
                "cargo",
                "função",
                "enquadramento",
                "classe funcional",
                "nível de classificação"
              ],
              "contexto_obrigatorio": [
                "docente",
                "técnico-administrativo",
                "professor",
                "servidor público federal"
              ],
              "contexto_negacao": [
                "terceirizado",
                "voluntário",
                "colaborador externo",
                "sem vínculo"
              ],
              "peso_relevancia": 1.5
            }
          ]
        },
        {
          "id": "PROC_ADIM",
          "name": "Status de Adimplência",
          "concepts": [
            {
              "termo_principal": "nada consta",
              "sinonimos": [
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
              "contexto_obrigatorio": [
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
              "contexto_negacao": [
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
              "peso_relevancia": 2.0
            }
          ]
        }
      ]
    },
    {
      "id": "P2",
      "name": "Pilar 2 — Configuração de Equipe",
      "definition": "Regras de composição da força de trabalho e protagonismo discente.",
      "regra": "PREX 42/2020 Art. 19 e 20",
      "processes": [
        {
          "id": "PROC_DISC",
          "name": "Participação Discente",
          "concepts": [
            {
              "termo_principal": "estudante",
              "sinonimos": [
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
                "aprendiz",
                "escolar",
                "acadêmico",
                "matriculado",
                "cursista",
                "educando formal",
                "aluno de nível médio",
                "aluno de graduação",
                "estagiário acadêmico",
                "bolsista de extensão",
                "voluntário acadêmico",
                "participante discente",
                "integrante discente",
                "membro estudantil",
                "discente colaborador",
                "aprendente"
              ],
              "contexto_obrigatorio": [
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
                "coeficiente de rendimento",
                "vínculo institucional",
                "registro acadêmico ativo",
                "situação regular no SISTEC",
                "componente curricular em andamento",
                "carga horária compatível",
                "termo de compromisso do bolsista",
                "plano de trabalho do bolsista",
                "orientação acadêmica",
                "tutor responsável",
                "inscrição no módulo de extensão"
              ],
              "contexto_negacao": [
                "egresso",
                "ex-aluno",
                "desistente",
                "matrícula trancada",
                "desligado",
                "transferido",
                "jubilado",
                "desvinculado",
                "concluinte",
                "formado",
                "desistente formal",
                "abandono de curso",
                "cancelamento de matrícula",
                "desligamento acadêmico",
                "inativo no sistema",
                "sem vínculo com a instituição"
              ],
              "peso_relevancia": 1.9
            },
            {
              "termo_principal": "protagonismo estudantil",
              "sinonimos": [
                "participação ativa",
                "liderança discente",
                "autonomia estudantil",
                "envolvimento discente",
                "protagonismo juvenil",
                "empoderamento estudantil",
                "protagonismo acadêmico",
                "agência discente",
                "voz do estudante",
                "ativismo estudantil",
                "corresponsabilidade discente",
                "gestão compartilhada com discentes",
                "autoria discente",
                "iniciativa estudantil",
                "engajamento discente",
                "participação protagonista",
                "liderança juvenil",
                "jovem protagonista"
              ],
              "contexto_obrigatorio": [
                "tomada de decisão",
                "planejamento participativo",
                "execução compartilhada",
                "avaliação coletiva",
                "construção conjunta",
                "reuniões de equipe com voz ativa",
                "proposição de atividades",
                "relatoria discente",
                "apresentação em eventos",
                "mediação de oficinas",
                "elaboração de materiais",
                "coordenação de grupos de trabalho",
                "representação discente",
                "autoavaliação",
                "feedback bidirecional"
              ],
              "peso_relevancia": 1.7
            }
          ]
        },
        {
          "id": "PROC_ORIENT",
          "name": "Orientação Técnica",
          "concepts": [
            {
              "termo_principal": "orientação docente",
              "sinonimos": [
                "docente orientador",
                "professor orientador",
                "supervisão",
                "tutoria acadêmica",
                "orientação pedagógica",
                "acompanhamento docente",
                "mentoria",
                "orientador responsável",
                "professor supervisor",
                "orientador técnico",
                "supervisão acadêmica",
                "tutoria educacional",
                "guia acadêmico",
                "mestre orientador",
                "coordenador pedagógico",
                "instrutor supervisor",
                "docente tutor",
                "professor conselheiro",
                "facilitador pedagógico"
              ],
              "contexto_obrigatorio": [
                "obrigatório",
                "técnico-administrativo",
                "bolsistas",
                "supervisão obrigatória",
                "acompanhamento pedagógico",
                "orientação de projetos",
                "coordenação compartilhada",
                "equipe multidisciplinar",
                "formação complementar",
                "aprendizagem supervisionada",
                "plano de orientação definido",
                "horários de atendimento",
                "relatório de acompanhamento",
                "avaliação do bolsista",
                "termo de orientação assinado",
                "vínculo orientador-orientando",
                "reuniões periódicas de supervisão"
              ],
              "peso_relevancia": 1.8
            },
            {
              "termo_principal": "equipe executora",
              "sinonimos": [
                "membros da equipe",
                "colaboradores",
                "participantes",
                "integrantes",
                "força de trabalho",
                "recursos humanos",
                "equipe do projeto",
                "grupo de trabalho",
                "núcleo executivo",
                "corpo de execução",
                "staff do projeto",
                "quadro de colaboradores",
                "time de extensão",
                "comissão de execução",
                "braço operacional",
                "grupo executor",
                "plantel de execução",
                "equipe de campo"
              ],
              "contexto_obrigatorio": [
                "multidisciplinar",
                "interdisciplinar",
                "complementar",
                "diversidade de formação",
                "atribuições definidas",
                "carga horária dedicada",
                "termos de compromisso individuais",
                "composição equilibrada",
                "participação de diferentes setores",
                "colaboração entre áreas"
              ],
              "peso_relevancia": 1.4
            }
          ]
        },
        {
          "id": "PROC_COORD",
          "name": "Estrutura de Coordenação",
          "concepts": [
            {
              "termo_principal": "coordenador único",
              "sinonimos": [
                "coordenação singular",
                "líder do projeto",
                "gestor responsável",
                "coordenador exclusivo",
                "titular da coordenação",
                "coordenador-geral",
                "coordenador principal",
                "gestor da ação",
                "responsável geral",
                "coordenador proponente",
                "cabeça da equipe",
                "chefe do projeto"
              ],
              "contexto_obrigatorio": [
                "único",
                "exclusivo",
                "individual",
                "centralizado",
                "sem co-coordenador",
                "designação formal",
                "portaria de coordenação",
                "única assinatura de responsável",
                "apenas um coordenador listado"
              ],
              "contexto_negacao": [
                "co-coordenador",
                "coordenação compartilhada",
                "dupla coordenação",
                "coordenadores múltiplos",
                "coordenação colegiada",
                "mais de um coordenador",
                "coordenador adjunto",
                "vice-coordenador",
                "coordenador substituto",
                "coordenação dual",
                "bicefalia de coordenação",
                "direção compartilhada",
                "gestão compartilhada da coordenação"
              ],
              "peso_relevancia": 1.6
            }
          ]
        }
      ]
    },
    {
  "id": "P3",
  "name": "Dimensão Pedagógica",
  "definition": "Integração das funções finalísticas e impacto social.",
  "regra": "PREX 42/2020 Art. 4 e 5",
  "processes": [
    {
      "id": "PROC_INDISS",
      "name": "Indissociabilidade",
      "concepts": [
        {
          "termo_principal": "indissociabilidade",
          "sinonimos": [
            "articulação ensino-pesquisa",
            "interdisciplinaridade",
            "formação integral",
            "integração acadêmica",
            "tripé universitário",
            "articulação teórico-prática",
            "convergência formativa",
            "integração ensino-extensão-pesquisa",
            "formação holística",
            "educação integrada",
            "inseparabilidade ensino-extensão",
            "simbiose acadêmica",
            "unidade teoria-prática",
            "articulação pesquisa-extensão",
            "prática pedagógica integrada",
            "aprendizagem significativa contextualizada",
            "currículo integrado",
            "formação omnilateral",
            "politecnia",
            "práxis educativa",
            "ação-reflexão-ação",
            "ensino com pesquisa",
            "extensão como princípio educativo"
          ],
          "contexto_obrigatorio": [
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
            "produção tecnológica",
            "protagonismo estudantil",
            "problematização da realidade",
            "intervenção social",
            "produção de conhecimento",
            "socialização de saberes",
            "diálogo entre disciplinas",
            "flexibilização curricular",
            "projetos integradores",
            "iniciação científica",
            "iniciação tecnológica"
          ],
          "contexto_negacao": [
            "atividade puramente assistencialista",
            "ação desvinculada do currículo",
            "prática sem reflexão teórica",
            "ensino bancário",
            "dissociação entre teoria e prática",
            "extensão isolada do ensino",
            "projeto sem fundamentação acadêmica"
          ],
          "peso_relevancia": 1.8
        },
        {
          "termo_principal": "interdisciplinaridade",
          "sinonimos": [
            "multidisciplinar",
            "transdisciplinar",
            "diálogo de saberes",
            "integração disciplinar",
            "convergência de áreas",
            "abordagem integrada",
            "pluridisciplinaridade",
            "interprofissionalidade",
            "interface disciplinar",
            "síntese de conhecimentos",
            "cooperação entre disciplinas",
            "entrelaçamento de conteúdos",
            "articulação de áreas"
          ],
          "contexto_obrigatorio": [
            "diferentes áreas",
            "múltiplos conhecimentos",
            "saberes diversos",
            "integração curricular",
            "equipe multidisciplinar",
            "colaboração entre departamentos",
            "diversidade epistemológica",
            "complexidade",
            "visão sistêmica",
            "pensamento complexo",
            "ecologia de saberes"
          ],
          "peso_relevancia": 1.6
        }
      ]
    },
    {
      "id": "PROC_EXT",
      "name": "Interação Dialógica",
      "concepts": [
        {
          "termo_principal": "público-alvo",
          "sinonimos": [
            "comunidade externa",
            "beneficiários",
            "público misto",
            "população atendida",
            "público beneficiário",
            "comunidade participante",
            "segmento social",
            "grupo focal",
            "destinatários",
            "atores sociais",
            "parceiros comunitários",
            "sujeitos da ação",
            "coletividade",
            "grupos sociais",
            "movimentos sociais",
            "organizações da sociedade civil",
            "escolas públicas",
            "comunidades tradicionais",
            "populações vulneráveis"
          ],
          "contexto_obrigatorio": [
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
            "protagonismo comunitário",
            "emancipação",
            "autonomia",
            "escuta ativa",
            "construção coletiva",
            "relação dialógica",
            "horizontalidade",
            "troca de saberes",
            "mão dupla",
            "interação",
            "comunicação bidirecional"
          ],
          "contexto_negacao": [
            "somente servidores",
            "comunidade interna exclusiva",
            "restrito ao campus",
            "apenas alunos",
            "público interno",
            "exclusivamente IFB",
            "ação unidirecional",
            "assistencialismo",
            "imposição de saberes",
            "extensão difusionista",
            "ausência de diálogo"
          ],
          "peso_relevancia": 1.7
        },
        {
          "termo_principal": "impacto social",
          "sinonimos": [
            "relevância social",
            "alcance comunitário",
            "benefício público",
            "retorno à sociedade",
            "transformação comunitária",
            "engajamento social",
            "efeito social",
            "resultados sociais",
            "melhoria social",
            "contribuição social",
            "valor público gerado",
            "externalidade positiva"
          ],
          "contexto_obrigatorio": [
            "resultados mensuráveis",
            "indicadores sociais",
            "mudança social",
            "desenvolvimento local",
            "melhoria da qualidade de vida",
            "inclusão produtiva",
            "geração de renda",
            "acesso a direitos",
            "fortalecimento de vínculos",
            "resiliência comunitária",
            "sustentabilidade",
            "ODS",
            "Objetivos de Desenvolvimento Sustentável"
          ],
          "peso_relevancia": 1.7
        }
      ]
    },
    {
      "id": "PROC_AVAL",
      "name": "Avaliação e Aprendizagem",
      "concepts": [
        {
          "termo_principal": "avaliação formativa",
          "sinonimos": [
            "avaliação contínua",
            "feedback processual",
            "avaliação dialógica",
            "monitoramento",
            "acompanhamento avaliativo",
            "avaliação qualitativa",
            "avaliação participativa",
            "avaliação emancipatória",
            "avaliação para aprendizagem",
            "retroalimentação",
            "devolutiva"
          ],
          "contexto_obrigatorio": [
            "processo ensino-aprendizagem",
            "desenvolvimento de competências",
            "reflexão crítica",
            "autoavaliação",
            "metacognição",
            "critérios transparentes",
            "registro de aprendizagens",
            "portfólio",
            "autoavaliação discente",
            "avaliação entre pares",
            "diário de bordo",
            "relatos de experiência"
          ],
          "peso_relevancia": 1.5
        }
      ]
    }
  ]
},
    {
  "id": "P4",
  "name": "Enquadramento Estratégico",
  "definition": "Classificação temática e tipológica da ação.",
  "regra": "PREX 42/2020 Art. 8 (Áreas Temáticas)",
  "processes": [
    {
      "id": "PROC_TEMA",
      "name": "Áreas Temáticas",
      "concepts": [
        {
          "termo_principal": "áreas de extensão",
          "sinonimos": [
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
            "campos temáticos",
            "área do conhecimento",
            "eixo articulador",
            "núcleo temático",
            "vertente extensionista",
            "domínio da extensão"
          ],
          "contexto_obrigatorio": [
            "vinculação",
            "área prioritária",
            "pdi",
            "plano de desenvolvimento institucional",
            "convergência institucional",
            "alinhamento estratégico",
            "política de extensão",
            "missão institucional",
            "objetivos estratégicos",
            "consonância temática",
            "aderência ao edital",
            "perfil institucional",
            "identidade institucional",
            "diretrizes da extensão",
            "política nacional de extensão"
          ],
          "peso_relevancia": 1.5
        },
        {
          "termo_principal": "abrangência territorial",
          "sinonimos": [
            "alcance geográfico",
            "cobertura territorial",
            "local de realização",
            "área de abrangência",
            "localização estratégica",
            "escala territorial",
            "raio de ação",
            "extensão geográfica",
            "circunscrição",
            "área de influência"
          ],
          "contexto_obrigatorio": [
            "local",
            "regional",
            "nacional",
            "internacional",
            "território de abrangência",
            "municípios atendidos",
            "estados participantes",
            "parceria interinstitucional",
            "abrangência justificada"
          ],
          "peso_relevancia": 1.4
        }
      ]
    },
    {
      "id": "PROC_TIPO",
      "name": "Tipologia da Ação",
      "concepts": [
        {
          "termo_principal": "classificação",
          "sinonimos": [
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
            "tipologia extensionista",
            "espécie de ação",
            "gênero da atividade",
            "categoria SUAP",
            "tipo de registro"
          ],
          "contexto_obrigatorio": [
            "modalidade",
            "suap",
            "natureza",
            "eixos de trabalho",
            "módulo de extensão",
            "classificação sistêmica",
            "categoria no sistema",
            "registro acadêmico",
            "certificação",
            "carga horária total",
            "público estimado",
            "número de vagas"
          ],
          "peso_relevancia": 1.6
        },
        {
          "termo_principal": "modalidade específica",
          "sinonimos": [
            "oficina",
            "minicurso",
            "palestra",
            "workshop",
            "seminário",
            "congresso",
            "feira",
            "exposição",
            "apresentação cultural",
            "intervenção artística",
            "ação comunitária",
            "mutirão",
            "campanha educativa",
            "curso de atualização",
            "curso de formação inicial e continuada",
            "FIC",
            "curso de qualificação profissional",
            "evento científico",
            "jornada",
            "simpósio",
            "colóquio",
            "mesa-redonda",
            "debate público",
            "sarau",
            "festival",
            "mostra",
            "concerto",
            "espetáculo",
            "performance",
            "intervenção urbana"
          ],
          "contexto_obrigatorio": [
            "carga horária",
            "público previsto",
            "metodologia específica",
            "programação detalhada",
            "local de realização",
            "periodicidade",
            "número de encontros"
          ],
          "peso_relevancia": 1.3
        }
      ]
    }
  ]
},
    {
  "id": "P5",
  "name": "Recursos e Viabilidade",
  "definition": "Governança financeira e infraestrutura de execução.",
  "regra": "PREX 42/2020 Art. 29 (VIII, IX e X)",
  "processes": [
    {
      "id": "PROC_FIN",
      "name": "Planejamento Financeiro",
      "concepts": [
        {
          "termo_principal": "orçamento",
          "sinonimos": [
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
            "estrutura de custos",
            "estimativa de despesas",
            "projeção orçamentária",
            "custeio",
            "capital",
            "investimento",
            "rateio de despesas",
            "planilha de custos"
          ],
          "contexto_obrigatorio": [
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
            "natureza da despesa",
            "classificação orçamentária",
            "elemento de despesa",
            "valor unitário",
            "quantidade",
            "periodicidade do desembolso"
          ],
          "peso_relevancia": 1.5
        },
        {
          "termo_principal": "auxílio financeiro",
          "sinonimos": [
            "bolsa de extensão",
            "bolsa estudantil",
            "auxílio ao extensionista",
            "recurso para custeio",
            "fomento",
            "financiamento",
            "apoio financeiro",
            "concessão de bolsas",
            "auxílio financeiro a pesquisador",
            "auxílio ao discente",
            "auxílio-transporte",
            "auxílio-alimentação"
          ],
          "contexto_obrigatorio": [
            "edital de fomento",
            "termo de compromisso do bolsista",
            "plano de trabalho do bolsista",
            "frequência do bolsista",
            "valor da bolsa",
            "vigência",
            "carga horária do bolsista",
            "orientador responsável",
            "relatório de atividades do bolsista"
          ],
          "peso_relevancia": 1.4
        }
      ]
    },
    {
      "id": "PROC_INFRA",
      "name": "Infraestrutura e Logística",
      "concepts": [
        {
          "termo_principal": "infraestrutura disponível",
          "sinonimos": [
            "recursos materiais",
            "espaço físico",
            "equipamentos",
            "instalações",
            "recursos audiovisuais",
            "laboratórios",
            "salas de aula",
            "auditório",
            "biblioteca",
            "recursos de TI",
            "conectividade",
            "transporte",
            "logística",
            "insumos",
            "materiais de consumo",
            "equipamentos de proteção",
            "mobiliário",
            "veículos oficiais"
          ],
          "contexto_obrigatorio": [
            "disponibilidade",
            "adequação",
            "acessibilidade",
            "capacidade de atendimento",
            "viabilidade técnica",
            "autorização de uso",
            "reserva de espaço",
            "compatibilidade com a ação",
            "condições de segurança",
            "plano de contingência"
          ],
          "peso_relevancia": 1.4
        }
      ]
    }
  ]
},
    {
  "id": "P6",
  "name": "Conformidade Documental",
  "definition": "Verificação da completude e validade dos documentos obrigatórios.",
  "regra": "Editais PREX (Anexos e Formulários)",
  "processes": [
    {
      "id": "PROC_DOC",
      "name": "Documentação Obrigatória",
      "concepts": [
        {
          "termo_principal": "declaração de apoio",
          "sinonimos": [
            "termo de aceite",
            "apoio institucional",
            "declaração da direção-geral",
            "carta de anuência do campus",
            "autorização institucional",
            "assinatura direção-geral",
            "aval do campus",
            "concordância da direção",
            "declaração de ciência",
            "manifestação favorável",
            "aprovação da unidade",
            "autorização da direção"
          ],
          "contexto_obrigatorio": [
            "anexo i",
            "formulário assinado",
            "documento digitalizado",
            "assinatura eletrônica",
            "carimbo institucional",
            "papel timbrado",
            "data da assinatura",
            "identificação do signatário",
            "cargo do signatário",
            "validade do documento"
          ],
          "peso_relevancia": 1.9
        },
        {
          "termo_principal": "termo de compromisso",
          "sinonimos": [
            "declaração de anuência",
            "anuência da chefia",
            "termo de responsabilidade",
            "compromisso do extensionista",
            "termo de parceria",
            "carta de compromisso",
            "acordo de cooperação",
            "convênio",
            "protocolo de intenções",
            "contrato de parceria",
            "termo de adesão"
          ],
          "contexto_obrigatorio": [
            "assinatura",
            "identificação do servidor",
            "carga horária dedicada",
            "período de vigência",
            "atribuições definidas",
            "cláusulas de responsabilidade",
            "direitos e deveres",
            "prazo de vigência",
            "renovação automática",
            "rescisão"
          ],
          "peso_relevancia": 1.8
        },
        {
          "termo_principal": "documentação complementar",
          "sinonimos": [
            "anexos obrigatórios",
            "documentos exigidos",
            "comprovantes",
            "formulários suplementares",
            "declarações adicionais",
            "documentos comprobatórios",
            "peças documentais",
            "dossiê completo"
          ],
          "contexto_obrigatorio": [
            "currículo do proponente",
            "currículo lattes",
            "certidão de nada consta",
            "declaração de adimplência",
            "planilha orçamentária",
            "cronograma",
            "plano de trabalho",
            "projeto detalhado",
            "carta de apresentação",
            "formulário de inscrição",
            "comprovante de submissão",
            "recibo de entrega"
          ],
          "peso_relevancia": 1.7
        }
      ]
    }
  ]
};

module.exports = bibliotecaTermosBackup;