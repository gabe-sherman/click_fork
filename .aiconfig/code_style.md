# Code Style Rules for Automated Reviews

These rules define the expectations the AI Code Review Assistant should reference when analyzing code. When providing feedback, reference the rule number where appropriate.

---

## 1. Code Structure and Readability

1.1 Favor **clear, simple logic** over clever implementations.  
1.2 Functions should be small and cohesive; avoid functions exceeding ~50–80 lines unless clearly justified.  
1.3 Each function should do **one thing well**. If a function does multiple unrelated things, suggest splitting.  
1.4 Variable and function names must be **descriptive and meaningful**. Avoid single-letter names except for clear loop indices.  
1.5 Prefer consistent formatting (indentation, spacing, brace style). Deviations should be pointed out.

---

## 2. Error Handling and Robustness

2.1 Code must not ignore errors silently.  
2.2 Use exceptions/error returns consistently according to the project’s conventions.  
2.3 Always validate assumptions on external input.  
2.4 Avoid broad exception catches (e.g., `catch (Exception)` or `except Exception:`) unless there is a documented reason.

---

## 3. Comments and Documentation

3.1 Comments should **explain intent**, not restate what the code already does.  
3.2 Public functions should include a **short description** and **parameter/return behavior** where applicable.  
3.3 TODO comments should include an associated task/issue reference when possible.  
3.4 Avoid excessive commenting; prefer code that is self-explanatory.

---

## 4. Consistency and Project Conventions

4.1 Follow the language-specific style guide used in this repository (e.g., PEP8 for Python, Google C++ style, etc.).  
4.2 Use existing modules/utilities already present in the codebase before writing new ones.  
4.3 Maintain consistent naming conventions (e.g., snake_case, camelCase) as used in the repository.

---

## 5. Performance and Efficiency

5.1 Avoid premature optimization. Only point out performance concerns when:
- The code introduces clear inefficiency (e.g., repeated processing in loops that can be hoisted).
- The inefficiency will meaningfully impact runtime or resource use.

5.2 Memory allocations in loops should be avoided when feasible.  
5.3 Data structures should be chosen for clarity first, then efficiency.

---

## 6. Security and Safety

6.1 Never interpolate untrusted input into system commands, SQL queries, or shell calls without sanitization.  
6.2 Always validate input lengths, formats, and ranges where relevant.  
6.3 Avoid using outdated or unsafe cryptographic or hashing algorithms.

---

## Review Output Style

When providing feedback:
- Be **concise**, **specific**, and **actionable**.
- Prefer *suggestions* over *judgments*.
- Quote only the relevant snippets when referencing code.

**Example response style:**

> Suggestion (Rule 1.4): The variable name `d` is unclear. Consider renaming to `distance_km` to clarify its purpose.

---
