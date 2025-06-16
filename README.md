# discord.py-template
A simple Discord.py bot ([with cogs](https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html)) template I use for all of my bots. Feel free to use and modify it.

## Usage
1. **Get a Bot Token:**  
    Create a bot in [Discord's Developer Portal](https://discord.com/developers/applications/) and copy its token. Make sure you have enabled all of the **Privileged Gateway Intents**!

2. **Create Environment File:**  
    Rename `.env.example` to `.env`.

3. **Add the Token:**  
    Paste the token into the `.env` file. It should look like this:
    ```bash
    # https://discord.com/developers/applications
    BOT_TOKEN="MTM0NTY3ODkwMTIzNDU2Nzg5.CDEfGH.IJKLMN_opq1234567890abcdef"
    ```

4. **Instal Dependencies:**  
    ```bash
    python -m pip install -r requirements.txt
    ```

5. **Create Your First Command (Cog):**  
    The bot automatically detects (recursively) cogs inside `src/cogs/` directory and loads them up. Here is a simple "hello" slash command to get you started:

    ```py
    import discord
    from discord import app_commands
    from discord.ext import commands
    from ..bot import Bot


    class Greetings(commands.Cog):
        def __init__(self, bot: Bot):
            self.bot = bot

        @app_commands.command(name="hello", description="Greets the user back.")
        async def hello(self, interaction: discord.Interaction):
            await interaction.response.send_message(f"Hello, {interaction.user.mention}!")


    async def setup(bot: Bot):
        await bot.add_cog(Greetings(bot))
    ```

    For more information, please [read this](https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html).

6. **Run the Bot:**  
    ```bash
    python main.py
    ```