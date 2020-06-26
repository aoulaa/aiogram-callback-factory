import setuptools

import aiogram_callback_factory


setuptools.setup(
    name="aiogram-callback-factory",
    version=aiogram_callback_factory.__version__,
    packages=setuptools.find_packages(),
    url="https://github.com/Abstract-X/aiogram-callback-factory",
    license="MIT",
    author="Abstract-X",
    author_email="abstract-x-mail@protonmail.com",
    description="Factory for servicing CallbackQuery in the Telegram bots.",
    install_requires=[
        "aiogram>=2.8,<3.0"
    ],
    include_package_data=False
)
