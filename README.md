Dota 2 Player Statistics Comparison Bot

This is a Discord bot that collects and compares Dota 2 player statistics using the OpenDota API. It allows you to search for a player's persona name (in-game name), display their information, and compare statistics between two players.
Features:

    Player Search:

        The bot searches for players by their persona name using the OpenDota API.

        Displays information such as persona name and Steam profile URL.

    Player Comparison:

        Compares two players, displaying their information side by side.

        Can be expanded in the future to include detailed statistics like win rate, KDA, etc.

    Useful Commands:

        .ping: Checks the bot's latency.

        .status: Checks if Dota 2 servers are online.

        .player <name>: Searches for a player by name and displays their information.

        .compare <player1> <player2>: Compares two players.

        .helpme: Displays a list of available commands.

How to Use
Prerequisites

    Python 3.x: The bot is developed in Python.

    Required Libraries:
    bash
    Copy

    pip install discord.py python-dotenv requests

    Discord Bot Token: Create a bot on the Discord Developer Portal and obtain the token.

    OpenDota API: The bot uses the public OpenDota API, which does not require an authentication key.

Setup

    Clone the repository:
    bash
    Copy

    git clone https://github.com/your-username/repository-name.git

    Create a .env file in the root of the project and add the bot token:
    env
    Copy

    DISCORD_TOKEN=your_token_here

    Run the bot:
    bash
    Copy

    python main.py

Bot Commands

    .ping: Checks the bot's latency.
    Copy

    .ping

    .status: Checks the status of Dota 2 servers.
    Copy

    .status

    .player <name>: Searches for a player by name.
    Copy

    .player "PlayerName"

    .compare <player1> <player2>: Compares two players.
    Copy

    .compare "Player1" "Player2"

    .helpme: Displays the list of available commands.
    Copy

    .helpme

Example Usage

    Add the bot to your Discord server.

    Use the commands in the server chat:

        To search for a player:
        Copy

        .player "PlayerName"

        To compare two players:
        Copy

        .compare "Player1" "Player2"

Contributing

Contributions are welcome! Follow these steps:

    Fork the project.

    Create a branch for your feature (git checkout -b feature/new-feature).

    Commit your changes (git commit -m 'Add new feature').

    Push to the branch (git push origin feature/new-feature).

    Open a Pull Request.

License

This project is licensed under the MIT License. See the LICENSE file for details.
