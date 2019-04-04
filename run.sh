# set up environment variables
export HADOOP_HOME=/usr/local/hadoop-2.7.6/
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export PATH=${JAVA_HOME}/bin:${HADOOP_HOME}/bin:${PATH}

# make scripts executable
chmod +x ~/COSC560-PA2/ii-mapper.py
chmod +x ~/COSC560-PA2/ii-reducer.py
chmod +x ~/COSC560-PA2/wc-mapper.py
chmod +x ~/COSC560-PA2/wc-reducer.py
chmod +x ~/COSC560-PA2/query.py
chmod +x ~/COSC560-PA2/run.sh
chmod +x ~/COSC560-PA2/reset.sh

# set up HDFS
hadoop fs -mkdir /tmp/ta_demo/
hadoop fs -copyFromLocal ~/COSC560-PA2/dummy.txt /tmp/ta_demo/

# run map-reduce job to generate list of stop words
hadoop jar /usr/local/hadoop-2.7.6/share/hadoop/tools/lib/hadoop-streaming-2.7.6.jar -files wc-mapper.py,wc-reducer.py,shakebooks -mapper 'wc-mapper.py shakebooks' -reducer wc-reducer.py -input /tmp/ta_demo/dummy.txt -output /tmp/ta_demo/wc-out
hadoop fs -copyToLocal /tmp/ta_demo/wc-out/part-00000 stop_words.txt

# run map-reduce job to create the inverse indexer
hadoop jar /usr/local/hadoop-2.7.6/share/hadoop/tools/lib/hadoop-streaming-2.7.6.jar -files ii-mapper.py,ii-reducer.py,shakebooks,stop_words.txt -mapper 'ii-mapper.py shakebooks stop_words.txt' -reducer ii-reducer.py -input /tmp/ta_demo/dummy.txt -output /tmp/ta_demo/ii-out
hadoop fs -copyToLocal /tmp/ta_demo/ii-out/part-00000 inverted_index.txt

# run the query script
./query.py inverted_index.txt

