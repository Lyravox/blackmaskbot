import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from nextcord import Member
from datetime import datetime

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @nextcord.slash_command(description='Gives info on commands')
    async def help(self, interaction: Interaction):
        text = """
My current commands are:    
> Ping: Gives bot latency.
> Avatar: Gets a specfic users avatar.
"""

        await interaction.response.send_message(text)
        
    @nextcord.slash_command(description="Gives bot latency")
    async def ping(self, interaction: Interaction):
        latency = round(self.bot.latency * 1000)
        await interaction.send(f"Pong! The bot's latency is {latency} ms.")

    @nextcord.slash_command(description="Displays information about the server")
    async def server(self, interaction: Interaction):
        guild = interaction.guild
        created_at = guild.created_at.strftime("%d %b %Y - %H:%M ")
        member_count = guild.member_count
        server_name = guild.name
        description = f"""
Server name: {server_name}
Member count: {member_count}
Created at: {created_at}
        """
        await interaction.response.send_message(description)
                
    @nextcord.slash_command(description="Displays information about a specfic user")
    async def user(self, interaction: Interaction, member: Member = None):
        if member == None:
            member = interaction.user
        name = member.name
        mention = member.mention
        
        embed = nextcord.Embed(
            title=name + "'s Information",
            color=0x2ecc71
        )
        embed.add_field(name="Name:", value=f"{mention}")
        
        await interaction.response.send_message(embed=embed)
    
    @nextcord.slash_command(description="Displays the avatar of a specfic user")
    async def avatar(self, interaction: Interaction, member: Member = None):
        if member is None:
            member = interaction.user
        avatar_url = str(member.avatar.url)
        name = member.name
        
        embed = nextcord.Embed(title=name + "'s Avatar:", color=0x1abc9c)
        embed.set_image(avatar_url)
        
        await interaction.response.send_message(embed=embed)
        
    @nextcord.slash_command(description="Displays server emojis")
    async def emojis(self, interaction: Interaction):
        emojis = interaction.guild.emojis
        if emojis:
            emoji_str = " ".join(str(emoji) for emoji in emojis)
            if len(emoji_str) <= 2000:
                await interaction.response.send_message(emoji_str)
            else:
                pass
            
        else:
            await interaction.response.send_message("No custom emojis available")
                
def setup(bot):
    bot.add_cog(Utilities(bot))