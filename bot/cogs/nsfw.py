from random import choice

import aiohttp
from discord.ext import commands

from bot import aoi


class NSFW(commands.Cog):
    """NSFW related commands"""
    def __init__(self, bot: aoi.AoiBot):
        self.bot = bot

    @commands.command(brief="Obligatory Hentai Command. Run `[p]hentai list` for available tags")
    async def hentai(self, ctx: aoi.AoiContext, tag: str = None):
        endpoints = [
            "Random_hentai_gif",
            "pussy",
            "nsfw_neko_gif",
            "lewd",
            "les",
            "kuni",
            "cum",
            "classic",
            "boobs",
            "bj",
            "anal",
            "yuri",
            "trap",
            "tits",
            "solog",
            "solo",
            "pwankg",
            "pussy_jpg",
            "lewdkemo",
            "lewdk",
            "keta",
            "hololewd",
            "holoero",
            "hentai",
            "femdom",
            "feetg",
            "erofeet",
            "feet",
            "ero",
            "erok",
            "erokemo",
            "cum_jpg",
            "gasm",
        ]
        if tag.lower() == "list":
            endpoint_list = "\n".join(endpoints)
            return await ctx.embed(description=f"```{endpoint_list}```")

        if tag is None:
            tag = choice(endpoints)

        if tag in endpoints:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://nekos.life/api/v2/img/{tag}") as resp:
                    await ctx.embed(image=(await resp.json())["url"])
        else:
            await ctx.send_error(f"Tag not found in available tags. Run `{ctx.clean_prefix}hentai list` to see all tags")

def setup(bot: aoi.AoiBot) -> None:
    bot.add_cog(NSFW(bot))