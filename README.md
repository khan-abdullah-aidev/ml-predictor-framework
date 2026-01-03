# ML-Style Prediction Framework (OOP-Based)

**A mini prediction framework that demonstrates clean OOP design, polymorphism, and scalable model interfaces — inspired by real-world ML systems.**

---

## Table of Contents
- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Solution](#solution)
- [Architecture](#architecture)
- [Project Structure](#project-structure)

---

## Overview
In real-world machine learning systems, different models often perform different tasks and require different inputs, yet they must be used through a **uniform interface**. Hard-coding model logic or checking model types leads to poor scalability and maintainability.

This project demonstrates how **Object-Oriented Programming (OOP)** and **polymorphism** can be used to design ML-style systems where multiple predictors are accessed in the same way, while handling their internal logic independently.

---

## Problem Statement
- Different predictors expect different types of input (numeric, text, etc.)
- Application code should not need to know how each predictor works internally
- Adding a new predictor should not require modifying existing logic

Conditional-based designs (`if-else`, `isinstance`) break abstraction and do not scale well.

---

## Solution
This framework implements:
- A `BasePredictor` class defining a common `predict(data)` interface
- Multiple concrete predictors inheriting from the base class
- A unified input structure (dictionary / JSON-like object)
- True polymorphism, where each predictor decides internally what data it needs

The calling code interacts with all predictors in the **same way**, without hard-coded logic.

---

## Architecture

BasePredictor
   ├── SalaryPredictor
   └── SentimentPredictor

- `BasePredictor` defines the contract (`predict`)
- Concrete predictors implement their own prediction logic
- The system can scale by adding new predictors without changing existing code

---

## Project Structure

ml-predictor-framework/
│
├── base.py        # Base class with predict() contract
├── salary.py      # SalaryPredictor (numeric prediction example)
├── sentiment.py   # SentimentPredictor (text prediction example)
├── main.py        # Demo: create predictors and call predict(data)
└── README.md
