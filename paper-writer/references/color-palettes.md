# Color Palettes for Academic Figures

Curated color palettes and plotting configuration for publication-quality academic figures. Load this file during M05 (Figures & Tables).

---

## Palettes

### Nature Style

Colors inspired by Nature journal figures. High contrast, professional appearance.

```python
NATURE = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#95C623']
# Blue, Purple, Orange, Red, Green
```

| Index | Hex | Name | Best For |
|-------|-----|------|----------|
| 0 | #2E86AB | Steel Blue | Primary data series, main method |
| 1 | #A23B72 | Mulberry | Secondary data series, comparison |
| 2 | #F18F01 | Amber | Highlights, key results |
| 3 | #C73E1D | Vermilion | Errors, negative results |
| 4 | #95C623 | Lime | Tertiary data, improvements |

### Cell Style

Colors inspired by Cell journal. Clean, modern, distinguishable.

```python
CELL = ['#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F', '#EDC948']
# Blue, Orange, Red, Teal, Green, Yellow
```

| Index | Hex | Name | Best For |
|-------|-----|------|----------|
| 0 | #4E79A7 | Muted Blue | Primary series |
| 1 | #F28E2B | Tangerine | Secondary series |
| 2 | #E15759 | Coral Red | Errors, baselines |
| 3 | #76B7B2 | Sage Teal | Tertiary series |
| 4 | #59A14F | Forest Green | Positive results |
| 5 | #EDC948 | Mustard | Additional series |

### Science Style

Colors inspired by Science journal. Subdued, professional, print-friendly.

```python
SCIENCE = ['#0C5DA5', '#FF9500', '#00B945', '#FF2C00', '#845B97', '#474747']
# Blue, Orange, Green, Red, Purple, Gray
```

| Index | Hex | Name | Best For |
|-------|-----|------|----------|
| 0 | #0C5DA5 | Deep Blue | Primary method |
| 1 | #FF9500 | Bright Orange | Key comparison |
| 2 | #00B945 | Vivid Green | Positive results |
| 3 | #FF2C00 | Signal Red | Errors, alerts |
| 4 | #845B97 | Muted Purple | Additional series |
| 5 | #474747 | Dark Gray | Baselines, references |

### Colorblind-Safe (Okabe-Ito)

The recommended palette for accessibility. Designed by Masataka Okabe and Kei Ito for deuteranopia, protanopia, and tritanopia.

```python
OKABE_ITO = ['#0077BB', '#33BBEE', '#009988', '#EE7733', '#CC3311', '#EE3377']
# Blue, Cyan, Teal, Orange, Red, Magenta
```

| Index | Hex | Name | Distinguishable By |
|-------|-----|------|--------------------|
| 0 | #0077BB | Blue | All types |
| 1 | #33BBEE | Cyan | All types |
| 2 | #009988 | Teal | All types |
| 3 | #EE7733 | Orange | All types |
| 4 | #CC3311 | Red | All types |
| 5 | #EE3377 | Magenta | All types |

**Full Okabe-Ito set** (8 colors):
```python
OKABE_ITO_FULL = [
    '#000000',  # Black
    '#E69F00',  # Orange
    '#56B4E9',  # Sky Blue
    '#009E73',  # Bluish Green
    '#F0E442',  # Yellow
    '#0072B2',  # Blue
    '#D55E00',  # Vermilion
    '#CC79A7',  # Reddish Purple
]
```

### Blue Gradient (for Heatmaps)

Sequential blue palette suitable for heatmaps, density plots, and single-variable visualizations.

```python
BLUE_GRADIENT = ['#A8DADC', '#6DAEDB', '#457B9D', '#2C5F7C', '#1D3557']
# Light to Dark
```

### Red-Blue Diverging (for Difference Maps)

```python
DIVERGING_RB = ['#B2182B', '#EF8A62', '#FDDBC7', '#F7F7F7', '#D1E5F0', '#67A9CF', '#2166AC']
# Red (negative) -> White (zero) -> Blue (positive)
```

---

## Usage Examples with Python Matplotlib

### Basic Line Plot

```python
import matplotlib.pyplot as plt
import numpy as np

# Choose palette
colors = ['#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F']

x = np.linspace(0, 10, 100)
methods = ['Ours', 'Baseline A', 'Baseline B', 'Baseline C', 'Baseline D']
linestyles = ['-', '--', '-.', ':', '-']
markers = ['o', 's', '^', 'D', 'v']

fig, ax = plt.subplots(figsize=(6, 4))
for i, (method, ls, mk) in enumerate(zip(methods, linestyles, markers)):
    y = np.sin(x + i * 0.5) + np.random.normal(0, 0.05, len(x))
    ax.plot(x, y, color=colors[i], linestyle=ls, marker=mk,
            markevery=15, markersize=6, linewidth=1.5, label=method)

ax.set_xlabel('Training Epochs')
ax.set_ylabel('Accuracy (%)')
ax.legend(frameon=False, fontsize=9)
ax.set_title('')  # Titles go in LaTeX captions, not in the figure
plt.tight_layout()
plt.savefig('comparison.pdf', dpi=450, bbox_inches='tight')
plt.close()
```

### Bar Chart with Error Bars

```python
import matplotlib.pyplot as plt
import numpy as np

colors = ['#4E79A7', '#F28E2B', '#E15759', '#76B7B2']
methods = ['Ours', 'Method A', 'Method B', 'Method C']
means = [92.3, 88.7, 85.2, 90.1]
stds = [0.8, 1.2, 1.5, 0.9]

fig, ax = plt.subplots(figsize=(5, 3.5))
bars = ax.bar(methods, means, yerr=stds, color=colors,
              edgecolor='black', linewidth=0.5, capsize=4, width=0.6)

# Highlight the best result
bars[0].set_edgecolor('black')
bars[0].set_linewidth(1.5)

ax.set_ylabel('Accuracy (%)')
ax.set_ylim(80, 96)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('bar_chart.pdf', dpi=450, bbox_inches='tight')
plt.close()
```

### Heatmap

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Custom blue gradient colormap
blue_colors = ['#A8DADC', '#6DAEDB', '#457B9D', '#2C5F7C', '#1D3557']
blue_cmap = LinearSegmentedColormap.from_list('academic_blue', blue_colors, N=256)

data = np.random.rand(8, 8)

fig, ax = plt.subplots(figsize=(5, 4))
im = ax.imshow(data, cmap=blue_cmap, aspect='auto')
cbar = plt.colorbar(im, ax=ax, shrink=0.8)
cbar.set_label('Value', fontsize=10)

ax.set_xlabel('Feature Index')
ax.set_ylabel('Sample Index')
plt.tight_layout()
plt.savefig('heatmap.pdf', dpi=450, bbox_inches='tight')
plt.close()
```

---

## Font Configuration

### Academic Fonts

The standard for academic figures is a serif font matching the paper body (Computer Modern, Times) or a clean sans-serif (Helvetica, Arial) for readability at small sizes.

### macOS Font Paths

```python
import matplotlib
import matplotlib.font_manager as fm

# Common Chinese font paths on macOS
CHINESE_FONTS_MACOS = {
    'SimSun':     '/System/Library/Fonts/Supplemental/Songti.ttc',      # 宋体
    'SimHei':     '/Library/Fonts/Microsoft/SimHei.ttf',                 # 黑体
    'STHeiti':    '/System/Library/Fonts/STHeiti Medium.ttc',            # 华文黑体
    'STSong':     '/System/Library/Fonts/Supplemental/Songti.ttc',      # 华文宋体
    'PingFang':   '/System/Library/Fonts/PingFang.ttc',                 # 苹方
    'Hiragino':   '/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc',      # Hiragino
}

# Register a Chinese font
def register_chinese_font(name='PingFang'):
    path = CHINESE_FONTS_MACOS.get(name)
    if path:
        fm.fontManager.addfont(path)
        return fm.FontProperties(fname=path)
    return None
```

### Windows Font Paths

```python
CHINESE_FONTS_WINDOWS = {
    'SimSun':   'C:/Windows/Fonts/simsun.ttc',     # 宋体
    'SimHei':   'C:/Windows/Fonts/simhei.ttf',     # 黑体
    'KaiTi':    'C:/Windows/Fonts/simkai.ttf',     # 楷体
    'FangSong': 'C:/Windows/Fonts/simfang.ttf',    # 仿宋
    'Microsoft YaHei': 'C:/Windows/Fonts/msyh.ttc', # 微软雅黑
}
```

### Linux Font Paths

```python
CHINESE_FONTS_LINUX = {
    'Noto Sans CJK': '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
    'WenQuanYi':     '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc',
}
```

---

## Global Style Setup Function

Use this function at the beginning of any figure generation script to ensure consistent, publication-quality styling.

```python
import matplotlib.pyplot as plt
import matplotlib as mpl

def setup_academic_style(
    font_size=10,
    title_size=12,
    label_size=10,
    tick_size=8,
    legend_size=9,
    dpi=450,
    font_family='serif',
    use_tex=False,
    chinese_support=False,
):
    """
    Configure matplotlib for publication-quality academic figures.

    Parameters
    ----------
    font_size : int
        Default font size for text elements.
    title_size : int
        Font size for titles (usually unused -- titles go in LaTeX captions).
    label_size : int
        Font size for axis labels.
    tick_size : int
        Font size for tick labels.
    legend_size : int
        Font size for legend entries.
    dpi : int
        Resolution for raster output. 450 DPI recommended for academic papers.
    font_family : str
        Font family: 'serif' (matches LaTeX body), 'sans-serif' (for clarity).
    use_tex : bool
        If True, use LaTeX for all text rendering (slower but exact match).
    chinese_support : bool
        If True, configure Chinese font support.
    """
    # Reset to defaults first
    mpl.rcdefaults()

    # Font configuration
    plt.rcParams.update({
        'font.size': font_size,
        'font.family': font_family,
        'axes.titlesize': title_size,
        'axes.labelsize': label_size,
        'xtick.labelsize': tick_size,
        'ytick.labelsize': tick_size,
        'legend.fontsize': legend_size,
    })

    # LaTeX rendering
    if use_tex:
        plt.rcParams.update({
            'text.usetex': True,
            'text.latex.preamble': r'\usepackage{amsmath}\usepackage{amssymb}',
        })

    # Chinese support
    if chinese_support:
        import platform
        system = platform.system()
        if system == 'Darwin':  # macOS
            plt.rcParams['font.sans-serif'] = ['PingFang SC', 'Hiragino Sans GB', 'Arial']
        elif system == 'Windows':
            plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial']
        else:  # Linux
            plt.rcParams['font.sans-serif'] = ['Noto Sans CJK SC', 'WenQuanYi Micro Hei', 'Arial']
        plt.rcParams['axes.unicode_minus'] = False  # Fix minus sign display

    # Figure quality
    plt.rcParams.update({
        'figure.dpi': 150,           # Screen display DPI
        'savefig.dpi': dpi,          # Output DPI (450 for publication)
        'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.05,
    })

    # Axes style
    plt.rcParams.update({
        'axes.linewidth': 0.8,
        'axes.spines.top': False,      # Remove top spine
        'axes.spines.right': False,    # Remove right spine
        'axes.grid': False,            # No grid by default
        'axes.axisbelow': True,        # Grid behind data
    })

    # Line and marker style
    plt.rcParams.update({
        'lines.linewidth': 1.5,
        'lines.markersize': 6,
    })

    # Legend style
    plt.rcParams.update({
        'legend.frameon': False,       # No frame around legend
        'legend.loc': 'best',
    })

    # Tick style
    plt.rcParams.update({
        'xtick.direction': 'in',
        'ytick.direction': 'in',
        'xtick.major.size': 4,
        'ytick.major.size': 4,
        'xtick.minor.size': 2,
        'ytick.minor.size': 2,
    })

    print(f"Academic style configured: {dpi} DPI, {font_family} font, "
          f"size {font_size}, {'LaTeX' if use_tex else 'matplotlib'} rendering")


# Quick usage:
# setup_academic_style()                           # Default: serif, 450 DPI
# setup_academic_style(use_tex=True)               # With LaTeX rendering
# setup_academic_style(chinese_support=True)        # With Chinese font support
# setup_academic_style(font_family='sans-serif')    # Sans-serif for presentations
```

---

## Recommended Figure Sizes

Standard sizes for common academic paper formats:

| Format | Single Column | Double Column | Full Width |
|--------|--------------|---------------|------------|
| NeurIPS/ICML/ICLR | 3.25" wide | N/A (single column) | 6.75" wide |
| ACL (two-column) | 3.3" wide | N/A | 6.8" wide |
| IEEE (two-column) | 3.5" wide | N/A | 7.16" wide |
| Elsevier (two-column) | 3.5" wide | N/A | 7.0" wide |

```python
# Figure size constants (width, height) in inches
FIG_SINGLE_COL = (3.25, 2.5)    # Single column figure
FIG_FULL_WIDTH = (6.75, 3.0)    # Full width figure
FIG_SQUARE = (3.25, 3.25)       # Square figure (e.g., confusion matrix)
FIG_WIDE = (6.75, 4.0)          # Wide figure (e.g., multi-panel comparison)
```

---

## Palette Selection Guide

| Scenario | Recommended Palette | Reason |
|----------|-------------------|--------|
| General comparison (2-5 methods) | Cell or Nature | High contrast, professional |
| Must be colorblind-safe | Okabe-Ito | Designed for all color vision types |
| Sequential data (heatmaps) | Blue Gradient | Clear ordering, print-friendly |
| Diverging data (difference maps) | Red-Blue Diverging | Clear positive/negative distinction |
| Grayscale-safe (print journal) | Use line styles + markers | Avoid relying on color alone |
| Presentation slides | Nature or Science | High contrast for projector |

### Rule of Thumb

1. Never use more than 6-7 colors in a single figure. If you need more, use subplots.
2. Always combine color with another visual channel (line style, marker shape, hatching) for accessibility.
3. Test your figure in grayscale before submission to print venues.
4. Avoid rainbow colormaps (jet/rainbow) -- they are not perceptually uniform and are colorblind-unfriendly.
