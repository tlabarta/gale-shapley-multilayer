# Gale-Shapley Extension for two layers of preferences


This respository contains an extension to the [Gale-Shapley algorithm](https://dl.acm.org/doi/abs/10.5555/68392). The extension first presented in the publication by Martin Aleksandrov and Tobias Labarta: "Fighting Passenger Harassment During Taxi Rides". 

The graphic below shows the code architecture.


![Architecture](https://user-images.githubusercontent.com/93525195/221872989-0fec4a7e-a9f1-4942-9644-92e2d89537fc.png)


**main:**
Calls the benchmark and runtime procedures.

**benchmark:**
For first part of the experiment. Defines the parameter n for which benchmarks of n drivers and passengers shall be created using the methods from utilities.py. Finally matches the benchmarks using matching.py and calculates performance indicators with methods from utilities.py. Exports the results

**runtime:**

**matching:**

**utilities:**




