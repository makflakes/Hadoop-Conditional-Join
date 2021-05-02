# Hadoop-Conditional-Join

# Introduction
What is the total number of viewers for shows on ABC (in data/input1.txt and data/input2.txt)? Write the mapper and reducer program to join two databases based on the mentioned condition.

# Objective
To write a Hadoop mapper and reducer program to join the two datasets based on TV channel and count the views for each show on ABC channel.

# Requirements 
This code has been developed and tested on Python3.8 with Hadoop version 2.4.1

# Execution

### Initialising Hadoop
```
<span style="color:blue">hadoop$</span> bin/hadoop namenode -format
```
```
hadoop$ sbin/start-dfs.sh
```
```
hadoop$ sbin/start-yarn.sh
```

### Creating and uploading to input directory
```
hadoop$ bin/hdfs dfs -mkdir /inputs
```
##### Uploading both input files to /inputs
```
hadoop$ bin/hdfs dfs -copyFromLocal /mnt/d/Users/Desktop/Hadoop_Linux/hadoop-2.4.1/MapReduceTutorial/data/input1.txt /inputs
hadoop$ bin/hdfs dfs -copyFromLocal /mnt/d/Users/Desktop/Hadoop_Linux/hadoop-2.4.1/MapReduceTutorial/data/input2.txt /inputs
```
```
hadoop$ bin/hdfs dfs -ls /inputs
```

### Running the hadoop program
##### Normal format
```
hadoop$ bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.4.1.jar 
-file <full path to mapper code>/mapper.py -mapper <full path to mapper code again>/mapper.py 
-file <full path to reducer code>/reducer.py -reducer <full path to reducer code again>/reducer.py 
-input /<path to hdfs input directory> 
-output /<creating a path for hdfs output directory>
```
##### Example (one command entirely)
```
hadoop$ bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.4.1.jar 
-file /mnt/d/Users/Desktop/Hadoop_Linux/hadoop-2.4.1/MapReduceTutorial/mapper.py -mapper /mnt/d/Users/Desktop/Hadoop_Linux/hadoop-2.4.1/MapReduceTutorial/mapper.py 
-file /mnt/d/Users/Desktop/Hadoop_Linux/hadoop-2.4.1/MapReduceTutorial/reducer.py -reducer /mnt/d/Users/Desktop/Hadoop_Linux/hadoop-2.4.1/MapReduceTutorial/reducer.py 
-input /inputs 
-output /outputs
```

##### Checking the output directory
```
hadoop$ bin/hdfs dfs -ls /outputs
```

##### Running the output file
```
hadoop$ bin/hdfs dfs -cat /outputs/part-00000
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

