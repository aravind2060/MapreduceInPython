
### General Objective
Learn how to develop and run MapReduce jobs in Python, focusing on processing daily climate summaries from the GHCNd dataset to compute average daily maximum and minimum temperatures.

### Specific Tasks

#### Task 1: Data Preparation
- **1.1** Download the GHCNd data for 2023 (`2023.csv.gz`) from the specified URL.
- **1.2** Extract the `.csv` file from the `.gz` archive to obtain `2023.csv`.

#### Task 2: Setup Hadoop Environment
- **2.1** Ensure a Hadoop cluster is deployed and running.
- **2.2** Verify that Python and the required packages (`Snakebite` for Hadoop file operations and `mrjob` for MapReduce jobs) are installed and configured correctly in your environment.

#### Task 3: Implement Snakebite Script for HDFS Upload
- **3.1** Write a Python script using Snakebite to upload `2023.csv` to the Hadoop Distributed File System (HDFS).
- **3.2** The script should accept the local file path and target HDFS directory path as inputs.

#### Task 4: Hadoop Streaming for Temperature Analysis
- **4.1** Write a Python mapper script to parse each line of `2023.csv`, extracting relevant data for temperature analysis.
- **4.2** Write a Python reducer script to compute the average of the daily maximum and minimum temperatures.
- **4.3** Run the Hadoop streaming job using the mapper and reducer scripts you developed, specifying the input and output paths in HDFS.

#### Task 5: Implement Temperature Analysis with `mrjob`
- **5.1** Create an `MRJob` class in Python that defines the steps of your MapReduce job for temperature analysis.
- **5.2** Implement methods for the mapper and reducer that perform the same calculations as your Hadoop streaming scripts.
- **5.3** Run your `mrjob` script locally or on the Hadoop cluster, analyzing the output to ensure correctness.

#### Task 6: Testing and Analysis
- **6.1** Test your implementation (both Hadoop streaming and `mrjob`) using the data in `2023.csv`.
- **6.2** Analyze the output files to verify that your jobs are computing the average temperatures correctly.
