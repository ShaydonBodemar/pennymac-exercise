# Run Instructions
In order to run the demo of the modules, use the following commands (`python3` instead if python2 not installed). A `-w` flag is used to indicate the filetype is weather, and `-s` to indicate a soccer filetype. The argument following this flag should be the filename, as shown in the example.
```bash
# the below entry will allow running of the given weather data file
python run_exercise.py -w w_data.dat

# the below entry will allow running of the given soccer data file
python run_exercise.py -s soccer.dat
```
If no version of Python is installed, installation instructions can be found at [this link](https://wiki.python.org/moin/BeginnersGuide/Download).

# Feedback
## Influence Between Modules
The data input format, as can be seen, is very similar between the two modules, with pandas DataFrames being populated from the data as it's read in line-by-line. As far as the main functions of each, the minimum difference between tempereatures and for/against goals, in the `weather.py` and `soccer.py` respectively, were very similar to find. The main distinction between the two is that `abs()` had to be used to find the absolute value in difference between for/against goals. This is because either might be larger than the other, which was not the case for the weather data.

Besides these items, the main difference between the two modules came down to formatting, which was relatively easy to handle.

## Working Time
From the creation of the repository to the completion of the exercise, this took me about 3 hours.

# TODO
## Missing Data
Since there were missing data values in 'w_data.dat', the manner in which the DataFrame was populated would be very erroneous if the data at or past these missing values were to be accessed. This could be fixed without too much trouble, but I did not do it for this exercise since it was not necessary.

# Thank You
Thank you for giving me the opportunity to showcase my work and technical abilities with this coding exercise.