## Stanford Grade Calculator

The following is a command-line Stanford Grade Calculator. This handy command-line tool helps you figure out your GPA for a specific quarter, a whole year, or even your overall GPA super easily.

![Demo of Stanford Grade Calculator](https://github.com/markmusic27/gpa_calculator/blob/main/docs/demo.png?raw=true)


## How GPA is Calculated

The GPA is calculated using the formula:

```math
\text{GPA} = \frac{\sum (\text{Class Grade} \times \text{Units})}{\text{Total Units}}
```
// 


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

## Installation

To install and run the Stanford Grade Calculator, ensure you have Python installed on your system. Then, clone the repository and navigate to the project directory. Run the following command to install any necessary dependencies:

```bash
pip install -r requirements.txt
```

## Loading Grades

To load your grades, create a JSON file for each academic year in the `grades` folder. Each file should contain your grades quarter by quarter. You can add classes, grades, and units for each quarter. Here's an example structure:

```json
{
    "fall": {
        "MATH 21": {
            "grade": "A",
            "units": 4
        },
        "PWR 1OS": {
            "grade": "B+",
            "units": 4
        },
        "GENE 134": {
            "grade": "B+",
            "units": 3
        }
    }
}
```

Feel free to modify the grades and units to see how it affects your GPA.

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
