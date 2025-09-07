# System Patterns: Textual Game of Life

## Architecture Overview

The system follows a **Model-View-Presenter (MVP)** pattern with clear separation of concerns:

- **Model**: Universe state and Game of Life logic
- **View**: Textual-based UI rendering and user interactions
- **Presenter**: Coordination between model and view

## Core Components

### GameApp (Main Application)

**Purpose**: Primary Textual application controller

**Responsibilities**:

- Initialize Textual app with header, log widget, and footer
- Handle keyboard bindings (d, n, r keys)
- Coordinate with TextualUniverseView for universe operations
- Manage app-level state like dark/light theme

**Key Patterns**:

- Uses Textual's App base class
- Implements action methods for user commands
- Delegates universe operations to view layer

### UniverseView (Abstract Interface)

**Purpose**: Define contract for universe visualization

**Responsibilities**:

- Abstract interface using Python's abc module
- Defines required methods: add, remove, clear, update
- Event handling: on_produce_next_generation, on_reset_to_seed

**Key Patterns**:

- Interface segregation principle
- Duck typing support via __subclasshook__
- Dependency inversion for testability

### TextualUniverseView (Concrete View)

**Purpose**: Textual-specific implementation of universe display

**Responsibilities**:

- Render universe state in terminal log widget
- Coordinate with presenter for universe operations
- Visual representation using coordinate grid and █ characters

**Key Patterns**:

- Adapter pattern (adapts Textual widgets to UniverseView interface)
- Composition over inheritance (contains Log widget)
- Event delegation to presenter

### UniversePresenter

**Purpose**: Business logic coordinator between model and view

**Responsibilities**:

- Manage universe model (list of Cell objects)
- Implement Game of Life rules and generation transitions
- Coordinate view updates based on model changes

**Key Patterns**:

- Mediator pattern between model and view
- Contains business logic separate from UI concerns
- Currently holds hardcoded seed patterns (planned: TOML file loading)

### Cell

**Purpose**: Fundamental data structure for universe positions

**Responsibilities**:

- Encapsulate x,y coordinates for living cells
- Simple value object with getter methods

**Key Patterns**:

- Value object pattern
- Encapsulation of coordinate data
- Immutable-style design

## Component Relationships

```
GameApp
  ↓ creates
TextualUniverseView
  ↓ contains
UniversePresenter
  ↓ manages
Cell[] (model)
```

## Design Decisions

### MVP vs MVC Choice

- **Chosen**: MVP pattern for clear presenter responsibilities
- **Alternative**: MVC would couple view more tightly to model
- **Benefit**: Easier testing and separation of Textual-specific code

### Interface-Based Design

- **Abstract UniverseView**: Enables different rendering implementations
- **Future extensibility**: Could support different UI frameworks
- **Testing benefits**: Mock implementations for unit tests

### Cell as Value Object

- **Simple coordinate container**: Minimal, focused responsibility
- **Immutable design**: No setters, construction-time initialization
- **Future extension**: Could add cell states, colors, or metadata

## Current Implementation Status

### Working Components

- Basic MVP architecture established
- Textual integration functional
- Coordinate-based cell representation
- Simple seed pattern display

### Areas for Development

- **Game of Life rules**: Currently hardcoded generation transitions
- **Model layer**: No proper universe model with neighbor counting
- **Configuration**: Hardcoded seed patterns (TOML loading planned)
- **Performance**: Remove operation clears all cells instead of selective removal
