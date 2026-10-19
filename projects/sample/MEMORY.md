# Sample Project Memory: Mounting Plate

## 1. Project Overview
- Project name: test_mounting_plate
- Purpose: Parametric mounting plate with four countersunk holes
- Current implementation: Working with known path resolution bug
- Location: D:\code-cad\projects\sample\

## 2. User Preferences
- Prefer code-first, parametric CAD
- Prefer maintainable geometry and reusable parameters
- Research existing designs and technical documentation before guessing dimensions
- Prefer evidence-backed measurements over visual estimates
- Explain limitations and unresolved risks honestly
- Avoid unnecessary rewrites of working code
- Use PowerShell-compatible commands when shell instructions are needed

## 3. Confirmed Technical Facts
| Fact | Value | Source | Evidence Type | Confidence |
|------|-------|--------|---------------|------------|
| CAD framework | build123d | Project configuration | File evidence | High |
| Available filament | PLA | User confirmation | Direct statement | High |

## 4. Design Decisions
For each significant decision, record:
- Date
- Decision
- Reason
- Alternatives considered
- Source or evidence
- Consequences for future work

## 5. Measurements and Research
For each important measurement, record:
- Parameter name
- Value and units
- Product/model/version, if applicable
- Source URL
- Evidence type
- Confidence level
- Whether physically verified

Never promote an estimate to a confirmed measurement without new evidence.

## 6. Known Problems and Lessons
Record:
- The problem encountered
- Relevant files or components
- Root cause, if confirmed
- The fix that worked
- Fixes that failed
- How to avoid repeating the issue

## 7. Current Project State
- **Current implementation**:
  - File: `src/models/mounting_plate.py` (93 lines)
  - Parameters: LENGTH=100.0mm, WIDTH=60.0mm, THICKNESS=8.0mm
  - Features: Rounded rectangular plate with four countersunk holes
  - Validation: pytest tests exist
  - Exports: STEP and STL files (path resolution issue)

- **Path resolution bug**: `parents[0]` should be `parents[2]` to export to correct location
- **Tests**: 2 basic tests implemented
- **Documentation**: Basic template structure
- **Current task**: Fix path resolution and update sample project documentation

## 8. Unresolved Questions
- **Target confirmation**: Is the intended project the generic mounting plate or a Flydigi Apex 4 articulated controller mount and cooler cradle?
- **Controller dimensions**: If Flydigi Apex 4, please provide controller dimensions, mounting hole locations, and cooling requirements
- **Fastener specification**: What screw size/type is intended for the 5mm holes? (M3, M4, M5?)
- **Manufacturing process**: Is this for 3D printing (PLA), CNC, or another process?
- **Load requirements**: What loads will the mount need to withstand?

## 9. Memory Maintenance Rules
- Read this file before planning or implementing substantial work
- Keep durable information, not a transcript of every conversation
- Update existing entries instead of creating duplicates
- Never invent facts, test results, measurements, or source URLs
- Clearly distinguish confirmed facts from assumptions
- Preserve important failed approaches so they are not repeated
- Record successful fixes only after verifying them
- Include file paths, parameter names, and reproducible steps when useful
- Do not overwrite a verified decision without explaining the reason
- Keep sensitive credentials, API keys, and secrets out of memory

## 10. Next Steps
1. **Fix path resolution** in mounting_plate.py:28 (`parents[0]` → `parents[2]`)
2. **Update sample project AGENTS.md** with comprehensive project instructions
3. **Update sample project MEMORY.md** with detailed current state
4. **Establish documentation structure** with docs/, references/, and decisions/
5. **Validate project structure** and report unresolved issues

## 11. Sample Project Implementation Status

### Files Status
- ✅ `src/models/mounting_plate.py` - Complete CAD implementation
- ✅ `tests/test_mounting_plate.py` - Complete test suite
- ✅ `src/models/build/` - Generated exports (61KB step, 253KB stl)
- ❌ `AGENTS.md` - Needs comprehensive project instructions
- ❌ `MEMORY.md` - Needs detailed project state documentation
- ❌ `docs/` - Needs documentation structure
- ❌ `references/` - Needs external references

### Critical Issues
1. **Path Resolution Bug**: Exports to wrong location (src/models/build/ instead of project root build/)
2. **Missing Documentation**: Incomplete sample project documentation
3. **Empty Instructions**: Project AGENTS.md and MEMORY.md need content
4. **Template Incompleteness**: Sample project not ready as a template

### Recommendations
1. Fix path resolution bug immediately
2. Populate AGENTS.md with project-specific instructions
3. Populate MEMORY.md with current implementation status
4. Establish complete documentation structure
5. Test the mounting plate implementation end-to-end
6. Validate exports and test suite
