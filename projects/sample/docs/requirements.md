# Project Requirements

## Overview
This mounting plate sample project demonstrates a parametric CAD implementation using Python and build123d. The design includes a rounded rectangular plate with four countersunk mounting holes.

## Functional Requirements

### Primary Requirements
- **Parametric Design**: All dimensions should be configurable parameters
- **Export Functionality**: Generate both STEP and STL files
- **Testing**: Implement comprehensive test coverage
- **Documentation**: Provide complete documentation for future projects

### Technical Requirements
- **Units**: Use millimeters as the standard unit system
- **Validation**: Verify geometry validity and test expected outputs
- **Documentation**: Maintain clear documentation of design decisions
- **Maintainability**: Code should be readable and maintainable

## Design Parameters

| Parameter | Description | Unit | Default Value | Testable |
|-----------|-------------|------|----|--------------|----------|
| LENGTH | Plate length | mm | 100.0 | ✅ Yes |
| WIDTH | Plate width | mm | 60.0 | ✅ Yes |
| THICKNESS | Plate thickness | mm | 8.0 | ✅ Yes |
| CORNER_RADIUS | Fillet radius on corners | mm | 3.0 | ✅ Yes |
| EDGE_OFFSET | Distance from edge to hole center | mm | 10.0 | ✅ Yes |
| HOLE_DIAMETER | Mounting hole diameter | mm | 5.0 | ✅ Yes |
| SINK_DIAMETER | Countersink diameter | mm | 9.0 | ✅ Yes |
| SINK_ANGLE | Countersink angle | degrees | 90.0 | ✅ Yes |

### Parameter Dependencies
- **CORNER_RADIUS**: Must be less than min(LENGTH, WIDTH) / 2
- **EDGE_OFFSET**: Must be less than min(LENGTH, WIDTH) / 2
- **HOLE_DIAMETER**: Must be less than SINK_DIAMETER
- **All parameters**: Must be positive values

### Design Constraints
- **Material**: PLA (3D printing filament)
- **Wall Thickness**: Minimum 8mm plate thickness
- **Fastener Standards**: M4/M5 compatibility for 5mm holes
- **Manufacturing**: 3D printing with minimum wall thickness requirements

## Interface Requirements

### Mounting Points
Four symmetrically arranged mounting holes:
- Positions calculated as: (±(LENGTH/2 - EDGE_OFFSET), ±(WIDTH/2 - EDGE_OFFSET))
- Total of 4 mounting points
- Countersunk for flush mounting

### Fastener Compatibility
- **Primary**: M4 or M5 flat-head screws
- **Hole Diameter**: 5mm (clearance fit)
- **Countersink**: 9mm diameter at 90° angle
- **Thread Standards**: Metric UNC/UNF compatibility

## Acceptance Criteria

### Functionality
- [x] Geometry validates and is non-empty
- [x] Solid count is exactly 1
- [x] Volume calculation correct (1,200,000 mm³)
- [x] Bounding box dimensions correct (100 × 60 × 8 mm)
- [x] Hole positions calculated correctly
- [x] Corner fillets applied correctly

### Quality Assurance
- [x] All pytest tests pass
- [x] Code linting passes with ruff
- [x] No undefined variables or syntax errors
- [x] Documentation complete and clear

### Export Requirements
- [x] STEP file generated and non-empty (> 50KB)
- [x] STL file generated and non-empty (> 200KB)
- [x] Export tolerance within acceptable limits
- [x] File naming conventions followed

## Research Requirements

### Required Documentation
- CAD framework documentation (build123d API verification)
- Testing framework documentation (pytest setup)
- Building instructions for development environment
- License and attribution requirements
- Dependencies and requirements documentation

### External References
- build123d library documentation
- OCP CAD Viewer integration
- Python 3.14 development environment
- Windows PowerShell compatibility

## Design Notes

### Implementation Approach
1. **Parameter System**: All design parameters are configurable constants
2. **Validation**: Comprehensive input validation for all parameters
3. **Geometry Generation**: BuildPart context for structured model creation
4. **Testing**: Unit tests for functionality and parameter validation
5. **Export**: Standardized export to STEP and STL formats

### Engineering Considerations
- **Printability**: Minimum wall thickness requirements
- **Assembly**: Tool access for countersunk screw installation
- **Accuracy**: Floating-point tolerance handling
- **Maintainability**: Clear parameter naming and documentation

### Risk Mitigation
- **Path Resolution**: Ensure exports go to correct directory
- **Parameter Validation**: Prevent invalid parameter combinations
- **Test Coverage**: Comprehensive testing for all functionality
- **Documentation**: Complete documentation for future developers

## Milestones

### Phase 1: Foundation
- [ ] Set up development environment
- [ ] Implement basic parameter system
- [ ] Create initial test framework
- [ ] Establish documentation structure

### Phase 2: Core Implementation
- [ ] Implement geometry generation
- [ ] Add hole and countersink features
- [ ] Implement export functionality
- [ ] Run initial tests

### Phase 3: Quality Assurance
- [ ] Complete test coverage
- [ ] Implement linting and formatting
- [ ] Document design decisions
- [ ] Validate final implementation

## Open Questions

1. **Target Application**: Is this a general mounting plate template or specific to Flydigi Apex 4 controller?
2. **Manufacturing Process**: Is this for 3D printing (PLA), CNC, or another process?
3. **Load Requirements**: What loads will the mounting plate support?
4. **Fastener Specification**: What screw size/type is intended for the 5mm holes? (M3, M4, M5?)
5. **Thermal Considerations**: Any thermal management requirements?