<p align="center">
  <h1 align="center"><b>GPA Calculator CLI</b></h1>
  <p align="center">
  ✶ A lightweight CLI for calculating your GPA @ Stanford ✶
    <br />
    <a href="https://github.com/markmusic27/gpa_calculator/archive/refs/heads/main.zip">Download »</a>
    <br />
  </p>
</p>

The following is a command-line Stanford Grade Calculator. This handy command-line tool helps you figure out your GPA for a specific quarter, a whole year, or even your overall GPA easily.

![Demo of Stanford Grade Calculator](https://github.com/markmusic27/gpa_calculator/blob/main/docs/demo.png?raw=true)


## How GPA is Calculated

The GPA is calculated using the formula:

```math
\text{GPA} = \frac{\sum (\text{Class Grade} \times \text{Units})}{\text{Total Units}}
```
<br>


This formula can be applied to calculate the GPA for a specific quarter, a specific year, or across all years.

### Grade Mapping

Below is the table that maps letter grades to their numerical representation:

| Letter Grade | Numerical Value |
|--------------|-----------------|
| A+           | 4.3             |
| A            | 4.0             |
| A-           | 3.7             |
| B+           | 3.3             |
| B            | 3.0             |
| B-           | 2.7             |
| C+           | 2.3             |
| C            | 2.0             |
| C-           | 1.7             |
| D+           | 1.3             |
| D            | 1.0             |
| D-           | 0.7             |
| NP           | 0.0             |
| L            | 2.0             |

## Loading Grades

To load your grades, create a JSON file for each academic year in the `grades` folder. **You need to create this folder in the root directory of the project.** Each file should contain your yearly grades, by quarter. You can add classes, grades, and units for each quarter. Here's an example structure:

```json
{
    "fall": {
        "MATH 21": {
            "grade": "A",
            "units": 4
        },
        "PWR 1OS": {
            "grade": "A",
            "units": 4
        },
        "GENE 134": {
            "grade": "B+",
            "units": 3
        }
    },
    "winter": {
        "COLLEGE 102": {
            "grade": "A",
            "units": 3
        },
        "CS 106B": {
            "grade": "B+",
            "units": 5
        }
     },
     "spring": {
        "COLLEGE 117": {
            "grade": "A",
            "units": 4
        },
        "MATH 51": {
            "grade": "A-",
            "units": 5
        },
        "CS 109": {
            "grade": "A",
            "units": 5
        },
    }
}
```

Feel free to modify the grades and units to see how it affects your GPA. You don't need to add a complete year. For example, this is also a valid `freshman.json` file:

```json
{
    "fall": {
        "MATH 21": {
            "grade": "A",
            "units": 4
        },
        "PWR 1OS": {
            "grade": "A",
            "units": 4
        },
        "GENE 134": {
            "grade": "B+",
            "units": 3
        }
    }
}
```

## Usage

Run the program using:

```bash
python calculator.py
```

The CLI will prompt you to select an option:

1. Calculate total GPA
2. Calculate GPA for a specific quarter
3. Calculate GPA for a specific year
4. Exit

Follow the prompts to calculate your desired GPA.
