# DataQuality
# DataQualityMonitor

DataQualityMonitor 是一个基于Python的数据质量监控工具，旨在帮助大数据架构师和数据工程师监测和维护数据的质量。该工具提供了一系列功能，包括常见维度数据质量监测、数据预警、数据异常信息记录与展示、失败重跑、元数据监控等。

## 功能特性

- **常见维度数据质量监测**：通过配置指标和规则，监测数据的常见维度质量，如完整性、准确性、一致性等。

- **数据预警，短信与邮件**：当数据质量异常时，系统能够及时发送预警通知，支持短信和邮件的形式。

- **数据异常信息记录与展示**：记录数据质量异常的详细信息，并提供可视化展示，帮助用户分析和排查问题。

- **失败重跑**：在数据处理过程中出现失败情况时，系统能够自动重跑失败的任务，保证数据处理的连续性和完整性。

- **元数据监控**：监控和追踪数据的元数据信息，包括数据来源、数据格式、数据版本等，以保证数据的可追溯性和一致性。

- **工作流嵌入**：脚本可直接嵌入工作流中运行，实现开箱即用，方便集成到现有的数据处理流程中。

## 使用示例

下面是一个简单的使用示例，演示如何运行 DataQualityMonitor 脚本：

1. 安装依赖：

pip install dataqualitymonitor


2. 编写配置文件 `config.yaml`，配置数据监控指标和规则：

```yaml
# 数据指标配置
indicators:
  - name: 完整性检查
    type: completeness
    threshold: 0.9

  - name: 准确性检查
    type: accuracy
    threshold: 0.95

# 数据规则配置
rules:
  - name: 质量规则1
    indicator: 完整性检查
    condition: col1 is null

  - name: 质量规则2
    indicator: 准确性检查
    condition: col2 > 100
```
3.运行监控脚本：
python data_quality_monitor.py --config config.yaml

脚本会读取配置文件中的指标和规则，对数据进行质量监控，并根据设定的阈值和条件发出预警通知。
