import os
import sys

path = os.path.dirname(os.path.abspath(__file__)) + '/Handlers'
for py in [f[:-3] for f in os.listdir(path) if f.endswith('.py') and f != '__init__.py']:
    mod = __import__('.'.join(['Handlers', py]), fromlist=[py])
    classes = [getattr(mod, x) for x in dir(mod) if isinstance(getattr(mod, x), type)]
    for cls in classes:
        setattr(sys.modules[__name__], cls.__name__, cls)


def build_handler_list(harley_bot, handlers=[]):
    h = handlers

    add_handlers = [
        UseHandler,
        CryHandler,
        HitHandler,
        DestroyUniverseHandler,
        DestroyYaoiHandler,
        GreetingHandler,
        HateHandler,
        CrusadeHandler,
        VacuumHandler,
        RideHandler,
        FaggotHandler,
        BecomeHandler,
        JokeBanHandler,
        DrinkHandler,
        BiteHandler,
        ScratchHandler,
        FlyHandler,
        RicardoHandler,
        BuildHouseHandler,
    ]

    for handler in add_handlers:
        h.append(handler(harley_bot))

    return h
