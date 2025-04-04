from msgspec import to_builtins


def struct_to_dict(obj, exclude_none=True) -> dict:
    return {k: v for k, v in to_builtins(obj).items() if not (exclude_none and v is None)}
