# Contributing to ModPocket

Thank you for your interest in contributing to ModPocket! This document provides guidelines for contributing to this monorepo project.

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ModPocket.git
   cd ModPocket
   ```
3. Install all packages in development mode:
   ```bash
   make install-dev
   ```

## Development Workflow

### Making Changes

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes in the appropriate package(s)

3. Test your changes:
   ```bash
   make test
   ```

4. Lint and format your code:
   ```bash
   make format
   make lint
   ```

5. Commit your changes:
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

6. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

7. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Use ruff for linting and formatting
- Add docstrings to all public functions and classes
- Keep functions focused and small

### Testing

- Write tests for all new features
- Ensure all tests pass before submitting a PR
- Aim for high test coverage

### Commit Messages

- Use clear, descriptive commit messages
- Start with a verb in present tense (Add, Fix, Update, etc.)
- Reference issue numbers when applicable

Example:
```
Add user authentication feature to API package

- Implement JWT token generation
- Add login and logout endpoints
- Update tests

Fixes #123
```

## Package-Specific Guidelines

### Core Package
- Contains fundamental functionality used by other packages
- Should have minimal external dependencies
- Changes here may affect all other packages

### Utils Package
- Utility functions and helpers
- Should be stateless and pure when possible
- Well-documented with usage examples

### API Package
- API interfaces and endpoints
- Should follow RESTful conventions
- Include comprehensive API documentation

## Pull Request Process

1. Update documentation to reflect changes
2. Add tests for new functionality
3. Ensure all tests pass
4. Update the package version if applicable
5. Request review from maintainers

## Questions or Issues?

- Open an issue for bugs or feature requests
- Use discussions for questions and general conversation

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.
