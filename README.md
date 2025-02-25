# Chaos-Dota
Bot de Comparação de Estatísticas de Jogadores do Dota 2

Este é um bot que coleta e compara estatísticas de jogadores do Dota 2 usando dados da Steam. Ele identifica o persona name (nome no Dota 2) de um ou mais jogadores, coleta suas estatísticas e as compara para fornecer insights sobre o desempenho de cada um.
Funcionalidades

    Coleta de Dados da Steam:

        O bot acessa a API da Steam para obter informações sobre os jogadores.

        Identifica o persona name de cada jogador com base no ID da Steam.

    Comparação de Estatísticas:

        Compara estatísticas como:

            Taxa de vitórias (win rate).

            Nível de habilidade (MMR).

            Heróis mais jogados.

            KDA (Kills, Deaths, Assists).

            Partidas recentes.

        Gera um relatório comparativo entre dois ou mais jogadores.

    Saída de Dados:

        Exibe os resultados em formato de texto ou tabela.

        Pode ser integrado a um chat (ex: Discord, Telegram) para envio automático dos resultados.

Como Usar
Pré-requisitos

    API Key da Steam: Você precisa de uma chave de API da Steam para acessar os dados. Obtenha uma aqui.

    Python 3.x: O bot foi desenvolvido em Python.

    Bibliotecas Necessárias:
    bash
    Copy

    pip install requests
    pip install pandas

Configuração

    Clone o repositório:
    bash
    Copy

    git clone https://github.com/seu-usuario/nome-do-repositorio.git

    Adicione sua API Key da Steam no arquivo de configuração:
    python
    Copy

    STEAM_API_KEY = "sua_api_key_aqui"

    Execute o bot:
    bash
    Copy

    python main.py

Exemplo de Uso
python
Copy

from bot import Dota2StatsBot

# IDs da Steam dos jogadores
player1_id = "123456789"
player2_id = "987654321"

# Inicializa o bot
bot = Dota2StatsBot(STEAM_API_KEY)

# Coleta e compara estatísticas
comparison = bot.compare_players(player1_id, player2_id)
print(comparison)

Estrutura do Projeto
Copy

.
├── README.md
├── main.py                # Script principal
├── bot.py                 # Lógica do bot
├── requirements.txt       # Dependências
└── config.py              # Configurações (ex: API Key)

Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:

    Faça um fork do projeto.

    Crie uma branch para sua feature (git checkout -b feature/nova-feature).

    Commit suas mudanças (git commit -m 'Adiciona nova feature').

    Push para a branch (git push origin feature/nova-feature).

    Abra um Pull Request.

Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.
