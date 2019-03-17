if has('python3')
    command! -nargs=1 Python python3 <args>
elseif has('python')
    command! -nargs=1 Python python <args>
else
    echo "Error: Requires Vim compiled with +python or +python3"
    finish
endif

" init load script parent path :h:h
execute "Python import sys"
execute "Python print('Plugin: " . expand("<sfile>:p:h:h") . "')"
execute "Python sys.path.append(r'" . expand("<sfile>:p:h:h") . "')"

Python << EOF
print("excecuted")
if 'vimimportmagic' not in sys.modules:
    import vimimportmagic
else:
    import imp
    # Reload python module to avoid errors when updating plugin
    vimimportmagic = imp.reload(vimimportmagic)
print(vimimportmagic.__file__)
EOF

if !exists('g:vim_importmagic_config')
    let g:vim_importmagic_config = {}
endif

" register command
command! -bang ImportMagic exec("Python vimimportmagic.magic('<bang>')")
