---
marp: true
title: Product Documentation with Marp
author: Technical Writer – 23f2000783@ds.study.iitm.ac.in
theme: default
paginate: true
---

<!-- _class: lead -->

# Product Documentation with Marp
### Maintainable • Version Controlled • Multi-format

---

# Why Marp?

- Write slides in **Markdown**
- Convert to **PDF, PPTX, HTML, or Images**
- Perfect for:
  - Technical documentation
  - Teaching & research
  - Conference talks
- Easy integration with **GitHub Pages**

---

<!-- Custom background image -->
![bg cover](https://static.vecteezy.com/system/resources/thumbnails/040/890/255/small_2x/ai-generated-empty-wooden-table-on-the-natural-background-for-product-display-free-photo.jpg)
# Custom Background Example

This slide uses a full background image.

---

# Custom Theme & Styling

<style>
section {
  background: #fdf6e3;
  color: #002b36;
}
h1 {
  color: #b58900;
}
blockquote {
  font-style: italic;
  color: #268bd2;
}
</style>

> Documentation is more effective when it is **consistent, styled, and reusable.**

---

# Algorithmic Complexity

We can write mathematical equations directly:

- Inline math: $O(n \log n)$
- Block math:

$$
T(n) = T(n/2) + O(n) \implies T(n) = O(n \log n)
$$

---

# File Organization

```text
presentation/
├── slides.md        # Main presentation
├── images/          # Backgrounds & assets
├── themes/          # Custom themes
└── package.json     # Build config

