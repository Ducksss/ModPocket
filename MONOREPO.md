# ModPocket Monorepo Structure

This document explains the monorepo structure and how to work with it.

## What is a Monorepo?

A monorepo (monolithic repository) is a software development strategy where code for many projects is stored in the same repository. This approach offers several benefits:

- **Code Sharing**: Easy to share code between packages
- **Atomic Changes**: Make changes across multiple packages in a single commit
- **Unified Versioning**: Manage versions consistently across packages
- **Simplified Dependency Management**: All packages use the same dependency versions

## Repository Structure

```
ModPocket/
├── packages/               # All packages live here
│   ├── core/              # Core functionality
│   │   ├── modpocket_core/    # Python package
│   │   ├── pyproject.toml     # Package config
│   │   └── README.md          # Package docs
│   ├── utils/             # Utility functions
│   │   ├── modpocket_utils/
│   │   ├── pyproject.toml
│   │   └── README.md
│   └── api/               # API interfaces
│       ├── modpocket_api/
│       ├── pyproject.toml
│       └── README.md
├── scripts/               # Helper scripts
│   └── install-all.sh     # Install all packages
├── pyproject.toml         # Root configuration
├── Makefile              # Common tasks
└── README.md             # Main documentation
```

## Working with the Monorepo

### Installing Packages

**Install all packages in development mode:**
```bash
make install-dev
```

Or use the installation script:
```bash
./scripts/install-all.sh
```

**Install individual packages:**
```bash
pip install -e packages/core[dev]
pip install -e packages/utils[dev]
pip install -e packages/api[dev]
```

### Available Make Commands

- `make help` - Show available commands
- `make install` - Install all packages
- `make install-dev` - Install all packages with dev dependencies
- `make clean` - Remove build artifacts
- `make test` - Run tests for all packages
- `make lint` - Lint all packages with ruff
- `make format` - Format all packages with ruff

### Adding a New Package

1. Create a new directory under `packages/`:
```bash
mkdir -p packages/newpackage/modpocket_newpackage
```

2. Create the package's `__init__.py`:
```python
"""ModPocket New Package."""

__version__ = "0.1.0"
```

3. Create `pyproject.toml`:
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "modpocket-newpackage"
version = "0.1.0"
description = "Description of the new package"
readme = "README.md"
requires-python = ">=3.8"
authors = [
    {name = "ModPocket Team"}
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "ruff>=0.1.0",
]
```

4. Create a `README.md` for the package

5. Update the root `Makefile` to include the new package

6. Install the package:
```bash
pip install -e packages/newpackage[dev]
```

### Cross-Package Dependencies

To use one package in another, add it as a dependency in the `pyproject.toml`:

```toml
[project]
dependencies = [
    "modpocket-core>=0.1.0",
]
```

Then install both packages in development mode:
```bash
pip install -e packages/core
pip install -e packages/dependent-package
```

### Testing

Run tests for all packages:
```bash
make test
```

Or run tests for a specific package:
```bash
pytest packages/core/
```

### Code Quality

**Linting:**
```bash
make lint
```

**Formatting:**
```bash
make format
```

## Best Practices

1. **Keep packages focused**: Each package should have a single, well-defined purpose
2. **Minimize cross-package dependencies**: Reduces coupling and makes packages more reusable
3. **Use consistent naming**: Follow the `modpocket_*` naming convention
4. **Document changes**: Update package READMEs when adding new features
5. **Test thoroughly**: Ensure changes don't break other packages
6. **Version together**: Consider versioning all packages together for simplicity

## Troubleshooting

**Import errors after installation:**
- Ensure you're in the correct virtual environment
- Try reinstalling the package: `pip install -e packages/packagename --force-reinstall`

**Make commands fail:**
- Ensure you have all required dependencies installed
- Check that you're in the repository root directory

**Package not found:**
- Verify the package structure matches the expected format
- Check that the package name in `pyproject.toml` matches the directory name
