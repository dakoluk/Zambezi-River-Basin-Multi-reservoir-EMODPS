import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch
import matplotlib.patches as mpatches

# Create figure with optimal spacing
fig, ax = plt.subplots(figsize=(22, 13))

# Title
#plt.title('Waves of Justice: The Evolution of Distributive Justice in Climate IAMs', 
#          fontsize=22, weight='bold', pad=30)

# Set up axes
ax.set_xlim(1988, 2029)
ax.set_ylim(-2.2, 9.5)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_yticks([])

# Create timeline arrow
arrow = FancyArrowPatch((1990, 0), (2027, 0),
                       arrowstyle='->', mutation_scale=40, linewidth=4.5, 
                       color='black', zorder=10)
ax.add_patch(arrow)

# Define wave parameters - well-separated vertically
waves_data = [
    {
        'name': 'WAVE 1: Discounted Utilitarian',
        'color': '#1B5E20',
        'start': 1990,
        'peak': 1997,
        'end': 2005,
        'base_height': 7.0,
        'amplitude': 1.3,
        'events': [
            (1994, 'DICE\nNordhaus', 0.6),
            (1996, 'RICE\nNordhaus', 0.9),
            (1998, 'Schmidt\nCGE', 0.7)
        ]
    },
    {
        'name': 'WAVE 2: Alternative Welfare & Intergenerational',
        'color': '#0D47A1',
        'start': 2003,
        'peak': 2011,
        'end': 2018,
        'base_height': 5.5,
        'amplitude': 1.3,
        'events': [
            (2008, 'DICE-2007\nNordhaus', 0.8),
            (2009, 'Adler\nDiscount rates', 0.65),
            (2017, 'Botzen et al.\nChichilnisky', 0.9)
        ]
    },
    {
        'name': 'WAVE 3: Prioritarian & Non-Utilitarian',
        'color': '#4A148C',
        'start': 2013,
        'peak': 2018,
        'end': 2023,
        'base_height': 4.0,
        'amplitude': 1.3,
        'events': [
            (2015, 'Dennig et al.\nNICE model', 0.75),
            (2017, 'Adler et al.\nPrioritarianism', 0.95),
            (2019, 'Mejean\nCatastrophic risk', 0.7)
        ]
    },
    {
        'name': 'WAVE 4: Disaggregation & Heterogeneity',
        'color': '#E65100',
        'start': 2017,
        'peak': 2021,
        'end': 2026,
        'base_height': 2.5,
        'amplitude': 1.3,
        'events': [
            (2017, 'Rao et al.\nSubnational', 0.7),
            (2021, 'Budolfson et al.\nRedistribution', 1.0),
            (2022, 'Safarzynska\nABM-IAM', 0.8)
        ]
    },
    {
        'name': 'WAVE 5: Methodological Synthesis',
        'color': '#B71C1C',
        'start': 2020,
        'peak': 2024,
        'end': 2028,
        'base_height': 1.0,
        'amplitude': 1.3,
        'events': [
            (2021, 'Jafino et al.\nJustice framework', 0.75),
            (2021, 'Dooley et al.\nFair-share', 0.6),
            (2022, 'Żebrowski et al.\nMulti-objective', 1.05),
            (2023, 'Schulan et al.\nEthical mapping', 0.85)
        ]
    }
]

# Draw each wave
for wave in waves_data:
    # Generate smooth wave curve
    x_wave = np.linspace(wave['start'], wave['end'], 300)
    
    # Create smooth sine curve
    progress = (x_wave - wave['start']) / (wave['end'] - wave['start'])
    y_wave = wave['base_height'] + wave['amplitude'] * np.sin(progress * np.pi)
    
    # Plot the wave
    ax.plot(x_wave, y_wave, color=wave['color'], linewidth=4.5, alpha=0.9, zorder=5)
    
    # Add wave label at the peak
    peak_x = wave['peak']
    peak_y = wave['base_height'] + wave['amplitude']
    ax.text(peak_x, peak_y + 0.35, wave['name'], 
            fontsize=12, ha='center', va='bottom', weight='bold', color=wave['color'],
            bbox=dict(boxstyle='round,pad=0.6', facecolor='white', 
                     edgecolor=wave['color'], linewidth=2.5, alpha=0.98))
    
    # Add events/models on the wave
    for event_year, event_label, height_offset in wave['events']:
        if wave['start'] <= event_year <= wave['end']:
            progress = (event_year - wave['start']) / (wave['end'] - wave['start'])
            event_y = wave['base_height'] + wave['amplitude'] * np.sin(progress * np.pi)
            
            # Vertical dashed line
            ax.plot([event_year, event_year], [0, event_y], 
                    linestyle='--', color=wave['color'], linewidth=2.5, alpha=0.35, zorder=3)
            
            # Event marker
            ax.plot(event_year, event_y, 'o', color=wave['color'], 
                    markersize=12, zorder=6, markeredgecolor='white', markeredgewidth=3)
            
            # Event label
            label_y = event_y + 0.15 + height_offset
            ax.text(event_year, label_y, event_label, 
                    fontsize=9.5, ha='center', va='bottom', color=wave['color'], 
                    weight='bold', bbox=dict(boxstyle='round,pad=0.45', 
                    facecolor='white', edgecolor=wave['color'], alpha=0.95, linewidth=2))

# Add timeline milestones
milestones = [
    (1992, 'UNFCCC\nRio'),
    (1997, 'Kyoto\nProtocol'),
    (2009, 'Copenhagen'),
    (2015, 'Paris\nAgreement'),
    (2021, 'Glasgow\nCOP26'),
    (2023, 'Dubai\nCOP28')
]

for year, label in milestones:
    ax.plot([year, year], [0, -0.3], color='#424242', linewidth=3, zorder=4)
    ax.text(year, -0.5, str(year), fontsize=11, ha='center', weight='bold')
    ax.text(year, -0.75, label, fontsize=10, ha='center', va='top', style='italic', color='#424242')

# Add decade markers
for year in range(1990, 2030, 5):
    if year not in [m[0] for m in milestones]:
        ax.plot([year, year], [0, -0.18], color='#757575', linewidth=2.5, zorder=4)
        ax.text(year, -0.4, str(year), fontsize=10, ha='center', color='#757575')

# Add legend box - positioned to avoid overlap
legend_x = 2020
legend_y = 8.5
legend_box = mpatches.FancyBboxPatch((legend_x, legend_y - 3.0), 8.0, 2.8,
                                     boxstyle="round,pad=0.25",
                                     edgecolor='#2C3E50', facecolor='white',
                                     linewidth=3, alpha=0.98, zorder=20)
ax.add_patch(legend_box)

ax.text(legend_x + 4.0, legend_y - 0.3, 'Key Justice Principles in IAMs', 
        fontsize=13, weight='bold', ha='center', color='#2C3E50')

justice_principles = [
    ('Utilitarianism', '#1B5E20', 'Maximize aggregate welfare'),
    ('Egalitarianism', '#0D47A1', 'Equal distribution of resources'),
    ('Prioritarianism', '#4A148C', 'Priority to worse-off individuals'),
    ('Sufficientarianism', '#E65100', 'Meeting minimum thresholds'),
    ('Limitarianism', '#B71C1C', 'Capping maximum resources')
]

for i, (principle, color, description) in enumerate(justice_principles):
    y_pos = legend_y - 0.8 - i*0.45
    ax.plot([legend_x + 0.4, legend_x + 1.3], [y_pos, y_pos], 
            color=color, linewidth=6, alpha=0.9)
    ax.text(legend_x + 1.6, y_pos, principle, 
            fontsize=10.5, va='center', ha='left', color=color, weight='bold')
    ax.text(legend_x + 4.2, y_pos, f'– {description}', 
            fontsize=9.5, va='center', ha='left', color='#424242', style='italic')

# Methodological evolution at bottom
evolution_y = -1.35
ax.text(1990, evolution_y + 0.1, 'Methodological Evolution:', 
        fontsize=12, ha='left', weight='bold', color='#2C3E50')

evolution_markers = [
    (1995, 'Global\naggregation', '#1B5E20'),
    (2004, 'Regional\ndisaggregation', '#0D47A1'),
    (2015, 'Within-region\ninequality', '#4A148C'),
    (2020, 'Agent-based\nmodeling', '#E65100'),
    (2024, 'Multi-objective\noptimization', '#B71C1C')
]

for year, label, color in evolution_markers:
    ax.text(year, evolution_y - 0.15, label, fontsize=10, ha='center', va='top', 
            color=color, weight='bold',
            bbox=dict(boxstyle='round,pad=0.5', 
            facecolor='white', edgecolor=color, alpha=0.95, linewidth=2.5))

# Footer
ax.text(1990, -2.0, 'Evolution from utilitarian optimization to comprehensive multi-dimensional justice assessment', 
        fontsize=13, style='italic', color='#666666', weight='bold')

plt.tight_layout()
plt.savefig('/Users/damlaakoluk/Zambezi-River-Basin-Multi-reservoir-EMODPS/ZambeziSmashPython/src/waves_final_clean.png', dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')

print("Final clean wave visualization created!")
print("Files saved:")
fig.show()
