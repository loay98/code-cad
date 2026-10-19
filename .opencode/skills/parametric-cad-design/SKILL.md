# Parametric CAD Design Skill: parametric-cad-design

## Purpose
**Goal**: Design maintainable, parametric mechanical CAD models using the project's established development framework and build123d where appropriate.

### When to Use
- Developing new parametric CAD components
- Modifying existing design parameters
- Creating reusable geometry and models
- Establishing design documentation and standards
- Validating geometry and interfaces

### Prerequisites
- Familiarity with build123d and Open CASCADE (OCCT) APIs
- Understanding of parametric design principles
- Access to project's existing source code and tests
- Ability to read and follow project documentation
- Experience with pytest and testing frameworks

### Procedure

#### Step 1: Understand Project Requirements
1. **Read Project Context**: Consult AGENTS.md, MEMORY.md, and relevant source files
2. **Identify Requirements**: Extract functional and mechanical requirements
3. **Review Existing Code**: Understand current implementation and design decisions
4. **Check Design Standards**: Review project's engineering rules and constraints
5. **Establish Scope**: Define project boundaries and design parameters

#### Step 2: Parameter Design
1. **Define Parameters**: Create comprehensive parameter table with units and constraints
2. **Establish Dependencies**: Identify parameter relationships and dependencies
3. **Parameter Validation**: Implement parameter validation logic
4. **Documentation**: Document all parameters with descriptions and constraints
5. **Default Values**: Set reasonable default values based on requirements

#### Step 3: Geometry Generation
1. **Function Organization**: Structure geometry generation in testable functions
2. **Component Design**: Design individual components with clear interfaces
3. **Assembly Design**: Create assembly relationships and interfaces
4. **Manufacturing Constraints**: Consider PLA limitations and manufacturing requirements
5. **Quality Assurance**: Implement quality checks and validation

#### Step 4: Implementation
1. **Code Structure**: Organize code into logical modules and functions
2. **Testing Integration**: Integrate with existing test suite
3. **Validation**: Implement validation for geometry and interfaces
4. **Documentation**: Add comprehensive documentation for all components
5. **Error Handling**: Implement robust error handling for edge cases

#### Step 5: Documentation and Validation
1. **Code Documentation**: Document code with clear explanations
2. **Design Documentation**: Document design decisions and rationale
3. **Testing Documentation**: Document test cases and expected results
4. special attention to ensuring documentation is clear, comprehensive, and maintainable.

### Key Principles
- **Parametric Approach**: All design elements are configurable through named parameters
- **Maintainability**: Code should be easy to understand, modify, and extend
- **Testability**: All functionality should be covered by comprehensive tests
- **Evidence-Based**: All dimensions and design decisions backed by verified information
- **Project Standards**: Follow project's established engineering rules and conventions
- **Quality Assurance**: Implement robust validation and quality checks

### Success Criteria
- ✅ Parameter system is comprehensive and well-documented
- ✅ Geometry generation functions are modular and testable
- ✅ Parameter validation logic prevents invalid parameter combinations
- ✅ Design documentation is complete and clear
- ✅ Tests cover all functionality and edge cases
- ✅ Code follows project coding standards

### Tools and Resources
- **Development Environment**: Python 3.14, build123d, Open CASCADE
- **Testing Framework**: pytest for unit and integration tests
- **Linting**: ruff for code quality and formatting
- **Documentation**: Markdown for documentation files
- **CAD Viewer**: ocp-vscode for visualization

### Integration with Other Skills
- **cad-research**: Use researched dimensions and requirements for design parameters
- **cad-validation**: Implement validation tests for geometry and interfaces
- **cad-documentation**: Document design decisions and parameter relationships
- **pla-design-review**: Review designs for 3D printing manufacturability
- **cad-ci-troubleshooting**: Troubleshoot and validate CI/CD pipeline failures

### Skill Usage Example
```
# Example usage of parametric-cad-design skill
Use parametric-cad-design to create a mounting plate:

Design parameters:
- LENGTH: 100.0 mm (from specification)
- WIDTH: 60.0 mm (from specification)
- THICKNESS: 8.0 mm (from specification)
- CORNER_RADIUS: 3.0 mm (from specification)
- EDGE_OFFSET: 10.0 mm (from specification)
- HOLE_DIAMETER: 5.0 mm (from specification)

Requirements:
- Four countersunk mounting holes
- Round corners for stress reduction
- PLA manufacturable (minimum wall thickness 8mm)
- Export STEP and STL formats
```

### Quality Assurance
- **Parameter Validation**: Comprehensive parameter validation with clear error messages
- **Geometry Validation**: Robust geometry validation and quality checks
- **Interface Compatibility**: Ensure compatibility with assembly interfaces
- **Testing**: Comprehensive test coverage for all functionality
- **Documentation**: Complete documentation for all parameters and components

### Common Challenges
- **Parameter Dependencies**: Complex parameter relationships
- **Geometry Validation**: Complex geometry operations and validation
- **Manufacturing Constraints**: Balancing design requirements with manufacturing limitations
- **Documentation**: Maintaining comprehensive documentation while avoiding redundancy

### Best Practices
- Use descriptive parameter names with units
- Implement comprehensive parameter validation
- Organize code into logical modules and functions
- Document all design decisions and assumptions
- Ensure robust error handling for edge cases
- Follow project's coding standards and conventions
- Implement comprehensive test coverage
- Maintain consistent code formatting and style

---

**Note**: This skill focuses on creating robust, maintainable parametric CAD designs that can be easily tested, documented, and extended. The emphasis is on creating modular, reusable components that support the project's engineering requirements while maintaining code quality and maintainability.