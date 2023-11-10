from setuptools import setup, find_packages

setup(
    name='openai-blog-updates',
    version='0.1.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'openai-blog-updates=blog_updates:main',
            ],
    },
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
)
