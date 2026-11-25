import os

LINE = "Grandma's kitchen smelled of fresh rice and rain, and for one whole summer I believed a hot dinner could fix anything."  # verified count: 118 chars

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
output_path = os.path.join(output_dir, 'entry.txt')

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(LINE)

print(len(LINE))
