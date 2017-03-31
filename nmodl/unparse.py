from functools import singledispatch
from nmodl.program import Program
from nmodl.title import Title
from nmodl.units import Units, UnitRef, UnitDef

from jinja2 import Environment
E = Environment(trim_blocks=True, lstrip_blocks=True)
from textwrap import dedent


@singledispatch
def unparse(obj):
    pass


@unparse.register(Program)
def _(program):
    return unparse(program.title[0]) 


@unparse.register(Title)
def _(title):
    return 'TITLE ' + title.title


@unparse.register(Units)
def _(units):
    return E.from_string(dedent('''
    UNITS {
        {% for ud in unit_defs %}
        {{ud}}
        {% endfor %}
    }''')).render(unit_defs=(unparse(ud) for ud in units.unit_defs))


@unparse.register(UnitDef)
def _(unit_def: UnitDef):
    return "({l}) = ({r})".format(
        l=unparse(unit_def.left), r=unparse(unit_def.right))


@unparse.register(UnitRef)
def _(unit_ref: UnitRef):
    return unit_ref.id
