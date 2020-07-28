from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    requires = [line.rstrip() for line in f.readlines()]


def get_version():
    u""" 从__version__.py中读取版本号。 """
    with open('deckiiing/__version__.py', encoding='utf-8-sig') as version_file:
        for line in version_file:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


if __name__ == '__main__':
    setup(
        name='deckiiing',
        description='Deck Building Master System',
        version=get_version(),
        packages=find_packages(),
        entry_points={'console_scripts': ['deckiiing=deckiiing:cli']},
        zip_safe=False,
        license="MIT Licence",
        package_data={
            'deckiiing': ['bin/*.*']
        },
        include_package_data=True,
        install_requires=requires,
        author='yujj&lirc',
        python_requires='>=3.6, <3.8',
        platforms="win_amd64"
    )
