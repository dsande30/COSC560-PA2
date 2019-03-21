sudo apt-get install default-jdk
export HADOOP_HOME=/usr/local/hadoop-2.7.6/
export JAVA_HOME=/usr/lib/jvm/default-java
export PATH=${JAVA_HOME}/bin:${HADOOP_HOME}/bin:${PATH}
echo "this is a test file with some of the words repeated this is a file with with with to test" > book.txt
hadoop fs -mkdir /tmp/akarnauc
hadoop fs -copyFromLocal book.txt /tmp/akarnauc/book.txt
