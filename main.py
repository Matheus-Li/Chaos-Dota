from dotenv import load_dotenv
import discord as ds
from discord.ext import commands
import requests
import os
from discord.ui import Select, View
dotaAPI = 'https://api.opendota.com/api/'

intents = ds.Intents.all() 
client = commands.Bot(command_prefix = '.',intents=intents)

class Player:
    def __init__(self,steamUrl,personaName):
          self.steamUrl = steamUrl
          self.personaName = personaName

    def player(self):
         print(f"{self.personaName}")

@client.event
async def on_ready():
    print('Works.')
    

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

@client.command()
async def status(ctx):
    endpoint = ('live')
    try:
        response = requests.get(dotaAPI + endpoint)
        if response.status_code == 200:
            jResponse = response.json()
            await ctx.send('Tá rolando')
        else:
            print('Error:',response.status_code)
            await ctx.send('Não tá rolando')
    except requests.exceptions.RequestException as e:
        await ctx.send('Complicou')

@client.command()
async def helpme(ctx):
    embed = ds.Embed(
        title = 'Help comands:',
        description = None,
        colour = ds.Colour.blue()

    )

    embed.add_field(
        name='.ping',
        value='Sends a ping to check if the bot is operating',
        inline=False,
        )
    embed.add_field(
        name='.status',
        value="Checks if Dota's server is up and running",
        inline=False,
    )
    embed.add_field(
        name='.player',
        value='Type a player name to get their statistics',
        inline=False,
    )
    embed.add_field(
        name='.compare "<player1>" "<player2>"',
        value='Type the name of two players separated by a space to compare their statistics',
        inline=False,
    )
    await ctx.send(embed=embed)

@client.command()
async def player(ctx, query: str=None):
    if not query:
        await ctx.send('It looks like you tried to use the ".player" command, for more info about how to use it type: ".helpme"')
        return

    dets = {'q' : query}
    endpoint = ('search/')
   
    try:
        response = requests.get(dotaAPI + endpoint, params=dets)
        if response.status_code == 200:
            jResponse = response.json()

            if isinstance(jResponse, list) and jResponse:
                
                nameCounts = {}
                players = []
                for playerDets in jResponse:
                    personaName = playerDets.get('personaname', 'No name')
                    accountId = str(playerDets.get('account_id')) 

                    nameCounts[personaName] = nameCounts.get(personaName, 0) + 1
                    players.append((personaName, accountId))

                duplicates = {name: count for name, count in nameCounts.items() if count > 1}

                if duplicates:
                    
                    duplicateFound = '\n'.join(
                        [f"**{name}:** {count} players" for name, count in duplicates.items()]
                    )
                    await ctx.send(f'Found multiple players with the same persona name:\n{duplicateFound}')

                    
                    players_to_display = players[:5]

                    
                    options = [ds.SelectOption(label=f"{personaName} - {accountId}", value=accountId) for personaName, accountId in players_to_display]
                    select = Select(placeholder="Choose a player", options=options)

                    
                    view = View(timeout=60)
                    view.add_item(select)

                   
                    await ctx.send("Please select a player from the list below:", view=view)

                    
                    interaction = await client.wait_for('interaction', check=lambda i: i.user == ctx.author and i.data['custom_id'] == select.custom_id)

                    
                    chosen_account_id = interaction.data['values'][0]

                    
                    player_details = next((player for player in players if player[1] == chosen_account_id), None)

                    if player_details is None:
                        await interaction.response.send_message('Selected player not found. Please try again.')
                        return

                    personaName, accountId = player_details

                    
                    endpoint = dotaAPI + 'players/'
                    response = requests.get(endpoint + str(accountId))
                    if response.status_code == 200:
                        jResponse = response.json()
                        profile = jResponse.get('profile', {})
                        personaName = profile.get('personaname', 'No name')
                        steamUrl = profile.get('profileurl', 'No profile')
                        player1 = Player(personaName, steamUrl)
                        message = (
                            f'**Persona name:** {player1.personaName}\n'
                            f'**Steam Url:** {player1.steamUrl}'
                        )
                        await ctx.send(message)
                    else:
                        await ctx.send('Error fetching player details.')

                else:
                    
                    accId = jResponse[0]["account_id"]
                    endpoint = dotaAPI + 'players/'
                    response = requests.get(endpoint + str(accId))
                    if response.status_code == 200:
                        jResponse = response.json()
                        profile = jResponse.get('profile', {})
                        personaName = profile.get('personaname', 'No name')
                        steamUrl = profile.get('profileurl', 'No profile')
                        player1 = Player(personaName, steamUrl)
                        message = (
                            f'**Persona name:** {player1.personaName}\n'
                            f'**Steam Url:** {player1.steamUrl}'
                        )
                        await ctx.send(message)

            else:
                await ctx.send('No players found.')

        else:
            await ctx.send('Sei quem é não')

    except requests.exceptions.RequestException as e:
        await ctx.send('Gabe tá ocupado')
        
       
@client.command()
async def compare(ctx, *, query: str):
    try:
        parte1, parte2 = query.split(" ")
    except ValueError:
        await ctx.send("Por favor, digite dois nomes separados por espaço.")
        return

    #Search for the first player
    try:
        dets = {'q': parte1}
        endpoint = 'search/'
        response = requests.get(dotaAPI + endpoint, params=dets)

        if response.status_code == 200:
            jResponse = response.json()
            accId = jResponse[0]["account_id"]
            response = requests.get(f'{dotaAPI}/players/{accId}')

            if response.status_code == 200:
                jResponse = response.json()
                profile = jResponse.get('profile', {})
                personaName = profile.get('personaname', 'No name')
                steamUrl = profile.get('profileurl', 'No profile')
                player1 = Player(personaName, steamUrl)

                print("Jogador 1:", player1.personaName)
            else:
                await ctx.send(f"Não foi possível buscar o jogador: {parte1}")
                return
        else:
            await ctx.send(f"Não foi possível buscar o jogador: {parte1}")
            return
    except requests.exceptions.RequestException:
        await ctx.send("A API está indisponível para o jogador 1.")
        return

    #Search for the second player
    try:
        dets2 = {'q': parte2}
        endpoint = 'search/'
        response2 = requests.get(dotaAPI + endpoint, params=dets2)

        if response2.status_code == 200:
            jResponse2 = response2.json()
            accId2 = jResponse2[0]["account_id"]
            response2 = requests.get(f'{dotaAPI}/players/{accId2}')
            
            if response2.status_code == 200:
                jResponse2 = response2.json()
                profile2 = jResponse2.get('profile', {})
                personaName2 = profile2.get('personaname', 'No name')
                steamUrl2 = profile2.get('profileurl', 'No profile')
                player2 = Player(personaName2, steamUrl2)

                #Displays first and second player
                message = (
                    f"**Jogador 1:** {player1.personaName}\n"
                    f"**Perfil:** {player1.steamUrl}\n\n"
                    f"**Jogador 2:** {player2.personaName}\n"
                    f"**Perfil:** {player2.steamUrl}"
                )
                await ctx.send(message)
            else:
                await ctx.send(f"Não foi possível buscar o jogador: {parte2}")
        else:
            await ctx.send(f"Não foi possível buscar o jogador: {parte2}")
    except requests.exceptions.RequestException:
        await ctx.send("A API está indisponível para o jogador 2.")


     




#Entry point
client.run('bot-discord-token-here')
