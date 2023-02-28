# Gale-Shapley Extension for two layers of preferences


This respository contains an extension to the [Gale-Shapley algorithm](https://dl.acm.org/doi/abs/10.5555/68392). The extension first presented in the publication by Martin Aleksandrov and Tobias Labarta: "Fighting Passenger Harassment During Taxi Rides". 


![Architecture](https://user-images.githubusercontent.com/93525195/221872989-0fec4a7e-a9f1-4942-9644-92e2d89537fc.png)




How to use this repository:
Run main.py to reproduce the results from the report. Currently, it will return profits and ETA for layer 1, as well as genders and gender preferences of layer 2. Then it will run Gale-Shapley to find a stable match on layer 1 and use this match on layer 2 to check for blocking pairs. In case of blocking pairs, it will return the first blocking pair it finds and then terminate. You can increase or decrease the variable n at the beginnning of main.py to increase or decrease the generated drivers and passengers.

NOTE: As the customers and drivers are generated randomly for each run of main.py, the numbers will differentiate.
