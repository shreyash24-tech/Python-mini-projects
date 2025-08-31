import numpy as np

# Define the matrix
A = np.array([[2, 1],
              [1, 2]])

# Eigenvalues and Eigenvectors
eigvals, eigvecs = np.linalg.eig(A)

print("Eigenvalues:")
print(eigvals)

print("\nEigenvectors (columns correspond to eigenvalues):")
print(eigvecs)

# Diagonalization
P = eigvecs
D = np.diag(eigvals)
P_inv = np.linalg.inv(P)

print("\nDiagonal matrix D:")
print(D)

print("\nVerification (P^-1 * A * P):")
print(P_inv @ A @ P)
