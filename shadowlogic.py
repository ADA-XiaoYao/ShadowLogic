#!/usr/bin/env python3
import sys
import os

# 将 src 目录添加到 Python 路径中
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.cli import cli

if __name__ == '__main__':
    cli()
