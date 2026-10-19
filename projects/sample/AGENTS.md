# Sample Project Instructions: Programmatic CAD

## Mission
This is the first sample project template for the multi-project CAD workspace. It provides a complete, working example of a parametric mounting plate with the following characteristics:

- Parametric design using Python and build123d
- Generated STEP and STL files
- Comprehensive test coverage
- Documentation structure for future projects

## Technology
- Python 3.14, where supported by installed dependencies
- build123d and Open CASCADE (OCCT)
- ocp-vscode for interactive 3D preview
- pytest for tests and ruff for linting
- Windows PowerShell is the default shell

## Engineering Rules
- Use millimeters for all dimensions
- Give design parameters descriptive names and units in comments
- Keep geometry generation in functions that can be tested
- Prefer explicit imports over wildcard imports
- Separate reusable geometry from individual models
- Derive dependent dimensions from source parameters
- Validate inputs before creating geometry
- Avoid unexplained numeric literals in geometry operations
- Use build123d APIs verified against the installed version
- Do not invent API methods; inspect documentation or test examples

## Geometry Validation
- Check that generated solids are valid and non-empty
- Check expected bounding boxes, hole positions and solid counts
- Use tolerances for floating-point comparisons
- Validate that STEP and STL exports exist and are non-empty
- Do not claim a design is manufacturable merely because it renders
- Flag uncertain fits, wall thicknesses, tolerances and fastener standards
- Never silently change user-specified dimensions

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

## Persistent Project Memory
Before substantial planning, research, or implementation:

1. Read `.opencode/MEMORY.md`.
2. Check relevant source files and tests to confirm whether stored information remains accurate.
3. Reuse existing verified decisions and avoid repeating failed approaches.
4. Identify any conflicts between stored memory and the current code or user requirements. Current verified evidence takes precedence over stale memory.

After completing substantial work:

1. Identify durable facts, successful fixes, important decisions, new measurements, and unresolved problems worth preserving.
2. Propose concise updates to `.opencode/MEMORY.md`.
3. Include source URLs and confidence levels for researched measurements.
4. Record test results only when the commands were actually executed and their results observed.
5. Never record assumptions as confirmed facts.

The planner must include proposed memory updates in its final report. The implementation agent must apply approved updates to the memory file after implementation and verification.

## Project Details
- Project name: test_mounting_plate
- Purpose: Parametric mounting plate with four countersunk holes
- Current state: Working implementation with path resolution bug to be fixed

## Relationship to Root Instructions
- Root instructions apply to all projects
- This project-specific instructions override root when conflicts occur
- Workspace memory contains reusable workspace-level information
- Project memory contains this project's specific information
- Agents must read both root and project instructions before work

## Sample Project Overview
This mounting plate sample demonstrates:

### Design Parameters
- **Length**: 100.0 mm (testable parameter)
- **Width**: 60.0 mm (testable parameter)
- **Thickness**: 8.0 mm (testable parameter)
- **Corner Radius**: 3.0 mm (testable parameter)
- **Hole Edge Offset**: 10.0 mm (testable parameter)
- **Hole Diameter**: 5.0 mm (testable parameter)
- **Countersink Diameter**: 9.0 mm (testable parameter)
- **Countersink Angle**: 90.0° (testable parameter)

### Current Implementation Status
- **Geometry**: Complete - rounded rectangular plate with four countersunk holes
- **Tests**: 2 basic tests implemented
- **Exports**: STEP and STL files generated (path resolution issue)
- **Path Bug**: `parents[0]` should be `parents[2]` to export to correct location
- **Documentation**: Basic template structure with incomplete implementation

### Sample Project Files
- `src/models/mounting_plate.py` - CAD implementation
- `tests/test_mounting_plate.py` - Test suite
- `src/models/build/` - Generated exports
- `AGENTS.md` - Project instructions
- `MEMORY.md` - Project memory
- `docs/` - Documentation structure
- `references/` - External references
- `projects/sample/` - Template for new projects

### Path Resolution Issue
The mounting_plate.py file has a path resolution bug where it exports to `src/models/build/` instead of the project root's `build/` directory. This should be fixed by changing `parents[0]` to `parents[2]` in line 28.