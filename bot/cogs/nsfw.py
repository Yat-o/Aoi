from random import choice

import aiohttp
from discord.ext import commands

from bot import aoi


class NSFW(commands.Cog):
    """NSFW related commands"""
    def __init__(self, bot: aoi.AoiBot):
        self.bot = bot

    @commands.command(brief="Obligatory Hentai Command. Run `[p]hentai list` for available tags")
    async def hentai(self, ctx: aoi.AoiContext, *, tag: str = None):
        endpoints = {
            "random hentai gif": "Random_hentai_gif",
            "pussy": "pussy",
            "nsfw neko gif": "nsfw_neko_gif",
            "lewd": "lewd",
            "les": "les",
            "kuni": "kuni",
            "cum": "cum",
            "classic": "classic",
            "boobs": "boobs",
            "bj": "bj",
            "anal": "anal",
            "yuri": "yuri",
            "trap": "trap",
            "tits": "tits",
            "solog": "solog",
            "solo": "solo",
            "pwankg": "pwankg",
            "pussy jpg": "pussy_jpg",
            "lewdkemo": "lewdkemo",
            "lewdk": "lewdk",
            "keta": "keta",
            "hololewd": "hololewd",
            "holoero": "holoero",
            "hentai": "hentai",
            "femdom": "femdom",
            "feetg": "feetg",
            "erofeet": "erofeet",
            "feet": "feet",
            "ero": "ero",
            "erok": "erok",
            "erokemo": "erokemo",
            "cum_jpg": "cum_jpg",
            "gasm": "gasm",
        }

        if tag is None:
            tag = choice(list(endpoints.values()))

        if tag is not None and tag.lower() == "list":
            available_tags = "\n".join(list(endpoints.values()))
            return await ctx.send_info(f"Available Tags:\n{available_tags}")

        if tag is not None and tag in endpoints.keys():
            tag = endpoints.get(tag)
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://nekos.life/api/v2/img/{tag}") as resp:
                    await ctx.embed(image=(await resp.json())["url"])
        else:
            await ctx.send_error(f"Tag not found in available tags. Run `{ctx.clean_prefix}hentai list` to see all tags")

def setup(bot: aoi.AoiBot) -> None:
    bot.add_cog(NSFW(bot))