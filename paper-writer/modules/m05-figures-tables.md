# Module 05: Figures and Tables

Figure generation and table data verification for publication-quality visual elements. This module covers Python-based figure creation with academic styling, TikZ diagram verification, table data cross-checking, and accessibility compliance.

## When to Load

Load this module when the user says: "figures", "plots", "tables", "TikZ", "diagram", "chart", "visualization", or when executing Stage S5 of a full paper writing project.

## Prerequisites

- Paper outline from Module 03 (to know which figures/tables are needed)
- Result data files identified from Module 01 (artifact mapping)
- Experiment results from Module 04 (for table content)

## Part A: Python Figure Generation

### Setup: Plot Style Function

Use this template as the foundation for all figures. It enforces academic standards for font sizing, resolution, and visual cleanliness.

```python
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from typing import Optional, Tuple

# Attempt to use SciencePlots for polished academic styling
try:
    import scienceplots
    plt.style.use(['science', 'no-latex'])  # 'ieee', 'nature', 'science' also available
except ImportError:
    pass  # Fall back to manual styling below


def setup_plot_style(
    fig_width: float = 3.5,        # Single column width in inches (3.5 for IEEE, 5.5 for full width)
    fig_height: Optional[float] = None,  # Auto-calculated from golden ratio if None
    font_size: int = 9,            # Base font size (8-10 for papers)
    font_family: str = 'serif',    # 'serif' for most journals, 'sans-serif' for some conferences
    dpi: int = 450,                # Publication quality: 300 minimum, 450 recommended
    use_grid: bool = True,
    grid_alpha: float = 0.3,
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Create a publication-ready figure with academic styling.

    Column widths by venue:
    - IEEE single column: 3.5 inches
    - IEEE double column: 7.16 inches
    - NeurIPS/ICML single column: 5.5 inches
    - Nature single column: 3.5 inches (89 mm)
    - Nature double column: 7.2 inches (183 mm)
    """
    if fig_height is None:
        golden_ratio = (1 + np.sqrt(5)) / 2
        fig_height = fig_width / golden_ratio

    # Global rcParams
    plt.rcParams.update({
        'font.size': font_size,
        'font.family': font_family,
        'axes.labelsize': font_size,
        'axes.titlesize': font_size + 1,
        'xtick.labelsize': font_size - 1,
        'ytick.labelsize': font_size - 1,
        'legend.fontsize': font_size - 1,
        'figure.dpi': dpi,
        'savefig.dpi': dpi,
        'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.02,
        'axes.linewidth': 0.8,
        'lines.linewidth': 1.5,
        'lines.markersize': 5,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.grid': use_grid,
        'grid.alpha': grid_alpha,
        'grid.linewidth': 0.5,
        'legend.frameon': False,
        'legend.borderaxespad': 0.5,
        'mathtext.fontset': 'stix',       # Math font consistent with serif text
        'axes.axisbelow': True,           # Grid behind data
        'figure.constrained_layout.use': True,  # Better than tight_layout
    })

    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    return fig, ax


def setup_subplot_style(
    nrows: int = 1,
    ncols: int = 2,
    fig_width: float = 7.16,
    fig_height: Optional[float] = None,
    **kwargs
) -> Tuple[plt.Figure, np.ndarray]:
    """Create a multi-panel figure with shared styling."""
    if fig_height is None:
        panel_height = (fig_width / ncols) / ((1 + np.sqrt(5)) / 2)
        fig_height = panel_height * nrows

    setup_plot_style(fig_width=fig_width, fig_height=fig_height, **kwargs)
    fig, axes = plt.subplots(nrows, ncols, figsize=(fig_width, fig_height))
    return fig, axes
```

### Save Figure Function

Always save in dual format (PNG for raster display, PDF/SVG for vector embedding in LaTeX).

```python
def save_figure(
    fig: plt.Figure,
    filename: str,
    output_dir: str = 'figures',
    formats: Tuple[str, ...] = ('pdf', 'png'),
    dpi: int = 450,
    transparent: bool = False,
) -> list:
    """
    Save figure in multiple formats for publication.

    Returns list of saved file paths.
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    saved_files = []
    for fmt in formats:
        filepath = output_path / f"{filename}.{fmt}"
        fig.savefig(
            filepath,
            format=fmt,
            dpi=dpi if fmt == 'png' else None,  # DPI only matters for raster
            bbox_inches='tight',
            pad_inches=0.02,
            transparent=transparent,
        )
        saved_files.append(str(filepath))

    plt.close(fig)
    return saved_files
```

### Color Palettes

Use research-publication-appropriate color palettes. Each palette is designed for specific journal families and optimized for readability.

```python
# ============================================================
# Color Palettes for Academic Publications
# ============================================================

PALETTES = {
    # Nature-style: Clean blues and warm accents
    'nature': [
        '#4C72B0',  # Steel blue
        '#DD8452',  # Warm orange
        '#55A868',  # Sage green
        '#C44E52',  # Muted red
        '#8172B3',  # Lavender purple
        '#937860',  # Taupe brown
        '#DA8BC3',  # Rose pink
        '#8C8C8C',  # Gray
        '#CCB974',  # Gold
        '#64B5CD',  # Sky blue
    ],

    # Cell-style: Vibrant, Tableau-like
    'cell': [
        '#1F77B4',  # Tableau blue
        '#FF7F0E',  # Tableau orange
        '#2CA02C',  # Tableau green
        '#D62728',  # Tableau red
        '#9467BD',  # Tableau purple
        '#8C564B',  # Tableau brown
        '#E377C2',  # Tableau pink
        '#7F7F7F',  # Tableau gray
        '#BCBD22',  # Tableau olive
        '#17BECF',  # Tableau cyan
    ],

    # Science-style: High contrast, fewer colors
    'science': [
        '#0C5DA5',  # Deep blue
        '#FF2C00',  # Bright red
        '#00B945',  # Green
        '#FF9500',  # Orange
        '#845B97',  # Purple
        '#474747',  # Dark gray
        '#9E9E9E',  # Light gray
    ],

    # Colorblind-safe: Okabe-Ito palette
    # Recommended for all publications. Safe for protanopia, deuteranopia, tritanopia.
    'colorblind': [
        '#E69F00',  # Orange
        '#56B4E9',  # Sky blue
        '#009E73',  # Bluish green
        '#F0E442',  # Yellow
        '#0072B2',  # Blue
        '#D55E00',  # Vermilion
        '#CC79A7',  # Reddish purple
        '#000000',  # Black
    ],

    # Grayscale-safe: For print journals that may reproduce in B&W
    'grayscale': [
        '#000000',  # Black
        '#404040',  # Dark gray
        '#808080',  # Medium gray
        '#BFBFBF',  # Light gray
        '#E0E0E0',  # Very light gray
    ],
}


def get_palette(name: str = 'colorblind', n_colors: int = None) -> list:
    """
    Get a color palette by name.

    Args:
        name: Palette name ('nature', 'cell', 'science', 'colorblind', 'grayscale')
        n_colors: Number of colors needed. If more than available, cycles.

    Returns:
        List of hex color strings.
    """
    palette = PALETTES.get(name, PALETTES['colorblind'])
    if n_colors is None:
        return palette
    if n_colors <= len(palette):
        return palette[:n_colors]
    # Cycle if more colors needed than available
    return [palette[i % len(palette)] for i in range(n_colors)]


def set_palette(name: str = 'colorblind'):
    """Set the default color cycle for matplotlib."""
    palette = get_palette(name)
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=palette)
```

### Chinese Font Configuration

For papers requiring Chinese characters in figures (bilingual papers, Chinese journals).

```python
def setup_chinese_fonts(platform: str = 'auto'):
    """
    Configure matplotlib to display Chinese characters.

    Args:
        platform: 'macos', 'windows', 'linux', or 'auto' for detection.
    """
    import platform as pf

    if platform == 'auto':
        system = pf.system()
        platform = {'Darwin': 'macos', 'Windows': 'windows', 'Linux': 'linux'}.get(system, 'linux')

    font_config = {
        'macos': {
            'sans-serif': ['Arial Unicode MS', 'PingFang SC', 'Heiti SC', 'STHeiti'],
            'serif': ['Songti SC', 'STSong', 'SimSun'],
            'monospace': ['Menlo', 'Monaco'],
            'fallback_path': '/System/Library/Fonts/PingFang.ttc',
        },
        'windows': {
            'sans-serif': ['Microsoft YaHei', 'SimHei', 'DengXian'],
            'serif': ['SimSun', 'NSimSun', 'KaiTi'],
            'monospace': ['Consolas'],
            'fallback_path': 'C:/Windows/Fonts/msyh.ttc',
        },
        'linux': {
            'sans-serif': ['WenQuanYi Micro Hei', 'Noto Sans CJK SC', 'Droid Sans Fallback'],
            'serif': ['Noto Serif CJK SC', 'AR PL UMing CN'],
            'monospace': ['WenQuanYi Micro Hei Mono'],
            'fallback_path': '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc',
        },
    }

    config = font_config.get(platform, font_config['linux'])

    plt.rcParams['font.sans-serif'] = config['sans-serif'] + plt.rcParams.get('font.sans-serif', [])
    plt.rcParams['font.serif'] = config['serif'] + plt.rcParams.get('font.serif', [])
    plt.rcParams['axes.unicode_minus'] = False  # Fix minus sign display with CJK fonts

    # Verify font availability
    from matplotlib.font_manager import FontManager
    fm = FontManager()
    available = [f.name for f in fm.ttflist]
    for family in ['sans-serif', 'serif']:
        for font_name in config[family]:
            if font_name in available:
                return font_name

    # If no named font found, try direct file path
    fallback = config.get('fallback_path', '')
    if Path(fallback).exists():
        from matplotlib.font_manager import FontProperties
        return FontProperties(fname=fallback)

    print(f"WARNING: No Chinese font found for platform '{platform}'. "
          f"Install one of: {config['sans-serif']}")
    return None
```

### Common Figure Templates

**Bar chart comparison (baseline vs. ours):**
```python
def plot_comparison_bars(methods, metrics, metric_name, ours_index=-1, filename='comparison'):
    """Plot grouped bar chart comparing methods on a single metric."""
    fig, ax = setup_plot_style(fig_width=5.5)
    colors = get_palette('colorblind', len(methods))
    # Highlight "ours" with a distinct pattern
    edge_colors = ['black' if i == ours_index else 'none' for i in range(len(methods))]
    edge_widths = [1.5 if i == ours_index else 0 for i in range(len(methods))]

    bars = ax.bar(range(len(methods)), metrics, color=colors,
                  edgecolor=edge_colors, linewidth=edge_widths)
    ax.set_xticks(range(len(methods)))
    ax.set_xticklabels(methods, rotation=30, ha='right')
    ax.set_ylabel(metric_name)

    # Add value labels on bars
    for bar, val in zip(bars, metrics):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01 * max(metrics),
                f'{val:.1f}', ha='center', va='bottom', fontsize=7)

    return save_figure(fig, filename)
```

**Training curve plot:**
```python
def plot_training_curves(data_dict, xlabel='Epoch', ylabel='Loss', filename='training_curve'):
    """Plot training curves for multiple runs/methods.

    Args:
        data_dict: {'Method A': (epochs_array, values_array), 'Method B': ...}
    """
    fig, ax = setup_plot_style()
    colors = get_palette('colorblind', len(data_dict))

    for (name, (x, y)), color in zip(data_dict.items(), colors):
        ax.plot(x, y, label=name, color=color)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()
    return save_figure(fig, filename)
```

## Part B: TikZ Diagram Verification

TikZ diagrams (architecture diagrams, pipeline figures, flowcharts) are common in ML papers. They must be verified for consistency with the paper text.

### Verification Procedure

1. **Locate all TikZ files**: Search for `\begin{tikzpicture}` in the main `.tex` file and for standalone `.tex` files in `figures/` directory.

2. **Cross-reference labels and nodes**: For each TikZ diagram:
   ```
   For each node/label in the TikZ source:
   a. Check: does this term appear in the Methods section?
   b. Check: is the spelling and capitalization consistent?
   c. Check: if the node represents a component, does the paper describe it?
   d. Check: if the node has a mathematical symbol, does it match the paper's notation?
   ```

3. **Check architectural details**: For architecture diagrams specifically:
   ```
   a. All layers/components mentioned in Methods section 3.2-3.3 appear in the diagram
   b. Activation functions are labeled (ReLU, GELU, etc.) if mentioned in text
   c. Normalization layers are shown if described in text
   d. Input/output dimensions match the text description
   e. Data flow direction is clear and consistent
   f. Skip connections, residual paths, attention mechanisms are all shown if described
   ```

4. **Check terminology consistency**: Build a terminology map:
   ```markdown
   | Paper Term | TikZ Node Text | Match? |
   |---|---|---|
   | "encoder" | "Encoder" | Yes (case-insensitive OK in figures) |
   | "multi-head attention" | "MHA" | Verify abbreviation is defined in caption |
   | "feature extraction" | "Feature Extractor" | Minor mismatch -- standardize |
   ```

5. **Common TikZ errors to flag:**
   - Node labels using outdated method names (from earlier drafts)
   - Missing connections between components that the text says are connected
   - Color meanings not explained in the caption
   - Font size too small to read at print scale (minimum 7-8pt equivalent)
   - Inconsistent arrow styles (solid vs. dashed without semantic meaning)

### TikZ Quality Checklist

- [ ] Every node label matches paper terminology exactly
- [ ] All components described in Methods appear in the diagram
- [ ] Mathematical notation in nodes matches paper notation
- [ ] Colors are consistent across all figures in the paper
- [ ] The caption is self-contained (explains what each component/color means)
- [ ] Font size is readable at print scale
- [ ] No orphan nodes (disconnected from the main diagram without explanation)

## Part C: Table Data Verification

Tables in ML papers frequently contain numerical errors due to copy-paste mistakes, rounding inconsistencies, or outdated results. Every number must be verified.

### Verification Procedure

1. **Identify all tables**: Search the `.tex` file for `\begin{table}` and `\begin{tabular}`.

2. **Locate source data**: For each table, find the corresponding data source:
   ```
   Search patterns:
   - results/*.json, results/*.csv, results/*.yaml
   - outputs/*/metrics.json
   - logs/*/eval_results.txt
   - wandb/*/files/summary.json
   - Any Python scripts that print or save results
   ```

3. **Parse and compare**: For each table:
   ```
   a. Parse the LaTeX table to extract all numerical values and their positions
      (row label, column header, value)
   b. Find the corresponding value in the source data file
   c. Compare: do they match within reasonable rounding?
      - 1 decimal place: round(source, 1) == table_value
      - 2 decimal places: round(source, 2) == table_value
      - Percentage vs. decimal: 0.953 in source == 95.3 in table
   d. Flag any discrepancies with exact location:
      "Table 1, row 'Ours', column 'Accuracy': table says 95.3, source says 95.1"
   ```

4. **Verify formatting conventions**:
   ```
   a. Best result per column: should be in \textbf{bold}
   b. Second-best result: should be \underline{underlined} (if this convention is used)
   c. Check that bold/underline are correct after any number corrections
   d. Units in column headers, not in cells
   e. Decimal alignment: all values in a column have the same number of decimal places
   f. +/- notation for standard deviations: consistent formatting (e.g., $95.3 \pm 0.2$)
   ```

5. **Verify table captions**:
   ```
   a. Caption describes what the table shows
   b. Caption explains any abbreviations used in the table
   c. Caption explains bold/underline conventions
   d. Caption is above the table (standard convention)
   e. Caption mentions the evaluation metric and dataset
   ```

### Table Quality Checklist

- [ ] Every number matches its source data file
- [ ] Bold correctly indicates best result per column
- [ ] Underline correctly indicates second-best (if used)
- [ ] Consistent decimal places within each column
- [ ] Units in headers, not in cells
- [ ] Standard deviations included where applicable
- [ ] Caption is self-contained and above the table
- [ ] Table uses booktabs style (`\toprule`, `\midrule`, `\bottomrule`, no vertical lines)
- [ ] Table is referenced in the text with `Table~\ref{tab:...}`

## Part D: Figure Accessibility

All figures must be accessible to readers with color vision deficiencies and readable in grayscale printing.

### Accessibility Checklist

1. **Colorblind safety**: Use the Okabe-Ito palette (provided above) or test with a colorblind simulator.
   - Tools: `colorspacious` Python package, Coblis web simulator (https://www.color-blindness.com/coblis-color-blindness-simulator/)
   - Rule of thumb: if two data series are distinguished only by red vs. green, change one.

2. **Grayscale readability**: In addition to color, use at least one other visual differentiator:
   - Different line styles: solid, dashed, dotted, dash-dot
   - Different marker shapes: circle, square, triangle, diamond, star
   - Different fill patterns for bars: solid, hatched, cross-hatched

3. **Self-contained captions**: The caption should explain:
   - What the figure shows (the data, not the conclusion)
   - What each color/marker/line style represents
   - Any non-obvious conventions (e.g., "higher is better", log scale)
   - The key observation the reader should notice

4. **No titles inside figures**: The figure caption serves as the title. Matplotlib's `ax.set_title()` should generally not be used in publication figures; it duplicates the caption and wastes space.

5. **Font consistency**: Figure text (axis labels, tick labels, legends) should use the same font family and similar sizes as the paper body text. The `setup_plot_style` function above handles this.

6. **Print size**: All text in the figure must be readable at the final print size. For a single-column figure (3.5 inches wide), the minimum font size is approximately 7-8pt.

### Accessibility Verification Code

```python
def check_figure_accessibility(fig_path: str) -> dict:
    """
    Basic accessibility checks for a saved figure.
    Returns a dict of check results.
    """
    from PIL import Image
    import numpy as np

    checks = {}
    img = Image.open(fig_path)
    img_array = np.array(img)

    # Check resolution
    dpi = img.info.get('dpi', (72, 72))
    checks['resolution'] = {
        'dpi': dpi,
        'pass': min(dpi) >= 300,
        'note': f"DPI is {min(dpi)}. Minimum 300 required for print."
    }

    # Check if image has sufficient contrast
    if len(img_array.shape) == 3:
        gray = np.mean(img_array[:, :, :3], axis=2)
    else:
        gray = img_array
    contrast = gray.std()
    checks['contrast'] = {
        'std': float(contrast),
        'pass': contrast > 30,
        'note': f"Grayscale contrast (std): {contrast:.1f}. Low values may indicate poor readability."
    }

    # Check image dimensions
    width_inches = img.width / max(dpi)
    checks['size'] = {
        'width_inches': width_inches,
        'pass': 3.0 <= width_inches <= 8.0,
        'note': f"Width: {width_inches:.1f} inches. Standard range: 3.5-7.2 inches."
    }

    return checks
```

## Recommended Tools

| Tool | Purpose | Install |
|---|---|---|
| matplotlib | Core plotting library | `pip install matplotlib` |
| SciencePlots | Academic plot styles (IEEE, Nature, Science) | `pip install SciencePlots` |
| seaborn | Statistical visualizations, built on matplotlib | `pip install seaborn` |
| PlotNeuralNet | LaTeX/TikZ neural network architecture diagrams | `git clone https://github.com/HarisIqbal88/PlotNeuralNet` |
| tikzplotlib | Convert matplotlib figures to TikZ code | `pip install tikzplotlib` |
| Pillow | Image processing and accessibility checks | `pip install Pillow` |
| colorspacious | Color vision deficiency simulation | `pip install colorspacious` |

## Deliverables

Upon completing this module:

1. **Publication-quality figures** saved in `figures/` directory:
   - Dual format: PDF (vector) + PNG (450 DPI raster)
   - Consistent styling across all figures
   - Colorblind-safe palette
   - Self-contained captions
2. **Verified tables**: All numerical data cross-checked against source files, with a verification report listing any discrepancies found and resolved.
3. **TikZ verification report**: Terminology consistency check, missing components check, and any corrections made.
4. **`plan/progress.md`** updated with:
   - S5 Figures & Tables: COMPLETE
   - List of generated figures with file paths
   - Table verification status (all passed / discrepancies found and corrected)
   - TikZ verification status
   - Next action: proceed to S6 (Citation Management)

## Common Pitfalls

- **Pitfall:** Using default matplotlib colors (the old "vomit-green" default cycle). Always set an explicit academic palette.
- **Pitfall:** Figures with text too small to read at print size. A figure that looks good on a 27-inch monitor may be unreadable in a two-column paper. Always check at the target print width.
- **Pitfall:** Inconsistent figure styles across the paper (different fonts, different color schemes, different grid styles). Use the `setup_plot_style` function for every figure to enforce consistency.
- **Pitfall:** Table numbers that do not match the source data. This is the single most common error in ML paper tables. Always verify programmatically, not by eye.
- **Pitfall:** Using `ax.set_title()` in publication figures. The LaTeX caption is the title. Internal titles waste vertical space and create redundancy.
- **Pitfall:** Relying solely on color to distinguish data series. Always add a secondary differentiator (line style, marker shape, or pattern fill) for accessibility.
