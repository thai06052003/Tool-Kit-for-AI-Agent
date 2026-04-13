---
inclusion: fileMatch
fileMatchPattern: ["**/*.cs", "**/*.csproj", "**/*.sln"]
---

# C# / .NET Development Standards

## Code Structure
- Use `sealed` classes by default
- Prefer `record` types for DTOs and value objects
- Enable Nullable Reference Types (`<Nullable>enable</Nullable>`)
- Use `required` keyword for mandatory properties

## Async/Await
- Always pass `CancellationToken` to async methods
- Never use `.Result` or `.Wait()` — deadlock risk
- Use `Task.WhenAll()` for independent parallel operations
- Never use `async void` (except event handlers)

## Dependency Injection
- Register services with appropriate lifetimes: Scoped > Transient > Singleton
- Use `AddScoped<TInterface, TImplementation>()` in Program.cs
- Inject via constructor, use `readonly` fields with `_camelCase`

## Entity Framework Core
- Use Code-First migrations
- Apply `AsNoTracking()` for read-only queries
- Use `Include()` to prevent N+1 queries
- Apply `IEntityTypeConfiguration<T>` for fluent mapping

## API Design
- Minimal API with route groups for simple services
- Controllers for complex domains with proper areas
- Return `TypedResults.Ok()`, `TypedResults.NotFound()`, etc.
- Use `[FromQuery]`, `[FromBody]`, `[FromRoute]` explicitly

## Testing
- xUnit with FluentAssertions
- Moq or NSubstitute for mocking
- WebApplicationFactory for integration tests
- Follow AAA pattern (Arrange-Act-Assert)

## Security
- Parameterized queries only
- `[Authorize]` on all endpoints by default
- Use FluentValidation for input validation
- Store secrets in User Secrets / Azure Key Vault
