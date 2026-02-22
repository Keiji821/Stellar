from setuptools import setup, find_packages
setup(
    name="stellar_translate",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["pyyaml", "rich"],
)
