from setuptools import setup, find_packages


setup(
    name="interruptingboar",
    use_scm_version=True,
    packages=find_packages(),
    author="Konrad Jałowiecki <dexter2206@gmail.com>",
    setup_requires=["setuptools_scm"]
)