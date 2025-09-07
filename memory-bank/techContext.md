# Technical Context: Textual Game of Life

## Technology Stack

### Core Framework

**Textual 0.x**

- **Purpose**: Rich terminal user interface framework
- **Capabilities**: Widgets, layouts, styling, event handling
- **Benefits**: Modern terminal UI without browser or native GUI overhead
- **Documentation**: https://textual.textualize.io/

### Python Environment

**Python 3.13+**

- **Version requirement**: Latest Python for modern language features
- **Package management**: Using standard pip and requirements.txt
- **Build system**: Hatchling for modern Python packaging

### Development Tools

**Testing**

- **pytest**: Primary testing framework
- **pytest-textual-snapshot**: Specialized testing for Textual apps
- **Coverage**: Built into pytest configuration

**Code Quality**

- **pre-commit**: Automated code quality checks before commits
- **Formatting/Linting**: Configured via pre-commit hooks
- **Import mode**: `importlib` for modern Python import handling

**Debugging**

- **textual console**: Built-in debug console for live development
- **textual-dev**: Development tools and utilities
- **Log widget**: In-app logging for development visibility

## Development Setup

### Environment Management

**Virtual Environment**

```bash
python -m venv ./venv
source ./venv/bin/activate  # Linux/Mac
```

**Direnv Integration**

- `.envrc` file present for automatic environment activation
- Seamless virtual environment management when entering directory

### Dependencies Installation

**Initial Setup**

```bash
pip install -r requirements.txt
pre-commit install
```

**Key Dependencies**:

- `textual`: Core UI framework
- `textual-dev`: Development tools
- `pytest-textual-snapshot`: UI testing
- `pre-commit`: Quality automation

### Development Workflow

**Running the Application**

```bash
# Standard execution
python -m game_app.game_app

# Development mode with debug console
textual run --dev game_app.game_app:GameApp

# Debug console (separate terminal)
textual console -x SYSTEM -x EVENT -x WORKER
```

**Important**: The application must be run as a module (`python -m game_app.game_app`) rather than as a direct script. This is because:
- The package uses absolute imports (`from game_app.module import Class`)
- Running as a module ensures Python recognizes the package context
- Direct script execution (`python src/game_app/game_app.py`) fails with `ModuleNotFoundError`

**Testing**

```bash
pytest  # Run all tests
```

**Code Quality**

- Pre-commit hooks run automatically on `git commit`
- Manual run: `pre-commit run --all-files`

## Project Structure

### Source Organization

```
src/game_app/
├── __init__.py          # Package initialization
├── game_app.py          # Main application entry point
├── universe_view.py     # Abstract view interface
├── textual_universe_view.py  # Textual-specific view implementation
├── universe_presenter.py     # Business logic coordinator
└── cell.py             # Core data structure
```

### Configuration Files

- **pyproject.toml**: Modern Python project configuration
- **requirements.txt**: Runtime and development dependencies
- **.pre-commit-config.yaml**: Code quality automation
- **.envrc**: Direnv environment setup
- **.gitignore**: Version control exclusions

## Technical Constraints

### Python Version

- **Minimum**: Python 3.13+
- **Reason**: Latest language features and performance improvements
- **Impact**: Users must have modern Python installation

### Terminal Requirements

- **Unicode support**: For █ character rendering
- **Color capability**: For theme switching (dark/light)
- **Keyboard input**: For interactive controls (d, n, r keys)

### Performance Considerations

- **Terminal rendering**: Limited by terminal refresh capabilities
- **Memory usage**: Minimal for typical Game of Life patterns
- **CPU usage**: Low for generation calculations

## Deployment Context

### Target Environments

- **Development**: Local terminal with full debugging support
- **Education**: Student environments with basic Python 3.13+
- **Demonstration**: Terminal presentations and code reviews

### Installation Methods

- **Source**: Git clone and pip install requirements
- **Package**: Future PyPI distribution possible
- **Containerization**: Docker for consistent environments

## Future Technical Considerations

### Planned Enhancements

- **TOML configuration**: Seed pattern loading from files
- **Universe model**: Proper Game of Life rule implementation
- **Performance optimization**: Efficient neighbor calculation
- **Extended UI**: More interactive controls and visualization options
