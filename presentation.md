# Discrete Mathematics Toolkit
## A Professional Analysis Tool for Students & Educators

---

# 📖 Overview

**Discrete Mathematics Toolkit** is a powerful, modern desktop application designed to assist students and educators in exploring core discrete mathematics concepts.

### 🎯 Goal
To provide a visual, interactive, and accurate tool for verifying calculations and understanding complex mathematical structures.

### 👥 Target Audience
- **Students**: Verify homework and understand algorithms.
- **Educators**: Demonstrate concepts live in class.
- **Learners**: Explore relations, logic, and graph theory.

---

# ✨ Key Features

The application is built around three robust modules:

1.  **🔗 Relation Checker**
    *   Analyze properties of relations on sets.
2.  **⚡ Logic Equivalence Checker**
    *   Generate truth tables and verify logical equivalences.
3.  **🌳 Tree Validator**
    *   Construct graphs and validate tree properties visually.

---

# 🔗 Feature: Relation Checker

Comprehensive analysis of mathematical relations.

### Capabilities
- **Property Verification**: Instantly checks if a relation is:
    - Reflexive
    - Symmetric
    - Antisymmetric
    - Transitive
- **Equivalence Relations**: Automatically determines if a relation is an equivalence relation.
- **Visualizations**:
    - Generates **Zero-One Matrix** representations.
    - Displays **Directed Graph (Digraph)** edge lists.

---

# ⚡ Feature: Logic Equivalence Checker

A powerful engine for propositional logic.

### Capabilities
- **Expression Parsing**: Supports standard operators:
    - `~` (NOT), `v` (OR), `^` (AND), `->` (IMPLIES), `<->` (BICONDITIONAL)
- **Truth Tables**: Generates complete truth tables for any valid expression.
- **Equivalence Testing**: Compares two expressions to check if they are logically equivalent (e.g., verifying De Morgan's Laws).
- **User-Friendly Input**: Quick-insert buttons for mathematical symbols.

---

# 🌳 Feature: Tree Validator

Interactive graph theory tool.

### Capabilities
- **Graph Construction**: Step-by-step input for vertices and edges.
- **Validation Algorithms**:
    - **Cycle Detection**: Uses Depth-First Search (DFS) to find cycles.
    - **Connectivity**: Uses Breadth-First Search (BFS) to ensure the graph is connected.
    - **Edge Counting**: Verifies the $|E| = |V| - 1$ property.
- **Real-time Feedback**: Immediate validation results (Valid Tree / Invalid).

---

# 🎨 Design & User Experience

Built with a focus on usability and aesthetics.

- **Professional Dark Mode**: A deep dark theme with vibrant cyan accents for reduced eye strain and a modern look.
- **Color-Coded Feedback**:
    - 🟢 **Green** for success/valid results.
    - 🔴 **Red** for errors/invalid states.
- **Responsive Layout**: Smooth hover effects and intuitive tabbed navigation.
- **High DPI Support**: Crystal clear rendering on 4K and Retina displays.

---

# 🛠️ Technical Architecture

Engineered for performance and maintainability.

### 🔧 Tech Stack
- **Language**: Python 3
- **GUI Framework**: PyQt5
- **Architecture**: Modular Backend/Frontend separation.

### 📂 Structure
- **Backend**: Pure Python logic for algorithms (DFS, BFS, Matrix operations).
- **Frontend**: PyQt5 widgets with custom styling (`styles.py`).
- **Extensibility**: Easy to add new modules without affecting existing ones.

---

# 🚀 Future Roadmap

- **Set Theory Module**: Operations like Union, Intersection, Difference.
- **Graph Visualization**: Visual plotting of graphs and trees.
- **Export Capabilities**: Save results to PDF or LaTeX.

---

# 🎓 Thank You!

**Discrete Mathematics Toolkit**
*Explore the beauty of mathematics.*
