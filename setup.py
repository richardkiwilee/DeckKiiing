from setuptools import setup, find_packages


def version():
    with open(r'.\deckiiing\__version__.py', 'r') as v:
        content = v.read().split('\n')[0]
    return content.split('=')[-1]


def requirements():
    with open('requirements.txt', 'r') as r:
        content = r.readlines()
    res = []
    for item in content:
        res.append( item.split('\n')[0])
    return res


if __name__ == '__main__':

    setup(
        name="deckiiing",
        version=version(),
        description="Deck Building Master System",
        license="MIT Licence",
        author="yujj&lirc",
        packages=find_packages(),
        include_package_data=True,
        platforms="any",
        install_requires=requirements(),
        scripts=[],
        entry_points={
            'console_scripts': [
                'deckiiing = deckiiing:main'
            ]
        }
    )
