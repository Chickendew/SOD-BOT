"""
Map randomation (with bans) Discord bot

Made for the Steel Division League

Random map gen written by Scoutspirit with modifications by Chickendew
Map ban system written by Chickendew
Faction picker written by Chickendew
Additional features written by Chickendew

Written in Python 3.5.2 
"""
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random

Client = discord.Client()
Bot = commands.Bot(command_prefix = "$")

#List of maps availible in SD
Maps = ["Pointe du Hoc","Pegasus Bridge","Omaha","Odon","Mont Ormel","Merderet","Cote 112","Colombelles","Colleville","Cheux","Caumont l'Evente","Carpiquet","Bois de Limors","Carpiquet-Duellist","Odon River","Sainte Mere l'Eglise","Sainte Mere l'Eglise Duellists"]
#Stores which maps (by number in list) are banned and which are not banned. When program starts they are all unbanned.
MapAllowed = [True]*17

#When called clears all bans.
def ClearBans():
    global  MapAllowed
    MapAllowed = [True]*17

#When the program is started in the console (not discord) a message will be displayed. 
@Bot.event
async def on_ready():
    print("Bot is ready!")

#When any message is recived the bot will check through it.
@Bot.event
async def on_message(message):
    
    userID = message.author.id #The bot records the ID of the user in case it needs to mention it later
    
    if message.content.upper().startswith("$PIAT"):#If the message starts with $PIAT
        await Bot.send_message(message.channel,"<@{}> Miss!".format(userID))#The bot will shoot the PIAT
        
    if message.content.upper().startswith("$BAN"):#If the message start with $BAN
            #The first statement with the correct key words releating to its map will ban that map. Maps ordered in preference.
            if ("carp" in message.content.lower()) and ("duel" in message.content.lower()):
                MapAllowed[13] = False
                await Bot.send_message(message.channel,"<@{}> Carpiquet-Duellist banned!".format(userID))
            elif "odon river" in message.content.lower():
                MapAllowed[14] = False
                await Bot.send_message(message.channel,"<@{}> Odon River banned!".format(userID))
            elif  ("saint" in message.content.lower()) and ("duel" in message.content.lower()):
                MapAllowed[16] = False
                await Bot.send_message(message.channel,"<@{}> Sainte Mere l'Eglise Duellists banned!".format(userID))
            elif ("saint" in message.content.lower()) or ("eglise" in message.content.lower()):
                MapAllowed[15] = False
                await Bot.send_message(message.channel,"<@{}> Sainte Mere l'Eglise banned!".format(userID))
            elif "hoc" in message.content.lower():
                MapAllowed[0] = False
                await Bot.send_message(message.channel,"<@{}> Pointe du Hoc banned!".format(userID))
            elif ("pegasus" in message.content.lower())or ("bridge" in message.content.lower()):
                MapAllowed[1] = False
                await Bot.send_message(message.channel,"<@{}> Pegasus Bridge banned!".format(userID))
            elif "omaha" in message.content.lower():
                MapAllowed[2] = False
                await Bot.send_message(message.channel,"<@{}> Omaha banned!".format(userID))
            elif "odon" in message.content.lower():
                MapAllowed[3] = False
                await Bot.send_message(message.channel,"<@{}> Odon banned!".format(userID))
            elif "ormel" in message.content.lower():
                MapAllowed[4] = False
                await Bot.send_message(message.channel,"<@{}> Mont Ormel banned!".format(userID))
            elif "merderet" in message.content.lower():
                MapAllowed[5] = False
                await Bot.send_message(message.channel,"<@{}> Merderet banned".format(userID))
            elif "112" in message.content.lower():
                MapAllowed[6] = False
                await Bot.send_message(message.channel,"<@{}> Cote 112 banned!".format(userID))
            elif "colom" in message.content.lower():
                MapAllowed[7] = False
                await Bot.send_message(message.channel,"<@{}> Colombelles banned!".format(userID))
            elif ("coll" in message.content.lower())or ("ville" in message.content.lower()):
                MapAllowed[8] = False
                await Bot.send_message(message.channel,"<@{}>Colleville  banned!".format(userID))
            elif "cheux" in message.content.lower():
                MapAllowed[9] = False
                await Bot.send_message(message.channel,"<@{}> Cheux banned!".format(userID))
            elif "cau" in message.content.lower():
                MapAllowed[10] = False
                await Bot.send_message(message.channel,"<@{}> Caumont l'Evente banned!".format(userID))
            elif "carp" in message.content.lower():
                MapAllowed[11] = False
                await Bot.send_message(message.channel,"<@{}> Carpiquet banned!".format(userID))
            elif ("bois" in message.content.lower()) or ("limors" in message.content.lower()):
                MapAllowed[12] = False
                await Bot.send_message(message.channel,"<@{}> Bois de Limors banned!".format(userID))
           
            
    if message.content.upper().startswith("$RESET"):#If a message starts with $Reset
        ClearBans()#Calls the clear bans Procedure, which resets all bans
        await Bot.send_message(message.channel,"<@{}> Random map generator reset.".format(userID))
        
    if message.content.upper().startswith("$MAP"):#If a message starts with $Map
        if "$MAPS" not in message.content.upper():#Stops this command conflicting with $Maps
            MapNotChosen = True
            while MapNotChosen: #Repeats until a map that is not banned is chosen
                if '4v4' in message.content.lower(): #If 4v4 is present anywhere in the message
                    MapNumber = random.randint(0, ((len(Maps))-6)) #generates a number representing a map up to the last 4v4 map in the maps list
                    if (MapAllowed[MapNumber]):#Checks this against the bans. If the map is not banned following code is executed
                        await Bot.send_message(message.channel,("<@{}>".format(userID) + " " + (Maps[MapNumber])))#display map
                        MapNotChosen = False #ends search for valid map
                        ClearBans() #Calls the clear bans Procedure, which resets all bans
                        await Bot.send_message(message.channel,"<@{}> Random map generator reset.".format(userID))                       
                elif ('1v1' in message.content.lower())  or ('2v2' in message.content.lower()) or ('3v3' in message.content.lower()):#If any map size other than 4v4 is present in the message
                    MapNumber = random.randint(0,((len(Maps)-1)))#generates a number representing a map up to the maximun amount of maps in SD
                    if (MapAllowed[MapNumber]): #Checks this against the bans. If the map is not banned following code is executed
                        await Bot.send_message(message.channel,("<@{}>".format(userID) + " " + (Maps[MapNumber])))#display map
                        MapNotChosen = False #ends search for valid map
                        ClearBans()#Calls the clear bans Procedure, which resets all bans
                        await Bot.send_message(message.channel,"<@{}> Random map generator reset.".format(userID))                       
                else:
                    await Bot.send_message(message.channel,"<@{}> When using the map command please input the size (1v1, 2v2, 3v3, 4v4).".format(userID))
                    MapNotChosen = False #ends search for valid map


    if message.content.upper().startswith("$FACTION"):#If a message starts with $faction
        Faction = random.randint(0,1)#random number 0-1 created
        if Faction: #If 1 Allies
             await Bot.send_message(message.channel,"<@{}> Allies.".format(userID))
        else: #If 0 Axis
            await Bot.send_message(message.channel,"<@{}> Axis.".format(userID))


    if message.content.upper().startswith("$HELP"): #Creates an embeded message with all the fields below. Name is the heading of each field. Field is the description of the heading.Describes all the commands. 
        embed = discord.Embed(title="The Commandments", description="The following list describes the commands that SOD BOT follows.", color=0x00ff00)
        embed.add_field(name="$Map (map size)", value="Gives a random map (excluding bans) that is availible in the mapsize entered. Map sizes are: 1v1, 2v2, 3v3, 4v4. After randomising a map all bans are reset.", inline=False)
        embed.add_field(name="$Ban (map name)", value="Excludes the map named in the random map picker.", inline=False)
        embed.add_field(name="$Reset", value="Removes all the current bans.", inline=False)
        embed.add_field(name="$Maps", value="Gives a list of maps and states if they are banned or allowed.", inline=False)
        embed.add_field(name="$Faction", value="Gives a random faction.", inline=False)
        embed.add_field(name="$Info", value="Gives information about the creation of SOD BOT.", inline=False)
        embed.add_field(name="$PIAT", value="Fires SOD BOT's PIAT!", inline=False)
        await Bot.send_message(message.channel, embed=embed)


    if message.content.upper().startswith("$MAPS"):
        embed = discord.Embed(title="List of Maps", description="The following list presents all the availible maps in Steel Division and whether or not they are banned.", color=0x00ff00)
        for x in range(0, 17):#loops through all maps creating a heading and description on each one. The description reflects if it banned or allowed. 
            if MapAllowed[x]:
                MapBannedStatus = "Map allowed"
            else:
                MapBannedStatus = "***Map banned***"
            embed.add_field(name= (Maps[x]), value=MapBannedStatus, inline=False)
        await Bot.send_message(message.channel, embed=embed)


    if message.content.upper().startswith("$INFO"):#Creates an embeded message with all the fields below. Name is the heading of each field. Field is the description of the heading. Describes who made the program and how.
        embed = discord.Embed(title="Authors", description="Random map generator written by ScoutSpirit with small modification by Chickendew. Map ban system, faction randomiser, help, documentation, and additional features written by Chickendew. Moral support provided by Curbs", color=0x00ff00)
        embed.add_field(name="Creation", value="Created in Python 3.5 using Discord API", inline=False)
        await Bot.send_message(message.channel, embed=embed)
         
         
         
    
    

Bot.run("NDUwMjg1NjU3OTk1MjE0ODQ5.DexBlw.4O7mZN4X2VUf9EwqfDCgzEfDXLE") #Runs the bot with the bots ID Token

