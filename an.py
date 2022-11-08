import discord
from discord.ext import commands
from discord.commands import Option
import time
bot = discord.Bot()

class an(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self._last_member = None

    @commands.has_permissions(administrator=True)
    @bot.slash_command(description="공지 보내기",administrator=True)
    async def 공지사항(
        self,
        ctx,
        전송채널: discord.TextChannel,
        내용: Option(str,"내용을 입력해주세요")
    ):
        embed=(
            discord.Embed(
                title="📢 공지사항",
                description=f"{내용}\n\n전송채널: `{전송채널}`",
                color=0xFF0000
            )
        )
        await ctx.respond(embed=embed)
        await 전송채널.send(f"@everyone\n",embed=embed)
    
    @공지사항.error
    async def an_error(slf,ctx,error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.respond("해당 명령어는 관리자만 사용 가능합니다.")