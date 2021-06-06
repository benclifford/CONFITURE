

# circuit python doesn't have functools.partial, but
# they give this source on:
# https://learn.adafruit.com/partials-in-circuitpython/more-complex-partial-application
def partial(func, *args):
    def newfunc(*fargs):
        return func(*(args + fargs))
    return newfunc
