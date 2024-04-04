from setuptools import setup, find_packages

setup(
    name='booklover',  # The package name
    version='0.1',  # The initial release version
    author='Your Name',  # Replace with your name
    author_email='your.email@example.com',  # Replace with your email address
    description='A package for book collection management and preference tracking',  # Package description
    packages=find_packages(),  # Automatically find package directories
    install_requires=[
        'pandas>=1.0.0',  # Specify your dependencies here; ensure you include pandas
    ],
    classifiers=[
        # Classifiers help users find your project by categorizing it.
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the minimum version of Python required
)
