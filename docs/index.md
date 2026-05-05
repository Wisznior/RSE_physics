# RSE_physics Documentation

A simple physics calculator using [Pint](https://pint.readthedocs.io/).

## Functions

### `calc_speed(distance, time)`
Calculates speed from distance and time, returns result in km/h.

**Example:**
```python
from RSE_physics import calc_speed
calc_speed("100m", "10s")  
# "36.0 kilometer / hour"
```