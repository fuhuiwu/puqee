svg_content = '''<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <!-- Large rounded rectangle -->
  <rect x="20" y="20" width="160" height="160" rx="15" ry="15" fill="#94bec6"/>
  
  <!-- Four small rounded rectangles -->
  <rect x="35" y="35" width="50" height="50" rx="8" ry="8" fill="#356c69"/>
  <rect x="115" y="35" width="50" height="50" rx="8" ry="8" fill="#356c69"/>
  <rect x="35" y="115" width="50" height="50" rx="8" ry="8" fill="#356c69"/>
  <rect x="115" y="115" width="50" height="50" rx="8" ry="8" fill="#356c69"/>
  
  <!-- Horizontal line -->
  <line x1="70" y1="100" x2="130" y2="100" stroke="#356c69" stroke-width="8"/>
  
  <!-- Diagonal curve -->
  <path d="M102 92 Q100 100 98 108" stroke="#94bec6" stroke-width="3" fill="none"/>
</svg>'''

with open('logo.svg', 'w') as f:
    f.write(svg_content)