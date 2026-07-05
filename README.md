# student-assessment-report-skill

将多次考试学业数据转化为高质量可视化 HTML 学业评估报告的 AI Skill。

## 用途

- 输入：学生多次考试成绩表（Markdown 表格）+ 辅助参数（人数、满分等）
- 输出：包含五维雷达图、趋势图、四象限矩阵、风险信号的单文件 HTML 报告

## 核心特性

- **8 阶段严格工作流**：输入校验 → 数据清洗 → 缺失检测 → 派生指标计算 → 评级 → 报告生成 → 汇总表 → 自检
- **五维能力模型**：知识掌握力、排名竞争力、学科均衡度、进步动能、抗压稳定性
- **可视化丰富**：Chart.js 雷达图 + 趋势图 + CSS 四象限矩阵 + KPI 卡片
- **诚实边界**：数据缺失自动降级，推测必须标注，绝不编造

## 与 `student-grade-analyzer-skill` 的区别

| 维度 | 本 Skill | student-grade-analyzer-skill |
|------|---------|------------------------------|
| 定位 | 纯数据分析引擎 | 中考备战教育顾问 |
| 输出 | 统计报告 + 五维评级 | 升学预测 + 行动路线图 |
| 学段 | 任意学段 | 侧重初三/中考 |
| 核心逻辑 | 量化阈值表 + analysis_state | 竞争定位 + 概率预测 |

## 依赖

- 无外部依赖
- HTML 报告使用 CDN 加载 Chart.js（`chart.umd.min.js`）

## 输出路径

```
~/outputs/student-assessment-report-skill/YYYY-MM-DD-<描述>-学业评估报告.html
```
