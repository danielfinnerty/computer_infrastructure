# Computer Infrastructure

by: Daniel Finnerty

## Introduction

This project provides a clear demonstration of the learnings gained both from the computer infrastructure module, and through additional research performed as a suplement to these learnings.

The scope of said project is to perform tasks regarding the five FAANG stocks (Facebook, Apple, Amazon, Netflix, Google); downloading the previous 5 day hourly stock prices for all five, saving the data, creating and saving a plot of the results, and finally automating the entire process through the use of GitHub Actions workflow.

To achieve this, the following Python packages are required.

- yfinance
- pandas
- numpy
- datetime
- matplotlib.pyplot

The code explanations and information sources can be found in `problems.ipynb`, with the finished code in `faang.py`.

All downloaded data can be found in the `data` folder, and associated plots in the `plots` folder.


### Running the Notebook locally
The notebook can be ran locally however, prior to doing so the repository must be cloned to your local machine through the following steps:

#### _Using cmder_

1. Download and install full version of cmder from:  
https://cmder.app/ 

2. In cmder, clone the repository

```
git clone https://github.com/danielfinnerty/computer_infrastructure.git
```

3. On your local machine, set new repository as directory

4. Configure git pull rebase

```
git config pull.rebase false
```

5. Open repository

```
python -m notebook
```

6. Select the `problems.ipynb` file

7. Click on the double-arrow icon at the top to 'restart the kernell and run all cells'.

### Running `faang.py`

As a result of the GitHub Actions outlined in the `poblems.ipynb` notebook, the `faang.py` code runs every Saturday morning at 09:05am however, to run it manually, the following steps needs to be taken:

1. In the main GitHub root directory ([Here](https://github.com/danielfinnerty/computer_infrastructure)) click on `Actions`
2. Click `Run Faang Script and Commit`
3. To the righthand side, select `Run workflow` and click the green icon `Run workflow`
4. Refresh the page

Once refreshed, the new workflow will become visible in the list, with the icon turning to a green tick once complete.


### Output
From running the script either manually, through the above steps, or automatically per the schedule, a download of the most recent stock prices will be created, and an associated plot. Both of these will be titled with the timestamp of when created, and can be found along with all previous downloads and plots in the `data` folder [HERE](https://github.com/danielfinnerty/computer_infrastructure/tree/main/data) and `plots` folder [HERE](https://github.com/danielfinnerty/computer_infrastructure/tree/main/plots).

# End