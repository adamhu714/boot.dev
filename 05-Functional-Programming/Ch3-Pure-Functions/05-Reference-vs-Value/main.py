def add_format(default_formats, new_format):
    default_formats_copy = default_formats.copy()
    default_formats_copy[new_format] = True
    return default_formats_copy


def remove_format(default_formats, old_format):
    default_formats_copy = default_formats.copy()
    default_formats_copy[old_format] = False
    return default_formats_copy
