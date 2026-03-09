import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_multiple_convergences(folder_path, file_prefix="convergence", file_count=5):
    plt.figure(figsize=(10, 6))

    for i in range(file_count):
        file_path = os.path.join(folder_path, f"{file_prefix}{i}.csv")
        
        # Check if the file exists
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue

        # Load the CSV file into a DataFrame
        try:
            convergence_data = pd.read_csv(file_path)
        except Exception as e:
            print(f"Error reading the file {file_path}: {e}")
            continue

        # Check if the DataFrame is empty
        if convergence_data.empty:
            print(f"The file {file_path} is empty. Skipping.")
            continue

        # Plot the data with a unique label and color
        plt.plot(
            convergence_data['nfe'], 
            convergence_data['epsilon_progress'], 
            marker='o', 
            label=f"Convergence {i}"
        )

    # Add labels, title, legend, and grid
    plt.xlabel('Number of Function Evaluations (nfe)')
    plt.ylabel('Epsilon Progress')
    plt.title('Convergence Plots')
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()

# Example usage
if __name__ == "__main__":
    # Update this path to the directory containing your convergence files
    folder_path = "/Users/damlaakoluk/Zambezi-River-Basin-Multi-reservoir-EMODPS/ZambeziSmashPython/runs/BC_BC_pseudo_200000nfe_5seed"
    plot_multiple_convergences(folder_path)