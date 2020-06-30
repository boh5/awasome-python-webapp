from www import config_default


class Dict(dict):
    """
    支持 x.y 访问的 dict
    """

    def __init__(self, names=(), values=(), **kwargs):
        super().__init__(**kwargs)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"'Dict' object has no attribute {key}")

    def __setattr__(self, key, value):
        self[key] = value


def merge(defaults: dict, override: dict) -> dict:
    r = {}
    for k, v in defaults.items():
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    return r


def to_dict(d: dict) -> Dict:
    D = Dict()
    for k, v in d.items():
        D[k] = to_dict(v) if isinstance(v, dict) else v
    return D


configs = config_default.configs

try:
    from www import config_override

    configs = merge(configs, config_override.configs)
except ImportError:
    pass

configs = to_dict(configs)
