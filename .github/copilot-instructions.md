# Copilot Instructions for Articles Code Challenge

## Project Overview
This is a Phase 3 Python code challenge implementing a **Magazine domain with many-to-many relationships** between Articles, Authors, and Magazines. The project uses pure Python (no SQLAlchemy) to practice object-oriented programming and relationship modeling.

## Architecture & Data Model

### Core Domain Model (in `lib/classes/many_to_many.py`)
- **Author**: Has many Articles. Properties must validate name (str, non-empty, immutable)
- **Magazine**: Has many Articles. Properties must validate name (2-16 chars, mutable) and category (str, non-empty, mutable)
- **Article**: Belongs to both Author and Magazine. Properties must validate title (5-50 chars, str, immutable)

**Key Pattern**: Articles act as the join table for the many-to-many Author-Magazine relationship. Maintain bidirectional consistency: when accessing `author.articles()`, it must return Article instances that reference that author.

### Critical Implementation Notes
1. **Immutable Properties**: Use `@property` with private `_attribute` backing. Prevent reassignment using `hasattr()` checks in the setter or during property access validation.
2. **Unique Collections**: Methods like `author.magazines()` and `magazine.contributors()` must return unique lists (use sets internally if needed).
3. **Aggregate Methods**: Methods like `Magazine.article_titles()` return None if empty, not empty list.
4. **Class-Level State**: `Magazine.top_publisher()` requires tracking all Magazine instances created (store in class variable).

## Testing & Validation

### Running Tests
```bash
pytest -v  # Run all tests with verbose output
```

### Test Structure (`lib/testing/`)
- **conftest.py**: Configures pytest to use docstrings as test names
- Test files use pytest fixtures and parameterization
- Tests have comments indicating which lines to toggle for optional Exception validation

### Development Workflow
```bash
pipenv shell              # Enter pipenv environment
python lib/debug.py       # Interactive debugging with ipdb
pytest lib/testing/       # Run specific test directory
```

## Project-Specific Conventions

1. **Validation Strategy**: Early versions accept invalid values silently (tests mutate properties and verify immutability). Advanced versions should raise `Exception` (requires uncommenting test lines).
2. **Return Types Are Strict**: Return `None` for empty aggregates (not empty list). Return lists for collections, never mixed types.
3. **Bidirectional Sync**: No persistence layer—maintain relationship integrity by careful method implementations (e.g., if Article stores author/magazine references, those same Article objects must appear in author/magazine collection methods).

## Key Files & Responsibilities
- `lib/classes/many_to_many.py`: Class definitions (mostly stubs needing implementation)
- `lib/testing/{article,author,magazine}_test.py`: Test specifications
- `lib/debug.py`: Interactive testing entry point
- `pytest.ini`: Configures Python path to include `lib` directory

## Common Gotchas
- Properties that are "immutable after instantiation" don't prevent mutation in tests; implement validation logic, don't rely on Python's default behavior
- `articles()`, `magazines()`, `contributors()` methods must handle cases where no relationships exist
- When implementing class methods like `top_publisher()`, must track instances at class creation time
