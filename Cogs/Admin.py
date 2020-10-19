import discord
from discord.ext import commands
import asyncio

class Admin(commands.Cog):
     def __init__(self, bot):
        self.bot = bot

     @commands.command(hidden=True)
     async def restart(self, ctx):
          bot_owner_id = 414530505585721357
          if ctx.author.id == bot_owner_id:
               message = await ctx.send("Ok! I'll restart now...")
               await self.bot.close()
          else:
               await ctx.send("You don't need to use this command :)")

     @commands.command(hidden=True)
     @commands.has_any_role(407585313129758720, 521372852952498179, 746485340545613915)
     async def say(self, ctx, channel:discord.TextChannel, *, words:str):
          await ctx.message.delete()
          await channel.trigger_typing()
          await asyncio.sleep(3)
          await channel.send(words)


    # If they don't have a role for it

     @commands.command(hidden=True)
     @commands.has_any_role(407585313129758720, 521372852952498179, 746485340545613915)
     async def dm(self, ctx, member:discord.Member, *, words):
         user = member
         await user.send(words)
         await ctx.message.delete()

# If they don't have the role

     @commands.command(name='load', hidden=True, description="Command which Loads a Module.\
     Remember to use dot path. e.g: Cogs.Admin")
     @commands.is_owner()
     async def acog_load(self, ctx, *, cog: str):
         try:
             self.bot.load_extension(cog)
         except Exception as e:
             await ctx.send(f'**`An error occured:`** ```py\n{type(e).__name__} - {e}\n```')
         else:
             await ctx.send(f'`{cog}` has been loaded!')

     @commands.command(name='unload', hidden=True, description="Command which Unloads a Module.\
     Remember to use dot path. e.g: Cogs.Admin")
     @commands.is_owner()
     async def acog_unload(self, ctx, *, cog: str):
         try:
             self.bot.unload_extension(cog)
         except Exception as e:
             await ctx.send(f'**`An error occured:`** ```py\n{type(e).__name__} - {e}\n```')
         else:
             await ctx.send(f'`{cog}` has been unloaded!')

     @commands.command(name='reload', hidden=True, aliases=["hotload", "hl"], description="Command which Reloads a Module.\
     Remember to use dot path. e.g: Cogs.Admin")
     @commands.is_owner()
     async def acog_reload(self, ctx, *, cog: str):
         try:
             self.bot.reload_extension(cog)
         except Exception as e:
             await ctx.send(f'**`An error occured:`** ```py\n{type(e).__name__} - {e}\n```')
         else:
             await ctx.send(f'`{cog}` has been hot-loaded! 🔥')



     @commands.is_owner()
     @commands.command(name="status", hidden=True)
     async def online(self, ctx, status:str=None):
         if status.lower() in (None,"g", "online"):
             await self.bot.change_presence(status=discord.Status.online)
             await ctx.send("Status set to online!")
         elif status.lower() in ("idle","yellow", "away", "y"):
             await self.bot.change_presence(status=discord.Status.idle)
             await ctx.send("Status set to idle!")
         elif status.lower() in ("dnd", "red", "r"):
             await self.bot.change_presence(status=discord.Status.dnd)
             await ctx.send("Status set to do not disturb!")
         else:
             await self.bot.change_presence(status=discord.Status.invisible)
             await ctx.send("Status set to offline!")


     @commands.is_owner()
     @commands.command(hidden=True)
     async def activity(self, ctx, status:str=None, *, an:str=None):
         if status is None:
             await self.bot.change_presence(activity=None)
             await ctx.send("Activity set to nothing!")
         elif status in ("playing", "p", "play", "game"):
             await self.bot.change_presence(activity=discord.Game(name=an))
             await ctx.send(f"I will now play {an}!")
         elif status in ("watching", "w", "watch", "tv"):
             await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=an))
             await ctx.send(f"I will now watch {an}!")
         elif status in ("listening", "l", "listen", "song"):
             await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=an))
             await ctx.send(f"I will now listen to {an}!")
         elif status in ("competing", "c", "compete", "battle"):
             # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name="a battle"))
             await ctx.send("Hang on! (will be in next update.)")
         else:
             await ctx.send("Invalid option.")

def setup(bot):
    bot.add_cog(Admin(bot))