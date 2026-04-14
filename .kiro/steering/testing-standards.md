---
inclusion: fileMatch
fileMatchPattern: ["**/*.test.*", "**/*.spec.*", "**/tests/**/*"]
---

# Testing Standards

## TDD Workflow: Red → Green → Refactor

1. **RED**: Write a failing test that defines the desired behavior
2. **GREEN**: Write the minimum code to make it pass
3. **REFACTOR**: Clean up while keeping tests green

## Test Structure (AAA Pattern)
```
Arrange → Set up test data and dependencies
Act     → Execute the code under test
Assert  → Verify the expected outcome
```

## Naming Convention
- C#: `MethodName_Condition_ExpectedResult` → `PlaceOrder_EmptyCart_ThrowsException`
- TS: `should [expected] when [condition]` → `should throw when cart is empty`
- Python: `test_method_condition_expected` → `test_place_order_empty_cart_raises`

## Test Prioritization
1. Unit Tests (70%) — Fast, isolated, test one unit
2. Integration Tests (20%) — Test component interactions
3. E2E Tests (10%) — Critical user flows only

## Mocking Rules
- Mock external dependencies (APIs, databases)
- Never mock the system under test
- Prefer fakes over mocks for complex behavior
- Keep mock setup close to the test

## Coverage Target: ≥80%
- Focus on behavior coverage, not line coverage
- Critical paths: 100% coverage required
- Edge cases: null, empty, boundary values, error paths
