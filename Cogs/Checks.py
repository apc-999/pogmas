import discord
from discord.ext import commands


def lvl3(**roles):
    original = commands.has_any_role(770380094866063380, 660926272750223361, 754287737439387679, 407585313129758720, 521372852952498179).predicate
    async def lvl3_extend(ctx):
        return ctx.author.id == 414530505585721357
    return commands.check(lvl3_extend)

async def lvl4(ctx):
    return ctx.author.id in (252504297772679168, 378924582452723734, 325357652752203777, 240035755458691072,\
    439784355343237151, 290619509641838603, 390978899645038602, 414530505585721357, 197100324727685121)