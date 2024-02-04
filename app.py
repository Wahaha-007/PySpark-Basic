import os
from util import get_spark_session

def main():
  env = os.environ.get('ENVIRON')
  spark = get_spark_session(env,'GitHub Activity - Getting Started')

  # Perform Spark operations here...
  # print(type(spark))
  spark.sql('SELECT current_date').show()

  # Stop the Spark session when done
  spark.stop()

if __name__ == '__main__':
  main()