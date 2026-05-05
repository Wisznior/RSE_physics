# RSE_physics
A simple calculator for physics units using **Pint**.

## Functions
- Automatic unit conversion for speed calculations
- CI/CD with GitHub Actions ( tests + docs deployment )
- documentation MkDocs

## Installation
```bash
pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ RSE-physics-Wiszniowski pint>=0.24
```

## Usage
```python
from RSE_physics import calc_speed
print(calc_speed("100m", "10s"))
```

## Demo
Open notebook in browser:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Wisznior/RSE_physics/blob/main/notebooks/demo.ipynb#)
