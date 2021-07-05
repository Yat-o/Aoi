import jishaku # is not needed but anyway import it
import aoi

def setup(bot: aoi.AoiBot) -> None:
    bot.load_extension("jishaku")