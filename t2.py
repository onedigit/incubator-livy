import os

from pyspark.sql import HiveContext
from pyspark.streaming import StreamingContext
import pyspark.cloudpickle as cloudpickle

from py4j.java_gateway import java_import, JavaGateway, GatewayClient
from pyspark.conf import SparkConf
from pyspark.context import SparkContext
from pyspark.sql import SQLContext, HiveContext, Row

print("Connecting to gateway")
gateway_port = int(36503)
try:
    from py4j.java_gateway import GatewayParameters
    gateway_secret = "4RkGTtJ03tla3CCIVWbH/hVKYcnr8z07+xPg/sb/wj4="
    gateway = JavaGateway(gateway_parameters=GatewayParameters(
        port=gateway_port, auth_token=gateway_secret, auto_convert=True))
except:
    gateway = JavaGateway(GatewayClient(port=gateway_port), auto_convert=True)

print("Connected to gateway")

# java_import(gateway.jvm, "org.apache.spark.SparkConf")
# java_import(gateway.jvm, "org.apache.spark.api.java.*")
# java_import(gateway.jvm, "org.apache.spark.api.python.*")
# java_import(gateway.jvm, "org.apache.spark.mllib.api.python.*")
# java_import(gateway.jvm, "org.apache.spark.sql.*")
# java_import(gateway.jvm, "org.apache.spark.sql.hive.*")
# java_import(gateway.jvm, "scala.Tuple2")

print("Creating jsc")

jsc = gateway.entry_point.sc()
jconf = gateway.entry_point.sc().getConf()

jsqlc = gateway.entry_point.hivectx() if gateway.entry_point.hivectx() is not None \
    else gateway.entry_point.sqlctx()

conf = SparkConf(_jvm = gateway.jvm, _jconf = jconf)
sc = SparkContext(jsc=jsc, gateway=gateway, conf=conf)

print("ready...")
