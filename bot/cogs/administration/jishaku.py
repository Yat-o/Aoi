from bot import aoi
from jishaku.cog import Jishaku

class MyJishaku(Jishaku):
  @property
  def description(self):
    return "Jishaku"


def setup(bot: aoi.AoiBot):
    cog = MyJishaku(bot=bot)

    for command in cog.walk_commands():
      command.brief="Just know what it does"

    bot.add_cog(cog)