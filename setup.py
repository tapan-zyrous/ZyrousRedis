import setuptools


VERSION = "0.0.1"
DESCRIPTION = "Zyrous Redis Module Experiment"
LONG_DESCRIPTION = "It is just demonstration of how to create python package for zyrous framework"

# Setting up
setuptools.setup(
    name="zyrous-redis",
    version=VERSION,
    author="Tapan Parmar",
    namespace_packages=["zyrous"],
    author_email="tapan.parmar@zyrous.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    package_dir={"": "src"},
    entry_points={"zyrous_plugins": ["zredis = zyrous.zredis"]},
    packages=setuptools.find_packages(where="src"),
    install_requires=[],
    keywords=["redis", "repository"],
)