## DataQualityMonitor
- 一期目标，针对数据开发平台与数据质量监控平台数据没有打通的数据流处理场景。在数据同步任务或者数据开发任务的数据处理流程中，将数据质量问题在事先或者事中处理掉。

- 二期目标，围绕数据质量问题进行相关的运维与运营工作。参考下方的数据质量模块功能架构图。

## DAMA（Data Management Association）数据质量模型定义了数据质量的六个维度，它们是：
目标主流的厂商都是依据DAMA的数据质量理论基础进行产品的开发以满足的数据质量的监控要求。
### 准确性（Accuracy）：数据是否准确、精确，是否与现实世界中的事实一致。
### 完整性（Completeness）：数据是否完整，是否包含了所需的所有数据，没有遗漏。
### 一致性（Consistency）：数据在不同数据源、不同系统、不同时间点之间是否保持一致，是否符合逻辑关系。
### 及时性（Timeliness）：数据是否及时更新，是否在需要的时间内提供给用户。
### 唯一性（Uniqueness）：数据是否唯一，是否存在重复数据或重复记录。
### 有效性（Validity）：数据是否符合预定义的规则、约束条件，是否满足数据的有效性要求。
这些维度被广泛应用于数据质量评估和管理，可以帮助组织全面了解和监控数据质量，识别数据质量问题，并采取相应的纠正措施。

请注意，每个维度可能有不同的子维度或具体的指标，具体的实现方式和度量方法可能因组织和具体业务需求而有所不同。

DataQualityMonitor 是一个基于Python的数据质量监控工具，旨在帮助大数据架构师和数据工程师监测和维护数据的质量。该工具提供了一系列功能，包括常见维度数据质量监测、数据预警、数据异常信息记录与展示、失败重跑、元数据监控等。

## 数据质量监控产品功能特性

- **常见维度数据质量监测**：通过配置指标和规则，监测数据的常见维度质量，如完整性、准确性、一致性等。

- **数据预警，短信与邮件**：当数据质量异常时，系统能够及时发送预警通知，支持短信和邮件的形式。

- **数据异常信息记录与展示**：记录数据质量异常的详细信息，并提供可视化展示，帮助用户分析和排查问题。

- **失败重跑**：在数据处理过程中出现失败情况时，系统能够自动重跑失败的任务，保证数据处理的连续性和完整性。

- **工作流嵌入**：脚本可直接嵌入工作流中运行，实现开箱即用，方便集成到现有的数据处理流程中。

## 数据质量模块功能架构图

![image text](https://github.com/dingminghbut/DataQuality/blob/main/page/%E6%95%B0%E6%8D%AE%E8%B4%A8%E9%87%8F%E6%B5%81%E7%A8%8B%E6%9E%B6%E6%9E%84%E5%9B%BE.jpg "DBSCAN Performance Comparison")


## 数据质量规则（参考《华为数据之道》）
异常数据是不满足数据标准、不符合业务实质的客观存在的数据，如某位员工的国籍信息错误、某位客户的客户名称信息错误等。

数据在底层数据库多数是以二维表格的形式存储，每个数据格存储一个数据值。若想从众多数据中识别出异常数据，就需要通过数据质量规则给数据打上标签。

数据质量规则是判断数据是否符合数据质量要求的逻辑约束。在整个数据质量监控的过程中，数据质量规则的好坏直接影响监控的效果，因此如何设计数据质量规则很重要。

依据数据在数据库落地时的质量特性及数据质量规则类型，设计如下四类数据质量分类框架。

- 1) 单列数据质量规则。关注数据属性值的有无以及是否符合自身规范的逻辑判断。
- 2) 跨列数据质量规则。关注数据属性间关联关系的逻辑判断。
- 3) 跨行数据质量规则。关注数据记录之间关联关系的逻辑判断。
- 4) 跨表数据质量规则。关注数据集关联关系的逻辑判断。

华为结合IS08000数据质量标准、数据质量控制与评估原则(国标SY/T 7005-2014) ，共设计了15类规则：
![image text](https://github.com/dingminghbut/DataQuality/blob/main/page/%E6%95%B0%E6%8D%AE%E8%B4%A8%E9%87%8F%E8%A7%84%E5%88%99.jpg "DBSCAN Performance Comparison")
