# Hadoop-Conditional-Join

# Introduction
This is a Hadoop Project to tally the total number of viewers for shows on ABC channel from data/input1.txt and data/input2.txt

# Objective
To write a Hadoop mapper and reducer program to join the two datasets based on TV channel and count the views for each show on ABC channel.

# Input Dataset
### input1.txt (show, channel)
```
Hourly_Sports,DEF
Baked_News,BAT
PostModern_Talking,XYZ
Loud_News,CNO
Almost_Show,ABC
Hot_Talking,DEF
Dumb_Show,BAT
Surreal_Show,XYZ
Cold_Talking,CNO
Hourly_Cooking,ABC
Baked_Cooking,DEF
PostModern_News,BAT
.
.
.
```

### input2.txt (show, views)
```
Hourly_Sports,21
PostModern_Show,38
Surreal_News,73
Dumb_Cooking,144
Cold_Talking,287
Almost_Talking,574
Loud_News,113
Hot_Talking,228
Baked_Games,459
Hourly_Talking,922
PostModern_Sports,813
Surreal_Cooking,596
Dumb_Games,163
Cold_Show,334
Almost_Show,677
.
.
.
```

# Requirements 
This code has been developed and tested on Python 3.8 with Hadoop(v2.4.1)

# Execution

### Initialising Hadoop
```
bin/hadoop namenode -format
```
```
sbin/start-dfs.sh
```
```
sbin/start-yarn.sh
```

### Creating and uploading to input directory
```
 bin/hdfs dfs -mkdir /inputs
```
##### Uploading both input files to /inputs
```
 bin/hdfs dfs -copyFromLocal /mnt/d/Users/Desktop/Hadoop_Linux/hadoop-2.4.1/MapReduceTutorial/data/input1.txt /inputs
 bin/hdfs dfs -copyFromLocal /mnt/d/Users/Desktop/Hadoop_Linux/hadoop-2.4.1/MapReduceTutorial/data/input2.txt /inputs
```
##### Check input directory
```
bin/hdfs dfs -ls /inputs
```

### Running the hadoop program
##### Syntax
```
bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.4.1.jar 
-file <full path to mapper code>/mapper.py -mapper <full path to mapper code again>/mapper.py 
-file <full path to reducer code>/reducer.py -reducer <full path to reducer code again>/reducer.py 
-input /<path to hdfs input directory> 
-output /<creating a path for hdfs output directory>
```
##### Example (one command entirely)
```
bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.4.1.jar 
-file /mnt/d/Users/Desktop/Hadoop_Linux/hadoop-2.4.1/MapReduceTutorial/mapper.py -mapper /mnt/d/Users/Desktop/Hadoop_Linux/hadoop-2.4.1/MapReduceTutorial/mapper.py 
-file /mnt/d/Users/Desktop/Hadoop_Linux/hadoop-2.4.1/MapReduceTutorial/reducer.py -reducer /mnt/d/Users/Desktop/Hadoop_Linux/hadoop-2.4.1/MapReduceTutorial/reducer.py 
-input /inputs 
-output /outputs
```

##### Checking the output directory
```
bin/hdfs dfs -ls /outputs
```

##### Running the output file
```
bin/hdfs dfs -cat /outputs/part-00000
```

# Output
```
Almost_Games    8149
Almost_News     7596
Almost_Show     8532
Baked_Games     9692
Baked_News      7824
Cold_News       7500
Cold_Sports     9636
Dumb_Show       9956
Dumb_Talking    18704
Hot_Games       8716
Hot_Show        8036
Hourly_Cooking  8452
Hourly_Show     7992
Hourly_Talking  19704
Loud_Games      10304
Loud_Show       7804
PostModern_Games        8244
PostModern_News 9736
Surreal_News    8024
Surreal_Sports  8144
```

