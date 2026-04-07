import matplotlib.pyplot as plt

def plot_chart():
    labels = ["Assets", "Liabilities", "Debt"]
    values = [100, 70, 50]
    
    plt.figure()
    plt.bar(labels, values)
    plt.title("Financial Overview")
    
    return plt