# Change nickname
# Prod. meatroast

import discord
from discord.ext import commands
from discord.commands import Option
import time
bot = discord.Bot()

class nickname(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self._last_member = None

    @bot.slash_command(description="닉네임변경")
    async def 닉네임변경(
        self,
        ctx,
        닉네임: Option(str,"변경하실 닉네임을 입력해주세요")
    ):
        await ctx.author.edit(nick=f"{닉네임}")

        embed=(
            discord.Embed(
                title=f"닉네임이 정상적으로 변경되었습니다.",
                description="Change nickname",
                color=0xFBFF6C
            )
            .add_field(
                name=f"{닉네임}",
                value=f"<@!{ctx.author.id}>",
                inline=False
            )
        )
        await ctx.respond(embed=embed)