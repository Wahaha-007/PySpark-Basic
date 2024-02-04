import os
from util import get_spark_session
from read import from_files

def main():
  env = os.environ.get('ENVIRON')
  spark = get_spark_session(env,'GitHub Activity - Getting Started')
  src_dir = os.environ.get('SRC_DIR')
  src_file_pattern = f'{os.environ.get("SRC_FILE_PATTERN")}-*'
  src_file_format = os.environ.get('SRC_FILE_FORMAT')

  df = from_files(spark,src_dir,src_file_pattern,src_file_format)
  print(env)
  print(type(spark))
  df.printSchema()
  df.select('repo.*').show()

  # Perform Spark operations here...
  # print(type(spark))
  # park.sql('SELECT current_date').show()

  # Stop the Spark session when done
  spark.stop()

if __name__ == '__main__':
  main()