import vim
import os
import sys

try:
    import importmagic
    imported = True
except ImportError:
    imported = False


def magic(refresh=None):
    if not imported:
        print("No importmagic. Run 'pip install importmagic'")
        return
    refresh = True if refresh == "!" else False
    current = vim.current.buffer  # or vim.current.range
    text = '\n'.join(current)

    config = vim.eval('g:vim_importmagic_config')
    if not isinstance(config, dict):
        print(
            'g:vim_importmagic_config should be dict, found %s' % type(config))
        return

    path = sys.path + [os.getcwd()]

    # XXX indexing takes too long do it async in background!?
    index = importmagic.SymbolIndex()
    index.get_or_create_index(paths=path, refresh=refresh)

    scope = importmagic.Scope.from_source(text)

    unresolved, unreferenced = scope.find_unresolved_and_unreferenced_symbols()
    text_updated = importmagic.update_imports(
        text, index, unresolved, unreferenced)
    text_updated = text_updated.split('\n')[:-1]
    current[:] = text_updated
