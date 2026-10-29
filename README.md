# Shapley-Variance-Decomposition

青藏高原东北部 WLR17 剖面代用指标的 Shapley 方差分解：把总解释方差拆成粒度（Grain size）、物源（Provenance）、稀释（Dilution）、年龄（Age）四组，剩下的记为未解释残差。

## 图

`figures/Shapley_variance_decomposition.tiff`（300 dpi，12 MB）

- 左：单一预测因子的 $R^2$，按所属因子组着色
- 右：四组 Shapley 贡献的堆叠柱，图例放在插图右侧的空白区，不压主图

## 分解结果

| 组 | 贡献 | 组内单一因子（$R^2$） |
| --- | --- | --- |
| Grain size | 36.3% | Fine/Coarse silt 0.327、Mean grain size 0.018、Clay (<8 µm) 0.015 |
| Provenance | 8.7% | Zr/Hf 0.012、Nb/Ta 0.010、Th/Sc 0.008 |
| Dilution | 8.4% | CaO 0.007、TOC 0.005 |
| Age | 0.6% | Age 0.0002 |
| Unexplained | 46.1% | — |

单一因子的 $R^2$ 与组贡献不能相加：前者是单变量回归各自解释的量，后者是在全模型下按 Shapley 值分摊的边际贡献。

## 脚本

```
scripts/shapley_variance_decomposition.py   出图脚本，产出 figures/ 下那张 TIFF
```

脚本不读外部数据，`R²` 与组贡献都写在脚本顶部的 Data 段，改数值后重跑即可。输出路径由 `out_dir` / `out_file` 两个变量控制（默认 `E:\WLR17\论文\图`），换机器前改成自己的路径。

## 运行

```bash
pip install numpy matplotlib
python scripts/shapley_variance_decomposition.py
```

生成环境：Python + matplotlib 3.11.2、numpy 2.5.3，字体 Times New Roman，绘图参数与入库文件一致（同一脚本重跑得到逐字节相同的 TIFF）。

## 配色

| 用途 | 色值 |
| --- | --- |
| Grain size | `#300a8b` |
| Provenance | `#3132f0` |
| Dilution | `#b7cfe7` |
| Age | `#d2625f` |
| Unexplained / 网格底 | `#e0e0e0` |

## 相关

同剖面的 PCA 分析见 [tang200312/Paleoclimate-PCA](https://github.com/tang200312/Paleoclimate-PCA)。