
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

## Collaboration Protocol

Before substantial planning or implementation:

1. Read `.opencode/AGENT_PROTOCOL.md` to understand workspace collaboration rules.
2. Identify the active project and load project context.
3. Follow established procedures for planning, implementation, and handoffs.
4. Update project memory after meaningful progress.
5. Review `.opencode/AGENT_PROTOCOL.md` for additional guidelines and procedures.

The protocol provides essential rules for agent roles, project loading, planning handoff, implementation handoff, memory management, documentation requirements, new project creation, and workspace write boundaries.