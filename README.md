# Cross-Platform UI Factory Pattern in Python

A clean implementation of the Factory Pattern for creating platform-specific UI elements (Windows, Mac, Linux) in Python.

## Overview

This project demonstrates how to use the Abstract Factory design pattern to create platform-appropriate UI elements while keeping client code decoupled from concrete implementations.

## Features

- **Platform Detection**: Automatically detects the operating system
- **UI Element Factories**: Creates consistent, platform-specific UI elements
- **Extensible Design**: Easy to add new platforms or UI components
- **Type Hints**: Full Python type hint support for better code clarity

## Design Pattern

![Abstract Factory Pattern Diagram](https://refactoring.guru/images/patterns/diagrams/abstract-factory/structure.png)

This implementation follows the **Abstract Factory** pattern, which:
1. Provides an interface for creating families of related objects
2. Encapsulates platform-specific implementations
3. Promotes consistency among created objects

## Working

```
# Get the appropriate factory for current platform
factory = get_ui_factory()

# Create platform-specific UI elements
button = factory.create_button()
window = factory.create_window()
menu = factory.create_menu()

# Use the elements
button.render()
window.render()
menu.render()
button.on_click()
```
