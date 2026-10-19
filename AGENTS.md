
# Project Instructions: Programmatic CAD

## Mission
Create parametric mechanical CAD using Python and build123d.
Source code is authoritative; STEP and STL files are generated outputs.

## Technology
- Python 3.14, where supported by installed dependencies.
- build123d and Open CASCADE (OCCT).
- ocp-vscode for interactive 3D preview.
- pytest for tests and ruff for linting.
- Windows PowerShell is the default shell.

## Engineering rules
- Use millimeters for all dimensions.
- Give design parameters descriptive names and units in comments.
- Keep geometry generation in functions that can be tested.
- Prefer explicit imports over wildcard imports.
- Separate reusable geometry from individual models.
- Derive dependent dimensions from source parameters.
- Validate inputs before creating geometry.
- Avoid unexplained numeric literals in geometry operations.
- Use build123d APIs verified against the installed version.
- Do not invent API methods; inspect documentation or test examples.

## Geometry validation
- Check that generated solids are valid and non-empty.
- Check expected bounding boxes, hole positions and solid counts.
- Use tolerances for floating-point comparisons.
- Validate that STEP and STL exports exist and are non-empty.
- Do not claim a design is manufacturable merely because it renders.
- Flag uncertain fits, wall thicknesses, tolerances and fastener standards.
- Never silently change user-specified dimensions.

## Workflow
1. Inspect the existing project before changing files.
2. Explain your implementation plan for complex changes.
3. Make small, reversible changes.
4. Run pytest and ruff after relevant changes.
5. Run the model-generation script and inspect errors.
6. Export STEP and STL into build/, never into source directories.
7. Report commands executed, test results and remaining limitations.

## Commands
- Tests: .venv\Scripts\python.exe -m pytest
- Lint: .venv\Scripts\python.exe -m ruff check .
- Preview/build: run the relevant model script using the project interpreter.

## Git
- Never overwrite user work without checking the diff.
- Do not commit generated build artifacts by default.
- Do not commit secrets, API keys or virtual environments.
- Keep AGENTS.md and dependency configuration under version control.
