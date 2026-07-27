# Hands-On 2 – SDLC vs TDLC, V-Model & Agile QA Integration

## Task 1: V-Model Mapping

### 9. V-Model Diagram

```
                 SDLC (Development)

            Requirements
                 |
          System Design
                 |
        Architecture Design
                 |
          Module Design
                 |
               Coding
                 |
---------------------------------------------------------
                 |
            Unit Testing
                 |
       Integration Testing
                 |
         System Testing
                 |
      Acceptance Testing

               TDLC (Testing)
```

### SDLC ↔ TDLC Mapping

| SDLC Phase | Corresponding TDLC Phase |
|------------|--------------------------|
| Requirements | Acceptance Testing |
| System Design | System Testing |
| Architecture Design | Integration Testing |
| Module Design | Unit Testing |
| Coding | Execution of Test Cases |

---

## 10. Test Artifacts Produced

| Development Phase | Test Artifact |
|-------------------|--------------|
| Requirements | Acceptance Test Plan |
| System Design | System Test Cases |
| Architecture Design | Integration Test Plan |
| Module Design | Unit Test Cases |
| Coding | Source Code & Test Execution |

---

## 11. Entry and Exit Criteria

### Unit Testing

**Entry Criteria**
- Module is developed.
- Unit test cases are ready.

**Exit Criteria**
- All unit tests executed.
- No critical defects.
- Code coverage achieved.

---

### Integration Testing

**Entry Criteria**
- Unit testing completed.
- Modules integrated.

**Exit Criteria**
- Interfaces verified.
- Integration defects fixed.

---

### System Testing

**Entry Criteria**
- Complete application available.
- Test environment ready.

**Exit Criteria**
- Functional requirements verified.
- No Critical or High severity defects remain.

---

### Acceptance Testing

**Entry Criteria**
- System testing completed.
- Client receives stable build.

**Exit Criteria**
- Client approves application.
- Business requirements satisfied.

---

## 12. Early QA Engagement

### 1. Requirements Review

QA reviews requirements for:
- Completeness
- Ambiguity
- Testability

### 2. Design Review

QA verifies:
- API endpoints
- Database design
- Validation rules
- Test scenarios

---

# Task 2: Agile QA and Shift-Left Testing

## 13. Problems with Waterfall Testing

### Problem 1

Defects are found late, making them expensive to fix.

### Problem 2

Requirements misunderstandings remain unnoticed until testing begins.

### Problem 3

Development and QA teams have limited collaboration, increasing project risk.

---

## 14. QA Role in Agile Ceremonies

### Sprint Planning

- Review user stories.
- Define acceptance criteria.
- Estimate testing effort.

### Daily Stand-up

- Report testing progress.
- Raise blockers.
- Coordinate with developers.

### Sprint Review

- Validate completed features.
- Demonstrate tested functionality.
- Verify acceptance criteria.

### Retrospective

- Discuss issues.
- Improve testing process.
- Suggest automation improvements.

---

## 15. Shift-Left Testing Practices

### a) Requirement Review

QA reviews requirements before development begins to ensure they are complete and testable.

### b) Test Cases Before Code (TDD/BDD)

Prepare test cases before implementation so developers clearly understand expected behaviour.

### c) Static Code Analysis

Use code quality tools to detect coding issues before execution.

### d) API Contract Testing

Verify API request and response formats before integrating with other services.

---

## 16. Acceptance Criteria (Given–When–Then)

### Scenario 1 – Happy Path

**Given** the college admin is logged in

**When** valid course details are entered and submitted

**Then** the course is created successfully and a success message is displayed.

---

### Scenario 2 – Duplicate Course Code

**Given** a course with the same course code already exists

**When** the admin submits the duplicate course code

**Then** the system displays an error stating that the course code already exists.

---

### Scenario 3 – Missing Required Fields

**Given** the course creation form is open

**When** required fields are left empty and submitted

**Then** validation messages are displayed and the course is not created.