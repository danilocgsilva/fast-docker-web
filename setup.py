from setuptools import setup

VERSION = "0.0.1"

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="fast_docker_web",
    version=VERSION,
    description="Wrapps the php web code with Docker environment",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="Docker web php development",
    url="https://github.com/danilocgsilva/fast-docker-web",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["fast_docker_web"],
    entry_points={"console_scripts": ["fdocker=fast_docker_web.__main__:main"],},
    include_package_data=True
)

