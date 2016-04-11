from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

plt.figure(figsize=(12, 8))
l100 = list(range(0, 100))
users = list()
data = list()
for userf in Path('./').iterdir():
    if userf.is_dir() and userf.name != '.git':
        users.append(userf.name)
        userd = list()
        data.append(userd)
        for i in range(1, 11):
            count = 0
            for j in l100[(i - 1) * 10:i * 10:]:
                p = Path(userf.name + '/chapter{:0>2}/knock{:0>2}.py'.format(i, j))
                if p.exists():
                    count += 1
            userd.append(count)
data = np.array(data, dtype=int)

ind = np.arange(len(data))
width = 0.35
labels = list('chapter{:0>2}'.format(i) for i in range(1, 11))

ax = plt.gca()
bottom = np.zeros(data.shape[0])
for i in range(data.shape[1]):
    plt.bar(ind,              # left pos x
            data[:, i],       # height
            width,            # width
            bottom,           # offset of height
            color=cm.Accent(i/10),  # color
            label=labels[i]   # label
            )
    for j in range(len(data)):
        if data[j, i] != 0:
            ann = ax.annotate(str(data[j, i]), xy = (ind[j] - 3 * width / 10, bottom[j] + data[j, i] * 0.45), fontsize = 12)
    bottom += data[:, i]

plt.xticks(ind + width / 2, users)
margin = 0.25
plt.xlim(-margin, len(data) - 1 + width + margin)
plt.ylim([0, 100])
plt.ylabel('Total')
plt.yticks(range(0, 101, 10))
handles, labels = ax.get_legend_handles_labels()
plt.legend(handles[::-1], labels[::-1], loc='upper right', bbox_to_anchor=(1.24, 1))
plt.subplots_adjust(right=0.83)
plt.grid(True)
plt.savefig('progress.png')
