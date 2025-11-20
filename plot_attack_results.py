import matplotlib.pyplot as plt

# Attack proportions and number of malicious clients
props = [0, 0.1, 0.3, 0.5]
n_clients = 10
x_values = [int(p * n_clients) for p in props]   # [0,1,3,5]


###############################################################################
# 1) Load results WITHOUT DEFENSE
###############################################################################
accs = []

print("\n===== Loading results: NO DEFENSE =====")
for p in props:
    # folders: mnist_non_iid_prop_0, mnist_non_iid_prop_0.1, ...
    folder = f"logs/mnist_non_iid_prop_{p}"
    filename = f"{folder}/final_acc.txt"

    try:
        with open(filename, "r") as f:
            acc = float(f.read().strip())
            accs.append(acc)
            print(f"[NO DEFENSE] prop={p} acc={acc}")
    except Exception as e:
        print(f"[NO DEFENSE] Missing {filename}: {e}")
        accs.append(None)


###############################################################################
# 2) Load results WITH MEDIAN DEFENSE
###############################################################################
median_accs = []

print("\n===== Loading results: MEDIAN DEFENSE =====")
for p in props:
    # non-iid folders: mnist_median_prop_non_iid_0_1 etc
    if p == 0:
        folder = "logs/mnist_median_prop_non_iid_0"
    else:
        safe_p = str(p).replace(".", "_")
        folder = f"logs/mnist_median_prop_non_iid_{safe_p}"

    filename = f"{folder}/final_acc.txt"

    try:
        with open(filename, "r") as f:
            acc = float(f.read().strip())
            median_accs.append(acc)
            print(f"[MEDIAN] prop={p} acc={acc}")
    except Exception as e:
        print(f"[MEDIAN] Missing {filename}: {e}")
        median_accs.append(None)


###############################################################################
# 3) Plot both curves
###############################################################################
plt.figure(figsize=(8,6))
plt.plot(x_values, accs, marker="o", linewidth=2, label="No Defense")
plt.plot(x_values, median_accs, marker="s", linewidth=2, label="Median Defense")

plt.title("Accuracy vs Number of Malicious Clients (Non-IID)")
plt.xlabel("Number of Malicious Clients")
plt.ylabel("Final Test Accuracy")
plt.grid(True)
plt.xticks(x_values)
plt.legend()
plt.tight_layout()
plt.show()
