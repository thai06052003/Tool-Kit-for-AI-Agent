---
inclusion: fileMatch
fileMatchPattern: ["**/*.ts", "**/*.tsx", "**/*.js", "**/*.jsx"]
---

# TypeScript / React Development Standards

## TypeScript
- `strict: true` in tsconfig.json
- Prefer `const` over `let`, never `var`
- Use `type` for unions/intersections, `interface` for objects with methods
- Use `satisfies` operator for type narrowing
- Zod or io-ts for runtime validation

## React
- Functional components with hooks only
- Server Components by default in Next.js (App Router)
- Use `'use client'` only when actually needing client features
- Memoize only when measured: `useMemo`, `useCallback`, `React.memo`
- Extract hooks into `useXxx` pattern

## State Management
- Server state: React Query / SWR
- Client state: Zustand or React Context (small apps)
- URL state: `useSearchParams` for filters/pagination

## Performance
- Lazy loading with `dynamic()` or `React.lazy()`
- Image optimization with `next/image`
- Bundle analysis with `@next/bundle-analyzer`
- Avoid layout shifts (set explicit width/height)

## Testing
- Vitest or Jest for unit tests
- React Testing Library for component tests
- Playwright for E2E tests
- MSW (Mock Service Worker) for API mocking
