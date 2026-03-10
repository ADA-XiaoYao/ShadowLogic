from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="shadowlogic",
    version="0.1.0",
    author="ShadowLogic Team",
    author_email="team@shadowlogic.dev",
    description="A cutting-edge AI-powered penetration testing assistant tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ADA-XiaoYao/ShadowLogic",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Topic :: System :: Networking",
        "Topic :: Security",
    ],
    python_requires=">=3.9",
    install_requires=[
        "openai",
        "requests",
        "python-dotenv",
        "rich",
        "click",
        "pyyaml",
    ],
    entry_points={
        "console_scripts": [
            "shadowlogic=src.cli:cli",
        ],
    },
)
