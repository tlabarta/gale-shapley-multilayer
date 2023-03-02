# Gale-Shapley Extension for two layers of preferences


This respository contains an extension to the [Gale-Shapley algorithm](https://dl.acm.org/doi/abs/10.5555/68392). The extension was presented in the publication by **Martin Aleksandrov and Tobias Labarta: "Fighting Passenger Harassment During Taxi Rides"**. 

The graphic below shows the code architecture. Required packages can be found in **requirements.txt**.


![Architecture](https://user-images.githubusercontent.com/93525195/222461753-5de9b294-f890-4ea9-954c-34e61d3158ac.png)


**main:**
Calls the benchmark and runtime procedures.

**benchmark:**
For first part of the experiment, investigating efficiency and stability of extended Gale-Shapley algorithm. Defines the parameter n for which benchmarks of n drivers and passengers shall be created using the methods from utilities.py. Finally matches the benchmarks using matching.py and calculates performance indicators with methods from utilities.py. Exports the results as .csv. Below is more documentation regarding the benchmark experiment.

**runtime:**
For second part of the experiment, investigating runtime of extended Gale-Shapley for an increasing set of drivers and passengers.

**matching:**
Contains procedures for executing the matching, calling utility methods for calculating performance indicators and returning the results.

**utilities:**
Contains methods for creating ETA, profit and gender preferences. Also contains methods for matching, calculating blocking pairs and calculating other performance indicators.

**Analysis.ipynb:**
Jupyter Notebook that analyzes the benchmark and run time results and creates plots based on the data.


### Benchmark experiment

![Benchmark Experiment](https://user-images.githubusercontent.com/93525195/221889145-6d5917d0-61ed-49ab-b8c4-de54579fd110.png)

### Columns in the generated data files
![Results](https://user-images.githubusercontent.com/93525195/221901656-9f76a2d9-39d5-428e-b368-4c93f1497a0b.png)




