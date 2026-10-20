
# Week 1: Thermal Conductivity Comparison
# Comparing diamond, copper, aluminium and stainless steel
# Using Fourier's Law of Heat Conduction

import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. MATERIAL PROPERTIES
# --------------------------------------------------

# Representative thermal conductivity values (W/mK)
materials = {
    "Diamond": 2000,
    "Copper": 400,
    "Aluminium": 237,
    "Stainless Steel": 16
}

# --------------------------------------------------
# 2. EXPERIMENTAL CONDITIONS
# --------------------------------------------------

area = 0.01          # Cross-sectional area (m²)
thickness = 0.01     # Material thickness (m)
temp_hot = 100       # Hot-side temperature (°C)
temp_cold = 50       # Cold-side temperature (°C)

# Temperature difference
delta_T = temp_hot - temp_cold

print("THERMAL CONDUCTIVITY COMPARISON")
print("--------------------------------")
print(f"Temperature difference: {delta_T} K")
print(f"Area: {area} m²")
print(f"Thickness: {thickness} m")

# --------------------------------------------------
# 3. FOURIER'S LAW
# --------------------------------------------------

# Q = (k * A * delta_T) / L

def heat_transfer(k, area, delta_T, thickness):
    Q = (k * area * delta_T) / thickness
    return Q

# --------------------------------------------------
# 4. CALCULATE HEAT TRANSFER
# --------------------------------------------------

heat_results = {}

print("\nHeat Transfer Results:")
print("--------------------------------")

for material, k in materials.items():
    Q = heat_transfer(k, area, delta_T, thickness)
    heat_results[material] = Q
    print(f"{material}: {Q:,.2f} W")

# --------------------------------------------------
# 5. COMPARE MATERIALS
# --------------------------------------------------

diamond = heat_results["Diamond"]
copper = heat_results["Copper"]
aluminium = heat_results["Aluminium"]
steel = heat_results["Stainless Steel"]

print("\nEngineering Comparison:")
print("--------------------------------")

print(f"Diamond vs Copper: {diamond/copper:.2f} times")
print(f"Diamond vs Aluminium: {diamond/aluminium:.2f} times")
print(f"Diamond vs Stainless Steel: {diamond/steel:.2f} times")

# --------------------------------------------------
# 6. VISUALISE RESULTS
# --------------------------------------------------

names = list(heat_results.keys())
values = list(heat_results.values())

colors = ["purple", "orange", "skyblue", "grey"]

plt.figure(figsize=(10, 6))

bars = plt.bar(names, values, color=colors)

plt.xlabel("Material")
plt.ylabel("Heat Transfer Rate (W)")
plt.title("Thermal Conductivity Comparison Using Fourier's Law")

# Add numerical labels above bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 1500,
        f"{height:,.0f} W",
        ha="center"
    )

plt.ylim(0, max(values) * 1.15)
plt.grid(axis="y", linestyle="--", alpha=0.3)
plt.tight_layout()

# Save graph for GitHub
plt.savefig("conductivity_comparison.png", dpi=300)

# Display graph
plt.show()
