# Import the discord.py library
import discord
from discord.ext import commands
import csv
intents = discord.Intents.all()

# Create a bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

# Define a command to export all roles' permissions into a csv file
@bot.command(name='export')
async def export(ctx):
    # Get the guild object
    guild = ctx.guild
    # Create a list to store the role data
    role_data = []
    
    # Loop through all the roles in the guild
    for role in reversed(guild.roles):
        # Get the permissions of the role
        permissions = role.permissions
        # Convert the permissions object into a dictionary
        permissions_dict = dict(permissions)
        # Add the role name and the permissions dictionary to the role data list
        role_data.append([role.name, permissions_dict])

    # Create a csv file name using the guild name
    csv_file = f"{guild.name}_roles.csv"

    # Open the csv file in write mode with UTF-8 encoding
    with open(csv_file, "w", newline='', encoding='utf-8') as f:
        # Create a CSV writer object
        csv_writer = csv.writer(f)
        # Write the header row
        csv_writer.writerow(["Role"] + list(permissions_dict.keys()))

        # Loop through the role data list
        for role in role_data:
            # Write the role name
            csv_writer.writerow([role[0]] + [role[1].get(perm, False) for perm in permissions_dict.keys()])

    # Send the csv file to the channel
    await ctx.send(file=discord.File(csv_file))

# Run the bot with your token

bot.run("Your_TOKEN")
