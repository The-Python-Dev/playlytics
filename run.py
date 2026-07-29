"""
Playlytics - Game Performance Analyzer
by Orange Tabby Codes

Entry point. Run this file to start the app.

Usage:
    python run.py
"""

from app.ui.app import App


def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()