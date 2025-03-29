from setuptools import setup, find_packages

setup(
    name="colabcode",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyngrok",
        "PyYAML",
        "nest_asyncio",
        "uvicorn",
    ],
    scripts=["scripts/colabcode"],
    author="Akram BEN GHANEM",
    author_email="akrambenghanem76@gmail.com",
    description="Run VS Code on Colab/Kaggle Notebooks",
    keywords="colab, vscode, kaggle",
    url="https://github.com/yourusername/colabcode",
)