# Textual Game of Life

Game of Life with Textual UI

## Development Environment Setup

Setup the virtual environment for python before changing files. If you use [direnv](https://github.com/direnv/direnv/wiki/Python), the virtual environment is created and / or activated automatically whenver you enter the working directory.

```shell
python -m venv ./venv
source ./venv/bin/activate
```

In a fresh virtual environment, install dependencies and build tools once:

```
pip install -r requirements.txt
pre-commit install
```

## Testing

```shell
pytest
```

## Debugging

Textual comes with a debug console. To connect it to the application, execute the following steps:

1. In a fresh terminal window, run the console: `textual console -x SYSTEM -x EVENT -x WORKER`

2. In another terminal window, run this app in development mode: `textual run --dev src/game_app/game_app.py`

## Committing changes

[Pre-commit](https://pre-commit.com/) is used to run code quality checks and formatters automatically before you are allowed to commit. If the tool reports an error, you can inspect the changes it suggests using `git diff`.

## References

(1) Textualize Inc, “Textualize.” Accessed: Aug. 09, 2025. [Online]. Available: [https://www.textualize.io/](https://www.textualize.io/)

(2) W. McGugan and G. Kampfhammer, _SE Radio 669: Will McGugan on Text-Based User Interfaces_. 2025. Accessed: Aug. 09, 2025. [Online]. Available: [https://se-radio.net/2025/05/se-radio-669-will-mcgugan-on-text-based-user-interfaces/](https://se-radio.net/2025/05/se-radio-669-will-mcgugan-on-text-based-user-interfaces/)
