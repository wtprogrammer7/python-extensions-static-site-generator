_callbacks = {}

def register(hook, order = 0):
    def register_callback(func):
        _callbacks.setdefault(hook, {})
        _callbacks.setdefault(order, [])
        _callbacks.append(func)
        return func
    return register_callback