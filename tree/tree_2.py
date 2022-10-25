from hexlet.fs import mkdir, mkfile


# Пример создания файловой структуры с метаданными
def generate():
    tree = mkdir('python-package', [
        mkfile('Makefile'), mkfile('README.md'), mkdir('dist', [
        ]), mkdir('test',[
            mkfile('test_solution.py')
        ]), mkfile('pyproject.toml'), mkdir('.venv', [
            mkdir('lib',[
                mkdir('python3.6', [
                    mkdir('site-packages', [
                        mkfile('hexlet-python-package.egg-link')
                    ])
                ])
            ])
        ], {'owner': 'root', 'hidden': False})

    ], {'hidden': True})
    return tree
# END
