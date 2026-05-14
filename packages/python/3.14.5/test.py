import io

import numpy as np
import pandas as pd
import scipy
import scipy.stats as stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import openpyxl
from PIL import Image

arr = np.array([1, 2, 3, 4, 5])
assert arr.mean() == 3.0

df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
assert df["a"].sum() == 6

_, p = stats.ttest_1samp([1, 2, 3, 4, 5], 0)
assert 0.0 < p < 1.0

fig, ax = plt.subplots()
ax.plot([0, 1], [0, 1])
buf = io.BytesIO()
fig.savefig(buf, format="png")
assert len(buf.getvalue()) > 0

wb = openpyxl.Workbook()
wb.active["A1"] = "hello"
buf = io.BytesIO()
wb.save(buf)
assert len(buf.getvalue()) > 0

img = Image.new("RGB", (8, 8), color=(255, 0, 0))
buf = io.BytesIO()
img.save(buf, format="PNG")
assert len(buf.getvalue()) > 0

print("OK")
