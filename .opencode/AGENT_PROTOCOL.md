# Agent Collaboration Protocol

## 1. Overview

The OpenCode workspace supports multiple independent mechanical CAD projects using Python and build123d. This protocol establishes consistent collaboration rules, project isolation, and workflows for all planners, implementers, reviewers, and workspace-maintenance agents.

**Workspace Scope**: This workspace manages multiple CAD projects, each with independent:
- Project-specific instructions and memory
- Source code and tests
- Documentation and references
- Build outputs and results

**Key Principle**: Workspace-wide rules apply to all projects, but each project maintains autonomy in its requirements, decisions, and implementation.

---

## 2. Agent Roles and Responsibilities

### 2.1 Core Agent Roles

| Agent | Role | Primary Scope | Key Responsibilities |
|-------|------|--------------|---------------------|
| **workspace-architect** | Workspace maintainer | Workspace structure, configuration, templates | Project scaffolding, memory management, Git workflow |
| **plan** | Engineering planner | Requirements, research, implementation orchestration | Evidence-based research, planning, approval handoffs |
| **cad-implementer** | Implementation specialist | Approved CAD work execution | Parametric modeling, validation, exports |
| **cad-planner-backup** | Planning reviewer | Independent verification | Requirements validation, conflict detection |
| **cad-vision-aldistinct** | Visual reviewer | Visual interpretation | Image analysis, spatial assessment |
| **cad-gemma-backup** | Alternative planning | Independent planning review | Requirements verification, design critique |

### 2.2 Role-Specific Responsibilities

#### workspace-architect
- **Workspace Structure**: Maintain multi-project organization and isolation
- **Project Templates**: Establish reusable project scaffolding
- **Configuration Management**: Update workspace-wide instructions and protocols
- **Git Workflow**: Define project branching and publication rules
- **Memory Management**: Separate workspace vs. project memory
- **Documentation**: Establish project documentation standards

#### plan
- **Requirements Analysis**: Gather and document project requirements
- **Research**: Conduct evidence-based technical research
- **Planning**: Develop implementation plans with measurable acceptance criteria
- **Coordination**: Delegate work to implementers with approved plans
- **Validation**: Review implementation results against requirements

#### cad-implementer
- **Implementation**: Execute approved parametric CAD designs
- **Validation**: Test geometry, interfaces, and exports
- **Documentation**: Update project memory and documentation
- **Quality Assurance**: Run tests, linting, and formatting

#### cad-planner-backup, cad-vision-alternative, cad-gemma-backup
- **Review**: Independently verify planning and implementation
- **Risk Assessment**: Identify potential issues and conflicts
- **Validation**: Check against requirements and evidence
- **Recommendations**: Provide alternative approaches and corrections

---

## 3. Project Context Loading Procedure

Before starting work on a project, every agent must:

### 3.1 Load Context in Order

1. **Identify Active Project**
   - Determine the current project by examining `projects/` directory
   - Locate the project's root directory under `projects/`

2. **Load Workspace Context**
   - Read root `AGENTS.md` for workspace-wide rules
   - Read `.opencode/AGENT_PROTOCOL.md` for collaboration rules
   - Read root `.opencode/MEMORY.md` for shared workspace information
   - Read `opencode.json` for current agent permissions

3. **Load Project Context**
   - Read project `projects/<project-name>/AGENTS.md` for project-specific instructions
   - Read project `projects/<project-name>/MEMORY.md` for project state
   - Read relevant source files, tests, and documentation

4. **Validate Information**
   - Verify critical measurements against actual files
   - Check memory consistency with current files
   - Confirm evidence sources and confidence levels

### 3.2 Information Handling Guidelines

#### Project Isolation
- Keep project-specific facts separate from workspace knowledge
- Do not assume switching projects transfers conversation history
- Use persistent files for handoffs between different projects
- Clearly distinguish verified facts, user requirements, assumptions, and unresolved questions

#### Evidence-Based Decision Making
- All dimensions must be evidence-backed or explicitly marked as assumptions
- Source URLs and evidence types must be cited for research-based information
- Unresolved dimensions must be clearly identified and addressed with the user

---

## 4. Planning and Implementation Handoff

### 4.1 Planner to Implementer Handoff

The planner submits the following information to the implementer:

**Project Identification**
- Active project name and absolute or workspace-relative path
- Current project status and context

**Requirements and Constraints**
- Functional and mechanical requirements
- Design parameters with units
- Material and manufacturing constraints
- Tolerance and clearance requirements

**Evidence and Research**
- Source URLs for critical measurements
- Evidence type (drawing, CAD measurement, specification, etc.)
- Confidence levels for researched information

**Implementation Plan**
- Approved engineering specifications
- Part relationships and dependencies
- Construction sequence and approach
- Validation procedures

**Acceptance Criteria**
- Measurable test requirements
- Geometry validation criteria
- Export and documentation requirements
- Quality and accuracy standards

### 4.2 Implementer Verification

The implementer must:

1. **Inspect Current State**
   - Read the approved plan
   - Inspect relevant source files and tests
   - Verify project memory and current implementation

2. **Execute Implementation**
   - Follow the approved plan exactly
   - Preserve existing functionality
   - Validate geometry and interfaces
   - Run tests and validation procedures

3. **Report Results**
   - Document files changed
   - Record decisions or deviations
   - Report commands actually executed
   - Document test results and validation outcomes
   - Identify known issues and remaining work

### 4.3 Planner Review

The planner reviews the implementation:

1. **Compare Against Plan**
   - Verify scope compliance
   - Check for unauthorized changes
   - Validate test results against acceptance criteria

2. **Request Corrections**
   - If issues are found, provide detailed feedback
   - Specify expected outcomes and validation methods
   - Document any scope adjustments

3. **Update Memory**
   - Record successful implementation
   - Document any lessons learned
   - Update project memory with verified results

---

## 5. Memory Ownership and Updates

### 5.1 Memory Management Principles

#### Workspace Memory (`.opencode/MEMORY.md`)
- **Owner**: workspace-architect
- **Content**: Reusable workspace-level knowledge
- **Updates**: workspace-architect only
- **Purpose**: Shared lessons and technical guidance

#### Project Memory (`projects/<project>/MEMORY.md`)
- **Owner**: Project team (workspace-architect, planners, implementers)
- **Content**: Project-specific verified information
- **Updates**: Project team members with appropriate permissions
- **Purpose**: Current project state and decisions

### 5.2 Update Procedures

#### Updating Project Memory
1. **Identify Relevant Changes**
   - New verified measurements
   - Successful implementations
   - Important engineering decisions
   - Known issues and lessons learned

2. **Update Memory File**
   - Read current memory for context
   - Add or update entries with evidence
   - Maintain existing entries when possible
   - Record verification status clearly

3. **Maintain Memory Quality**
   - Distinguish facts from assumptions
   - Cite sources for researched information
   - Record verification methods and results
   - Preserve historical decisions when superseded

#### Updating Workspace Memory
1. **Workspace-Level Changes**
   - New workspace procedures
   - Updated collaboration rules
   - Shared technical lessons
   - Changes affecting multiple projects

2. **Coordination Required**
   - Report changes to workspace-architect
   - Ensure all agents can update their memory
   - Validate new information against current files

### 5.3 Memory Update Protocol

#### Required Information for Memory Updates
- **Verification**: Commands actually executed and their results
- **Source URLs**: For researched measurements and references
- **Confidence Levels**: For estimates and evidence-based information
- **File Paths**: Parameter names and reproducible steps

#### Update Restrictions
- **No Unverified Assumptions**: Never record assumptions as confirmed facts
- **Evidence Required**: All claims must have supporting evidence
- **Consistent Format**: Follow established memory structure
- **Preserve Context**: Maintain existing entries when possible

---

## 6. CAD Documentation Procedures

### 6.1 Documentation Structure

Every substantial CAD planning task must produce documentation in the active project's `docs/` directory:

**Required Documents**:
1. **docs/requirements.md** - Functional requirements and constraints
2. **docs/research.md** - Researched designs, measurements, product references
3. **docs/design.md** - Selected architecture and part relationships
4. **docs/testing.md** - Validation plans and actual test results
5. **docs/parts-and-measurements.md** - Planning format for parts and measurements
6. **docs/decisions/** - Individual engineering decision records

### 6.2 Parts and Measurements Format

For every proposed or selected part, record:

| Field | Description |
|-------|-------------|
| **Part Name** | Descriptive identifier and purpose |
| **Status** | proposed, researched, selected, designed, printed, validated |
| **Dimensions** | Value and units with evidence source |
| **Dimension Type** | source-confirmed, measured, calculated, estimated, unknown |
| **Tolerances/Clearances** | Fit requirements and interfaces |
| **Material Constraints** | Manufacturing and material limitations |
| **Source** | URL or documentation reference |
| **Confidence** | High, medium, low |
| **Dependencies** | Required relationships with other parts |
| **Acceptance Criteria** | Validation methods and expected results |

**Evidence Table**:
| Parameter | Value and units | Source | Evidence type | Confidence |
|-----------|----------------|--------|---------------|------------|
| Example: mounting-hole spacing | Verified value or unknown | Source URL | Drawing, CAD measurement, specification | High, medium, or low |

### 6.3 Decision Records

Each decision record must contain:

| Field | Description |
|-------|-------------|
| **Decision ID** | Unique identifier |
| **Title** | Brief description of decision |
| **Date** | Decision date |
| **Context** | Background and constraints |
| **Options** | All alternatives considered |
| **Selected Decision** | Chosen option |
| **Rationale** | Why this option was selected |
| **Consequences** | Impact and trade-offs |
| **Evidence** | Supporting sources and measurements |
| **Review Conditions** | Criteria for revisiting the decision |

---

## 7. New Project Creation and Git Procedures

### 7.1 Project Creation Workflow

1. **Confirm New Project**
   - Verify project name and purpose
   - Ensure no naming conflicts

2. **Establish Project Directory**
   - Create `projects/<new-project-name>/` directory
   - Set appropriate directory structure

3. **Copy Project Template**
   - Copy sample project files and directories
   - Remove sample-specific information
   - Update project name and requirements

4. **Adapt Template Content**
   - Replace sample project names with new project name
   - Update design parameters and requirements
   - Remove or adapt sample-specific references

5. **Establish Git Branch**
   - Check current Git status
   - Create new branch: `project/<new-project-name>`
   - Add files to staging
   - Commit initial project setup

6. **Verify Project Structure**
   - Check all required directories and files
   - Validate project configuration
   - Test project build and generation

### 7.2 Git Workflow Rules

#### Branch Strategy
- **Project Isolation**: Each project uses its own branch
- **Branch Naming**: `project/<project-name>` convention
- **Feature Branches**: Use descriptive branch names for specific features
- **Release Branches**: Use stable branches for final implementations

#### Publication Guidelines
- **Local Development**: Work on local branches for development
- **Review Process**: Create pull requests for code review
- **Publication**: Require approval before pushing to remote
- **Backup**: Maintain multiple branch strategies for project versions

#### Safety Precautions
- **Never Silently Switch Branches**: Always verify uncommitted changes
- **Never Discard Changes**: Never lose user work without checking diffs
- **Git Safety**: Always inspect the current branch and working tree
- **Explicit Confirmation**: Always ask for confirmation before publishing

---

## 8. Workspace Write Boundary Enforcement

### 8.1 Permission Verification

#### Workspace-Protected Files
- Root `AGENTS.md`
- Root `opencode.json`
- Root `.opencode/` directory
- Project templates in `projects/` (scaffolding only)

#### Project-Writable Files
- `projects/<project-name>/` directory and subdirectories
- All project-specific source code
- Project documentation and tests
- Generated project outputs

### 8.2 Agent Permission Enforcement

#### workspace-architect Permissions
- **Read**: All workspace and project files
- **write**: Workspace configuration and project templates
- **Shell Access**: Requires approval for workspace changes

#### Project Implementation Agents
- **Read**: Project files and workspace context
- **Write**: Only project files in `projects/`
- **Shell Access**: Requires approval for project operations

#### Read-Only Agents
- **Read**: All files as needed for review
- **Write**: None (edit permissions set to deny)
- **Shell Access**: Deny

---

## 9. Integration and Validation

### 9.1 Protocol Compliance

#### Documentation Requirements
1. **Update Root AGENTS.md**: Add protocol reading requirement
2. **Create .opencode/AGENT_PROTOCOL.md**: Establish collaboration protocol
3. **Update Agent Prompts**: Include protocol references where appropriate
4. **Validate Configuration**: Ensure all agents have appropriate permissions

### 9.2 Validation Process

#### Step 1: Protocol Creation
1. Create comprehensive `.opencode/AGENT_PROTOCOL.md`
2. Document all agent roles and responsibilities
3. Establish project loading procedures
4. Define planning and implementation handoff
5. Specify memory management rules
6. Establish documentation requirements
7. Define new-project creation process
8. Set Git workflow rules

#### Step 2: Configuration Update
1. Update `opencode.json` instructions to include protocol
2. Add protocol reading requirement to agent prompts
3. Validate that all agent permissions align with protocol
4. Ensure read-only agents remain protected
5. Verify workspace-architect has appropriate permissions

#### Step 3: Documentation Creation
1. Create initial `.opencode/AGENT_PROTOCOL.md`
2. Populate with comprehensive collaboration rules
3. Establish project documentation structure
4. Define parts-and-measurements format
5. Create decision record templates

#### Step 4: Testing and Validation
1. Validate protocol JSON syntax
2. Check that agents can load project context
3. Verify planning handoff works correctly
4. Test memory update procedures
5. Ensure documentation processes function
6. Validate Git workflow rules

### 9.3 Success Criteria

✅ **Agent Roles Defined**: All configured agents have clear responsibilities
✅ **Project Context Loading**: Agents can identify and load project context
✅ **Planning Handoff**: Clear procedures for approval and delegation
✅ **Memory Management**: Proper separation of workspace and project memory
✅ **Documentation Requirements**: Clear guidelines for engineering documentation
✅ **New Project Creation**: Established process for project setup
✅ **Git Workflow**: Clear rules for branching and publication
✅ **Write Boundary Enforcement**: Workspace-protected files, project-specific access
✅ **Protocol Integration**: Protocol embedded in agent prompts and configuration

---

## 10. Implementation Instructions

### 10.1 Create `.opencode/AGENT_PROTOCOL.md`

The protocol file should contain the complete content from section 9 of this document.

### 10.2 Update Root `AGENTS.md`

Add the following requirement:

```markdown
## Collaboration Protocol

Before substantial planning or implementation:

1. Read `.opencode/AGENT_PROTOCOL.md` to understand workspace collaboration rules.
2. Identify the active project and load project context.
3. Follow established procedures for planning, implementation, and handoffs.
4. Update project memory after meaningful progress.
5. Read `.opencode/AGENT_PROTOCOL.md` retreat: [Link to .opencode/AGENT_PROTOCOL.md]
```

### 10.3 Update Agent Prompts

Add protocol references to relevant agent prompts, particularly:
- `plan` agent: Reference to planning handoff procedures
- `cad-implementer` agent: Reference to project-scoped work requirements
- `workspace-architect` agent: Reference to workspace maintenance responsibilities

### 10.4 Validation Checklist

After implementing changes, verify:

1. **Protocol File Exists**: `.opencode/AGENT_PROTOCOL.md` is created and accessible
2. **Agent Roles**: All configured agents have documented roles
3. **Permission Alignment**: Agent permissions align with protocol requirements
4. **Documentation Requirements**: Clear guidelines for engineering documentation
5. **Git Workflow**: Established rules for project branching and publication
6. **Review Process**: Independent review capabilities maintained
7. **Collaboration Features**: All required collaboration procedures documented

---

## Summary

This agent protocol establishes a consistent collaboration framework for the multi-project mechanical CAD workspace:

### Key Features

✅ **Clear Role Definition**: Every agent has defined responsibilities and scope
✅ **Project Isolation**: Workspace and project operations are strictly separated
✅ **Evidence-Based Planning**: All decisions based on verified information
✅ **Structured Documentation**: Comprehensive documentation requirements
✅ **Safe Git Workflow**: Clear rules for branching and publication
✅ **Memory Management**: Proper separation of workspace and project knowledge
✅ **Review and Validation**: Independent verification capabilities maintained

### Implementation Requirements

1. **Create `.opencode/AGENT_PROTOCOL.md`** with complete collaboration rules
2. **Update root `AGENTS.md`** to require protocol reading
3. **Validate agent permissions** ensure project isolation
4. **Test collaboration procedures** verify handoff and review workflows
5. **Establish documentation structure** for engineering projects

The workspace is now ready to support multiple independent CAD projects with clear protocols for collaboration, project isolation, and quality assurance.