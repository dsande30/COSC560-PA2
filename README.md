# COSC 560 Programming Assignment 2
## Dakota Sanders & Andrey Karnauch

### Shell script
If ```/usr/lib/jvm/default-java``` does not exist, do a ```sudo apt-get install default-jdk```
#### Set up environment:
```
export HADOOP_HOME=/usr/local/hadoop-2.7.6/
export JAVA_HOME=/usr/lib/jvm/default-java
export PATH=${JAVA_HOME}/bin:${HADOOP_HOME}/bin:${PATH}
```
#### Creating files on HDFS:
```
hadoop fs -[ls, mkdir, copyFromLocal] /tmp
```
#### Running mapper.py and reducer.py
```
hadoop jar /usr/local/hadoop-2.7.6/share/hadoop/tools/lib/hadoop-streaming-2.7.6.jar -files ii-mapper.py,ii-reducer.py,shakebooks/ -mapper ii-mapper.py -reducer ii-reducer.py -input /tmp/akarnauc/books/dummy.txt -output /tmp/akarnauc/out
```
### MapReduce Function 1: StopWords
Implement mapping function that analyzes the wordcount of all words from a corpus. Reduce function creates a blacklist of stopwords based on a user-configurable percentage.

### MapReduce Function 2: Full Inverted Index
Implement mapping function that (ignoring stopwords) creates key value pairs keyed on words with a pair value containing the file name and the word location. Reduce function counts occurances and pairs with location.

### Example: 
#### Document 1:
**1. Yuh, ooh, brr, brr**\
**2. Gucci gang, Gucci gang, Gucci gang, Gucci gang (Gucci gang)**\
**3. Gucci gang, Gucci gang, Gucci gang (Gucci gang)**\
**4. Spend three racks on a new chain (Yuh)**

#### Document 2:
**1. When I die, bury me inside the Gucci store (tell 'em)**\
**2. When I die, bury me inside the Louis store (true)**

#### Map [Key &rarr; (DocID, Line No.)]
>Yuh &rarr; (1, 1)\
>Ooh &rarr; (1, 1)\
>brr &rarr; (1, 1)\
>brr &rarr; (1, 1)\
>Gucci &rarr; (1, 2)\
>Gucci &rarr; (1, 2)\
>Gucci &rarr; (1, 2)\
>Gucci &rarr; (1, 2)\
>Gucci &rarr; (1, 2)\
>...\
>store &rarr; (2, 2)\
>true &rarr; (2, 2)

#### Reduce [Key &rarr; List of (DocID, Line No.)]
>Yuh &rarr; [(1, 1), (1, 4)]\
>Ooh &rarr; [(1, 1)]\
>...\
>true &rarr; [(2, 2)]
