import matplotlib.pyplot as plt

labels = ['step 1', 'step 2', 'step 3', 'step 4', 'step 5']
values = [100, 75, 50, 30, 10]

cumulative_values = [sum(values[:i + 1]) for i in range(len(values))]

color = ['blue', 'green', 'orange', 'purple']

fig, ax = plt.subplots()

for i in range(len(labels) - 1):  # Adjust the loop range
    ax.fill_betweenx([i, i + 1], cumulative_values[i], cumulative_values[i + 1], step='mid', alpha=0.5, color=color[i])

ax.set_yticks(range(len(labels)))
ax.set_yticklabels(labels)
ax.set_xlabel('conversion rate')

for i, value in enumerate(cumulative_values):
    ax.annotate(str(value), xy=(value, i), xytext=(5, 5), textcoords='offset points')

plt.title('funnel chart')
plt.show()