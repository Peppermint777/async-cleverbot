"""
MIT License

Copyright (c) 2018-2021 chr1s

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Example Cleverbot cog for discord.py@rewrite bots.

import discord
from discord.ext import commands
import async_cleverbot as ac


class Cleverbot(commands.Cog):
    """Commands for interacting with the Travitia Cleverbot API"""

    def __init__(self, bot):
        self.bot = bot
        self.cleverbot = ac.Cleverbot("API key here", context=ac.DictContext())

    @commands.command(name="cleverbot", aliases=["cb"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cleverbot_(self, ctx, *, query: str):
        """Ask Cleverbot a question!"""
        try:
            r = await self.cleverbot.ask(query, ctx.author.id) # the ID is for context
        except ac.InvalidKey:
            return await ctx.send("An error has occurred. The API key provided was not valid.")
        except ac.APIDown:
            return await ctx.send("I have to sleep sometimes. Please ask me later!")
        else:
            await ctx.send("{}, {}".format(ctx.author.mention, r.text))

    def cog_unload(self):
        self.bot.loop.create_task(self.cleverbot.close())


def setup(bot):
    bot.add_cog(Cleverbot(bot))
