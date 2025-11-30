# 🎓 Discrete Mathematics Toolkit

A professional PyQt5 application for discrete mathematics analysis with modern dark mode UI.

## ✨ Features

### 🔗 Relation Checker
- Check if a relation is **reflexive**, **symmetric**, **antisymmetric**, or **transitive**
- Determine if a relation is an **equivalence relation**
- Generate **zero-one matrix** representation
- Display **directed graph** (digraph) edge list

### ⚡ Logic Equivalence Checker
- Parse logical expressions with operators: `~` (NOT), `v` (OR), `^` (AND), `->` (IMPLIES), `<->` (BICONDITIONAL)
- Generate **truth tables** for any expression
- Check if two expressions are **logically equivalent**
- Quick-insert operator buttons

### 🌳 Tree Validator
- Validate if a graph is a **tree**
- **Cycle detection** using DFS algorithm
- **Connectivity verification** using BFS algorithm
- Live edge count validation
- Step-by-step guided input

## 🚀 Quick Start

### Prerequisites
```bash
pip install pyqt5
```

### Run the Application
```bash
python main.py
```

## 📖 Usage Examples

### Example 1: Check Equivalence Relation
1. Go to **🔗 Relations** tab
2. Set A: `1, 2, 3`
3. Relation: `(1,1), (2,2), (3,3), (1,2), (2,1), (1,3), (3,1), (2,3), (3,2)`
4. Click **Analyze Relation**
5. Result: ✓ Equivalence Relation (all properties satisfied)

### Example 2: Verify Logical Equivalence
1. Go to **⚡ Logic** tab
2. Expression 1: `p -> q`
3. Expression 2: `~p v q`
4. Click **Check Equivalence**
5. Result: ✓ Equivalent (De Morgan's law)

### Example 3: Validate Tree
1. Go to **🌳 Trees** tab
2. Vertices: `A, B, C, D`
3. Click **Set Vertices**
4. Add edges: `A-B`, `B-C`, `C-D`
5. Click **Validate Tree**
6. Result: ✓ Valid tree (3 edges, no cycles, connected)

## 🎨 Design Features

- **Professional Dark Mode**: Deep dark theme with vibrant cyan accents
- **Color-Coded Results**: Green for success, red for errors
- **Responsive Layout**: Smooth interactions with hover effects
- **High DPI Support**: Sharp rendering on all displays
- **Intuitive Navigation**: Tabbed interface for easy module switching

## 📁 Project Structure

```
discreteMaths/
├── backend/               # Pure Python logic (no UI dependencies)
│   ├── relation_checker.py
│   ├── logic_checker.py
│   └── tree_checker.py
├── frontend/              # PyQt5 UI components
│   ├── styles.py          # Dark mode stylesheet
│   ├── relation_widget.py
│   ├── logic_widget.py
│   ├── tree_widget.py
│   └── main_window.py
└── main.py               # Application entry point
```

## 🔧 Extensibility

The architecture supports easy additions:
- **Backend**: Add new logic classes in `backend/`
- **Frontend**: Create new widgets in `frontend/`
- **Styling**: All styles centralized in `styles.py`

New modules automatically inherit the dark mode theme!

## 💡 Technical Highlights

- **Graph Algorithms**: DFS (cycle detection), BFS (connectivity)
- **Expression Parsing**: Regex-based with operator precedence
- **Matrix Generation**: Dynamic zero-one matrix construction
- **Truth Tables**: Exhaustive variable combinations
- **Type Flexibility**: Handles numeric and string elements

## 📚 Perfect For

- Discrete mathematics students
- Educators demonstrating concepts
- Quick homework verification
- Exploring mathematical structures
- Learning about relations, logic, and graphs

---

**Enjoy exploring discrete mathematics! 🎓✨**
