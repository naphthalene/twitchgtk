#!/usr/bin/env python

from distutils.core import setup, find_packages
from twitchgtk.VERSION import version as twitchgtk_version

setup(
    name='twitchgtk',
    version=twitchgtk_version,
    packages=find_packages(),

    author='Pavel Sadikov',
    author_email='pashalab@gmail.com',
    maintainer='Pavel Sadikov',
    maintainer_email='pashalab@gmail.com'
    description='twitch.tv GTK+ client',
    keywords='gtk twitch twitch.tv livestreamer games',
    url='https://github.com/naphthalene/twitchgtk',

    namespace_packages=['twitchgtk']

    install_required=[
        'livestreamer>=1.12.0',
        'twitcherapi>=0.8.0',
    ]
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'twitchgtk=twitchgtk.run:twitchgtk'
        ]
    }
)
