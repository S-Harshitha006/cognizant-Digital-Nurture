# Hands-On 1 – QA Concepts, Functional Testing & Defect Lifecycle

## Task 1: Map Testing Types to a Real System

### 1. Testing Levels for the Course Management API

#### Unit Testing
**Test Case:** Verify that the `create_course()` function correctly creates a course object when valid input is provided.

- Component Tested: Single function (`create_course()`)
- Expected Result: A course object is created successfully.

**Classification:** Functional Testing

---

#### Integration Testing

**Test Case:** Verify that the `POST /api/courses/` endpoint correctly stores course information in the database.

- Components Tested:
  - API Endpoint
  - Database

- Expected Result:
  - API returns HTTP 201 Created.
  - Course is stored in the database.

**Classification:** Functional Testing

---

#### System Testing

**Test Case:** Verify the complete flow of adding a course using the API and retrieving it using `GET /api/courses/`.

- Steps:
  1. Send POST request.
  2. Verify response.
  3. Send GET request.
  4. Verify newly created course exists.

**Classification:** Functional Testing

---

#### User Acceptance Testing (UAT)

**Test Case:** A college administrator successfully adds a new course and confirms that it appears in the course list.

**Expected Result:**
The administrator can complete the task without technical assistance.

**Classification:** Functional Testing

---

### 2. Functional vs Non-Functional Testing

| Testing Type | Example |
|--------------|---------|
| Functional | Verify POST /api/courses/ creates a new course successfully. |
| Non-Functional | Verify the API responds within 2 seconds when 100 users send requests simultaneously. |

Example Non-Functional Test:

**Performance Testing**

- Objective:
  Verify the Course Management API can handle multiple concurrent users while maintaining acceptable response time.

---

### 3. Black-Box Testing vs White-Box Testing

| Black-Box Testing | White-Box Testing |
|-------------------|------------------|
| Tester does not know internal code. | Tester has knowledge of source code. |
| Focuses on inputs and outputs. | Focuses on internal logic and code paths. |
| Performed mainly by QA testers. | Performed mainly by developers. |

**QA testers** generally perform **Black-Box Testing**, while **developers** usually perform **White-Box Testing**.

---

### 4. Formal Test Cases for POST /api/courses/

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
|--------------|-------------|---------------|------------|-----------------|---------------|-----------|
| TC001 | Create course with valid data | API running | Send POST request with valid course details | HTTP 201 Created and course stored | | |
| TC002 | Create course with missing course name | API running | Send POST request without course name | HTTP 400 Bad Request with validation message | | |
| TC003 | Create duplicate course | Course already exists | Send POST request using existing course ID | Duplicate course rejected with proper error message | | |

---

# Task 2: Defect Lifecycle & Severity Classification

## 5. Defect Lifecycle

```
New
 ↓
Assigned
 ↓
Open
 ↓
Fixed
 ↓
Retest
 ↓
Verified
 ↓
Closed
```

### Alternative Paths

**Rejected**

- Bug is invalid.
- Duplicate defect.
- Cannot reproduce.
- Works as designed.

**Deferred**

- Bug is acknowledged.
- Fix postponed to a future release due to low priority or schedule constraints.

---

## 6. Severity and Priority Classification

### a) POST /api/courses/ returns HTTP 500 for every request

**Severity:** Critical

**Priority:** P1

**Justification:**
The main functionality of the API is completely unavailable.

---

### b) Course names longer than 150 characters are silently truncated

**Severity:** Medium

**Priority:** P3

**Justification:**
The API works but data integrity is affected.

---

### c) Typo in Swagger documentation

**Severity:** Low

**Priority:** P4

**Justification:**
Only documentation is affected.

---

### d) Login occasionally returns HTTP 401 despite correct credentials

**Severity:** High

**Priority:** P1

**Justification:**
Intermittent authentication failures affect users and indicate possible system instability.

---

## 7. Defect Report

**Defect ID:** DEF-001

**Title:**
POST /api/courses/ returns HTTP 500 Internal Server Error.

**Environment:**

- Windows 11
- Python 3.10
- FastAPI
- Chrome Latest

**Build Version:**
v1.0.0

**Severity:**
Critical

**Priority:**
P1

**Steps to Reproduce:**

1. Start the API.
2. Open Swagger UI.
3. Navigate to POST /api/courses/.
4. Enter valid course details.
5. Click Execute.

**Expected Result:**

Course should be created successfully with HTTP 201 Created.

**Actual Result:**

HTTP 500 Internal Server Error is returned.

**Attachments:**

- Screenshot of 500 error.

---

## 8. Severity vs Priority

### Severity

Severity indicates how seriously the defect affects the system.

### Priority

Priority indicates how quickly the defect should be fixed.

### Example

A typo in the CEO's dashboard heading:

- Severity: Low
- Priority: High

Reason:
The typo does not affect functionality but must be fixed immediately because it is highly visible to senior management.
