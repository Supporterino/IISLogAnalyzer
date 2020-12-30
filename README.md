# IISLogAnalyzer

## Introduction

This analyzer uses IIS Logs, to create statistics as raw text files and as CSV files. besides the mentioned text reports the analyzer also creates a directory called `graphs`, which stores a collection of charts created with `matplotlib`.

## Requirements

+ Python > 3.5 (Not tested with python 2.X)
+ matplotlib >= 3.1.1
+ Memory >= Logfiles size (A future version will probably migrate to a real db to remove this constrain)
