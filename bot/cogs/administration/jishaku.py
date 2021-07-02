from bot import aoi
from jishaku.cog import Jishaku

def setup(bot: aoi.AoiBot) -> None:
    bot.add_cog(Jishaku(bot=bot))