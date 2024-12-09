def obter_recomendacao(uso, desempenho, custo, energia):
    processadores = [
        {
            "modelo": "AMD Ryzen 9 7950X",
            "uso": "Jogos",
            "desempenho": "Alto",
            "custo": "Alto",
            "energia": "Alto",
            "arquitetura": "CISC",
            "cache": "L1 de 64KB, L2 de 1MB, L3 de 64MB",
            "frequencia": "4.5GHz (Turbo 5.7GHz)",
            "justificativa": "O ápice de desempenho para jogos, excelente para rodar em altas resoluções."
        },
        
        {
            "modelo": "AMD Ryzen 7 7700X",
            "uso": "Jogos",
            "desempenho": "Alto",
            "custo": "Intermediário",
            "energia": "Médio",
            "arquitetura": "CISC",
            "cache": "L1 de 64KB, L2 de 1MB, L3 de 32MB",
            "frequencia": "4.5GHz (Turbo 5.4GHz)",
            "justificativa": "Alto desempenho para todos os jogos e com um preço razoável."
        },

        {
            "modelo": "AMD Ryzen 5 4500",
            "uso": "Jogos",
            "desempenho": "Médio",
            "custo": "Intermediário",
            "energia": "Médio",
            "arquitetura": "CISC",
            "cache": "L1 de 64KB, L2 de 512KB, L3 de 8MB",
            "frequencia": "3.6GHz (Turbo 4.1GHz)",
            "justificativa": "Desempenho razoável para jogos de última geração."
        },

        {
            "modelo": "AMD Ryzen 3 3200G",
            "uso": "Jogos",
            "desempenho": "Baixo",
            "custo": "Econômico",
            "energia": "Baixo",
            "arquitetura": "CISC",
            "cache": "L1 de 96KB, L2 de 512KB, L3 de 4MB",
            "frequencia": "3.6GHz (Turbo 4GHz)",
            "justificativa": "Um processador de orçamento acessível, rodará bem jogos menos exigentes."
        },

        {
            "modelo": "Intel Core i9-13900KS",
            "uso": "Edição de Vídeo",
            "desempenho": "Alto",
            "custo": "Alto",
            "energia": "Alto",
            "arquitetura": "CISC",
            "cache": "L1 de 80KB, L2 de 2MB, L3 de 36MB",
            "frequencia": "3.2GHz (Turbo 6GHz)",
            "justificativa": "Excelente para edição de vídeos de alta resolução e com renderização rápida."
        },

        {
            "modelo": "AMD Ryzen 7 7700X",
            "uso": "Edição de Vídeo",
            "desempenho": "Médio",
            "custo": "Intermediário",
            "energia": "Médio",
            "arquitetura": "CISC",
            "cache": "L1 de 64KB, L2 de 1MB, L3 de 32MB",
            "frequencia": "4.5GHz (Turbo 5.4GHz)",
            "justificativa": "Ideal para edição em 1080p/4K com tempos de exportação decentes."
        },

        {
            "modelo": "Intel Core i5-13400",
            "uso": "Edição de Vídeo",
            "desempenho": "Baixo",
            "custo": "Econômico",
            "energia": "Baixo",
            "arquitetura": "CISC",
            "cache": "L1 de 80KB, L2 de 1.25MB, L3 de 20MB",
            "frequencia": "2.5GHz (Turbo 4.6GHz)",
            "justificativa": "Atende edições mais simples e projetos menores."
        },

        {
            "modelo": "AMD Ryzen Threadripper PRO 5975WX",
            "uso": "IA",
            "desempenho": "Alto",
            "custo": "Alto",
            "energia": "Alto",
            "arquitetura": "CISC",
            "cache": "L1 de 64KB, L2 de 512KB, L3 de 128MB",
            "frequencia": "3.6GHz (Turbo 4.5GHz)",
            "justificativa": "Projetado para cargas de trabalho massivas e treinamento de modelos grande."
        },

        {
            "modelo": "Intel Core i7-13700KF",
            "uso": "IA",
            "desempenho": "Médio",
            "custo": "Intermediário",
            "energia": "Médio",
            "arquitetura": "CISC",
            "cache": "L1 de 80KB, L2 de 2MB, L3 de 30MB",
            "frequencia": "3.4GHz (Turbo 5.4GHz)",
            "justificativa": "Bom para treinamentos menores e inferência em tempo real."
        },

        {
            "modelo": "AMD Ryzen 5 5600G",
            "uso": "IA",
            "desempenho": "Baixo",
            "custo": "Econômico",
            "energia": "Baixo",
            "arquitetura": "CISC",
            "cache": "L1 de 64KB, L2 de 512KB, L3 de 16MB",
            "frequencia": "3.9GHz (Turbo 4.4GHz)",
            "justificativa": "Para aplicações mais leves e inferência básica."
        },

        {
            "modelo": "AMD Ryzen 7 7840U",
            "uso": "IoT",
            "desempenho": "Alto",
            "custo": "Alto",
            "energia": "Alto",
            "arquitetura": "CISC",
            "cache": "L1 de 64KB, L2 de 1MB, L3 de 16MB",
            "frequencia": "3.3GHz (Turbo 5.1GHz)",
            "justificativa": "Perfeito para aplicações complexas e desenvolvimento robusto em IoT."
        },

        {
            "modelo": "Intel Core i5-1335U",
            "uso": "IoT",
            "desempenho": "Médio",
            "custo": "Intermediário",
            "energia": "Médio",
            "arquitetura": "CISC",
            "cache": "L1 de 80KB, L2 de 1.25MB, L3 de 12MB",
            "frequencia": "1.3GHz (Turbo 4.6GHz)",
            "justificativa": "Bom para projetos de IoT intermediários e testes."
        },

        {
            "modelo": "Raspberry Pi 4 Model B (SoC Broadcom)",
            "uso": "IoT",
            "desempenho": "Baixo",
            "custo": "Econômico",
            "energia": "Baixo",
            "arquitetura": "RISC",
            "cache": "L1 de 48KB, L2 de 1MB, L3 de 0",
            "frequencia": "1.5GHz (Turbo 2GHz)",
            "justificativa": "Excelente para protótipos e dispositivos IoT com baixo consumo de energia."
        }
    ]
    
    # Recomendação por pontos
    melhor_proc = None
    maior_pontuacao = -1

    for proc in processadores:
        pontuacao = 0
        if proc["uso"] == uso:
            pontuacao += 5
        if proc["desempenho"] == desempenho:
            pontuacao += 2
        if proc["custo"] == custo:
            pontuacao += 3
        if proc["energia"] == energia:
            pontuacao += 1

        if pontuacao > maior_pontuacao:
            maior_pontuacao = pontuacao
            melhor_proc = proc

    return melhor_proc if melhor_proc else {
        "modelo": "Não encontrado",
        "arquitetura": "N/A",
        "cache": "N/A",
        "frequencia": "N/A",
        "justificativa": "Nenhum processador foi encontrado."
    }
