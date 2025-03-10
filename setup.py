from setuptools import setup, find_packages

setup(
    name="hyperrequest",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],
    author="speedrunblaze",
    description="An optimized request manager that automatically handles errors, retries, and anti-flood mechanisms.",
    url="https://github.com/speedrunblaze/hyperrequest",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
