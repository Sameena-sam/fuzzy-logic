# Fuzzy Logic Inference System

Python implementations of fuzzy membership functions and a Mamdani fuzzy inference system, built for the Fuzzy Logic module of the MSc in Artificial Intelligence at Asia Pacific University (2026).

## What it does

- **Membership functions:** increasing, decreasing, triangular, trapezoidal, Gaussian and sigmoid.
- **Fuzzy sets:** age groups (very young, young, middle-aged, old), plotted over ages 0 to 100.
- **Inference system:** estimates lifespan from alcohol consumption (0 to 100) and water consumption (0 to 10) with three rules:

| Rule | If | Then lifespan is |
|---|---|---|
| R1 | less water **and** more alcohol | poor |
| R2 | more water **and** less alcohol | good |
| R3 | (more water **and** average alcohol) **or** (less water **and** less alcohol) | average |

AND uses the minimum and OR the maximum. Each rule clips its output set (min implication), the clipped sets are combined with the maximum, and the result is defuzzified with the centroid. With water at 5 and alcohol at 75, the system returns a lifespan of 41.7 on the 10 to 50 scale.

## Project structure

```
fuzzy-logic/
├── src/
│   ├── membership.py            # reusable membership functions
│   ├── membership_examples.py   # increasing, decreasing, triangular and trapezoidal examples
│   ├── age_fuzzy_sets.py        # fuzzy sets for age groups
│   └── lifespan_inference.py    # Mamdani inference system
├── requirements.txt
└── README.md
```

## Run

```bash
pip install -r requirements.txt
python src/lifespan_inference.py   # prints the lifespan and plots the inputs, outputs and rule activations
python src/age_fuzzy_sets.py       # plots the age fuzzy sets
```

To try other inputs, change `inp_water` and `inp_alc` in `src/lifespan_inference.py`.

## Tech

Python, NumPy (2.0 or later), Matplotlib.

## Author

Sameena Siddiqua
