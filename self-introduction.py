# self-introduction
# Prod. meatroast

from ast import Break
import discord
from discord.ext import commands
from discord.commands import Option
import time
bot = discord.Bot()

class myself(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self._last_member = None

    @bot.slash_command(description="자기소개하기")
    async def 자기소개(
        self,
        ctx,
        닉네임: Option(str, "닉네임을 입력해주세요."),
        나이: Option(str,"나이를 선택해주세요", choices=["10대","20대"]),
        성별: Option(str,"성별을 선택해주세요", choices=["여자","남자"]),
        생일_월: Option(str,"생일을 입력해주세요",choices=["1월","2월","3월","4월","5월","6월","7월","8월","9월","10월","11월","12월"]),
        생일_일: Option(str,"숫자만 입력해주세요"),
        나이비공개유무: Option(str,"나이 비공개 유무", choices=["공개","비공개"])
    ):
        embed=(
            discord.Embed(
                title=f"자기소개 정보 입니다.",
                description="self-introduction",
                color=0xFBFF6C
            )
            .add_field(
                name=f"{닉네임}",
                value="닉네임",
                inline=False
            )
            .add_field(
                name=f"{나이}",
                value="나이",
                inline=False
            )
            .add_field(
                name=f"{성별}",
                value="성별",
                inline=False
            )
            .add_field(
                name=f"{생일_월} {생일_일}일",
                value="생일",
                inline=False
            )
        )
        awa = await ctx.respond("자기소개 내역을 처리중입니다...", ephemeral=True)
        if 나이 == "10대":
            a = 00000
        if 나이 == "20대":
            a = 00000
        if 성별 == "남자":
            gender = 00000
        if 성별 == "여자":
            gender = 00000
        age = discord.utils.get(ctx.guild.roles, id=a)
        genders = discord.utils.get(ctx.guild.roles, id=gender)
        await ctx.author.add_roles(
            age,
            genders
        )
        await ctx.author.edit(nick=f"{닉네임}")
        time.sleep(0.3)
        await awa.edit_original_response(
            content = "처리가 완료되었습니다.\3초후 해당 채널이 안보입니다.",
            embed=embed
        )
        자기소개관리 = self.bot.get_channel(int(00000))
        await 자기소개관리.send(f"{ctx.author}님의 자기소개 정보입니다.( {ctx.author.id} )",embed=embed)
        test = self.bot.get_channel(int(00000))
        if 나이비공개유무 == "공개":
            embed=(
                discord.Embed(
                    title=f"{닉네임}님 어서오세요!!",
                    description="",
                    color=0xFBFF6C
                )
                .add_field(
                    name=f"{나이}",
                    value="나이",
                    inline=False
                )
                .add_field(
                    name=f"{성별}",
                    value="성별",
                    inline=False
                )
                .add_field(
                    name=f"{생일_월} {생일_일}일",
                    value="생일",
                    inline=False
                )
            )
            await test.send(embed=embed)
            time.sleep(3)
        if 나이비공개유무 == "비공개":
            await ctx.author.remove_roles(age)
            await ctx.author.add_roles(discord.utils.get(ctx.guild.roles, id=00000))
            embed=(
                discord.Embed(
                    title=f"{닉네임}님 어서오세요!!",
                    description="고깃집서버 시즌2에 오신걸 환영합니다!",
                    color=0xFBFF6C
                )
                .add_field(
                    name=f"비공개",
                    value="나이",
                    inline=False
                )
                .add_field(
                    name=f"{성별}",
                    value="성별",
                    inline=False
                )
                .add_field(
                    name=f"{생일_월} {생일_일}일",
                    value="생일",
                    inline=False
                )
            )
            await test.send(embed=embed)
        
        time.sleep(3)
        await ctx.author.remove_roles(discord.utils.get(ctx.guild.roles, id=00000))