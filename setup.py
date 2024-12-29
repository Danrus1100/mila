from setuptools import setup, find_packages
from setuptools.command.install import install
import os

class CustomInstall(install):
    def run(self):
        os.makedirs(os.path.expanduser("~/.mila"), exist_ok=True)
        install.run(self)
        
setup(
    name="mila",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "mila=mila.main:main",
        ],
    },
    cmdclass={
        "install": CustomInstall,
    },
)
