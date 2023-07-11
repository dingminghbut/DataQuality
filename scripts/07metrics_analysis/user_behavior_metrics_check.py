from pyspark.sql import SparkSession

# 创建SparkSession
spark = SparkSession.builder.getOrCreate()

# 从CSV文件读取数据，并创建DataFrame
df = spark.read.csv('../../data/05metrics_statistics/user_behavior_metrics.csv', header=True, inferSchema=True)

# 注册DataFrame为临时视图
df.createOrReplaceTempView("metrics")

# 执行SparkSQL查询
query = """
    SELECT IMEI,
        COUNT(1) AS Count,
        SUM(Login) AS Login_Sum,
        MAX(Login) AS Login_Max,
        MIN(Login) AS Login_Min,
        AVG(Login) AS Login_Avg,
        VARIANCE(Login) AS Login_Variance,
        APPROX_PERCENTILE(Login, 0.5) AS Login_Median,
        SUM(Browse) AS Browse_Sum,
        MAX(Browse) AS Browse_Max,
        MIN(Browse) AS Browse_Min,
        AVG(Browse) AS Browse_Avg,
        VARIANCE(Browse) AS Browse_Variance,
        APPROX_PERCENTILE(Browse, 0.5) AS Browse_Median,
        SUM(AppInstall) AS AppInstall_Sum,
        MAX(AppInstall) AS AppInstall_Max,
        MIN(AppInstall) AS AppInstall_Min,
        AVG(AppInstall) AS AppInstall_Avg,
        VARIANCE(AppInstall) AS AppInstall_Variance,
        APPROX_PERCENTILE(AppInstall, 0.5) AS AppInstall_Median,
        SUM(AppActive) AS AppActive_Sum,
        MAX(AppActive) AS AppActive_Max,
        MIN(AppActive) AS AppActive_Min,
        AVG(AppActive) AS AppActive_Avg,
        VARIANCE(AppActive) AS AppActive_Variance,
        APPROX_PERCENTILE(AppActive, 0.5) AS AppActive_Median,
        Date
    FROM metrics
    GROUP BY IMEI,Date
    ORDER BY IMEI,Date
"""

imei_stats = spark.sql(query)

# 展示结果
imei_stats.show()
