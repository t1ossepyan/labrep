import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # Increased window size
    clock = pygame.time.Clock()
    
    # Drawing variables
    radius = 10
    mode = 'blue'
    shape_mode = 'line'  # Default to line drawing
    all_shapes = []  # Stores all shapes drawn
    current_shape = []  # Stores points for the current shape being drawn
    drawing = False  # Track if we're currently drawing
    start_pos = None  # Track where shape drawing started
    
    # Colors
    button_colors = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'eraser': (255, 255, 255)
    }
    
    # Button setup
    button_font = pygame.font.SysFont('Arial', 16)
    button_width, button_height = 80, 30
    button_margin = 5
    
    # Color buttons (first row)
    color_buttons = {
        'red': pygame.Rect(button_margin, button_margin, button_width, button_height),
        'green': pygame.Rect(button_margin + (button_width + button_margin), button_margin, button_width, button_height),
        'blue': pygame.Rect(button_margin + 2*(button_width + button_margin), button_margin, button_width, button_height),
        'eraser': pygame.Rect(button_margin + 3*(button_width + button_margin), button_margin, button_width, button_height)
    }
    
    # Shape buttons (second row)
    shape_buttons = {
        'line': pygame.Rect(button_margin, button_margin*2 + button_height, button_width, button_height),
        'rectangle': pygame.Rect(button_margin + (button_width + button_margin), button_margin*2 + button_height, button_width, button_height),
        'circle': pygame.Rect(button_margin + 2*(button_width + button_margin), button_margin*2 + button_height, button_width, button_height),
        'square': pygame.Rect(button_margin + 3*(button_width + button_margin), button_margin*2 + button_height, button_width, button_height),
        'right_triangle': pygame.Rect(button_margin + 4*(button_width + button_margin), button_margin*2 + button_height, button_width, button_height)
    }
    
    # More shape buttons (third row)
    shape_buttons.update({
        'equilateral_triangle': pygame.Rect(button_margin, button_margin*3 + button_height*2, button_width, button_height),
        'rhombus': pygame.Rect(button_margin + (button_width + button_margin), button_margin*3 + button_height*2, button_width, button_height),
        'clear': pygame.Rect(button_margin + 2*(button_width + button_margin), button_margin*3 + button_height*2, button_width, button_height)
    })
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check color buttons
                for color, btn in color_buttons.items():
                    if btn.collidepoint(event.pos):
                        mode = color
                
                # Check shape buttons
                for shape, btn in shape_buttons.items():
                    if btn.collidepoint(event.pos):
                        if shape == 'clear':
                            all_shapes = []
                        else:
                            shape_mode = shape
                
                # Start drawing if not clicking a button
                if not any(btn.collidepoint(event.pos) for btn in list(color_buttons.values()) + list(shape_buttons.values())):
                    if event.button == 1:  # left click
                        drawing = True
                        start_pos = event.pos
                        if shape_mode == 'line':
                            current_shape = []
                            radius = min(200, radius + 1)
                        elif shape_mode == 'eraser':
                            current_shape = []
                
                if event.button == 3:  # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    drawing = False
                    end_pos = event.pos
                    
                    if shape_mode == 'line' and current_shape:
                        all_shapes.append(('line', current_shape.copy(), radius, mode))
                    elif shape_mode != 'line' and start_pos:
                        # Add the completed shape
                        all_shapes.append((shape_mode, start_pos, end_pos, radius, mode))
                    
                    current_shape = []
                    start_pos = None
            
            if event.type == pygame.MOUSEMOTION and drawing:
                if shape_mode == 'line':
                    current_shape.append(event.pos)
                    current_shape = current_shape[-256:]  # limit points
                elif shape_mode == 'eraser':
                    # For eraser, we'll draw white circles along the path
                    current_shape.append(event.pos)
                    all_shapes.append(('circle', event.pos, event.pos, radius, 'eraser'))
                
        screen.fill((255, 255, 255))
        
        # Draw all shapes
        for shape in all_shapes:
            if shape[0] == 'line':
                _, points, width, color = shape
                if len(points) >= 2:
                    for i in range(len(points)-1):
                        drawLineBetween(screen, i, points[i], points[i+1], width, color)
            elif shape[0] == 'rectangle':
                _, start, end, width, color = shape
                drawRectangle(screen, start, end, width, color)
            elif shape[0] == 'circle':
                _, start, end, width, color = shape
                radius = int(math.sqrt((end[0]-start[0])**2 + (end[1]-start[1])**2))
                drawCircle(screen, start, radius, width, color)
            elif shape[0] == 'square':
                _, start, end, width, color = shape
                drawSquare(screen, start, end, width, color)
            elif shape[0] == 'right_triangle':
                _, start, end, width, color = shape
                drawRightTriangle(screen, start, end, width, color)
            elif shape[0] == 'equilateral_triangle':
                _, start, end, width, color = shape
                drawEquilateralTriangle(screen, start, end, width, color)
            elif shape[0] == 'rhombus':
                _, start, end, width, color = shape
                drawRhombus(screen, start, end, width, color)
        
        # Draw current line in progress
        if shape_mode == 'line' and len(current_shape) >= 2:
            for i in range(len(current_shape)-1):
                drawLineBetween(screen, i, current_shape[i], current_shape[i+1], radius, mode)
        
        # Draw preview of current shape being drawn
        if drawing and start_pos and shape_mode != 'line' and shape_mode != 'eraser':
            end_pos = pygame.mouse.get_pos()
            if shape_mode == 'rectangle':
                drawRectangle(screen, start_pos, end_pos, radius, mode, True)
            elif shape_mode == 'circle':
                drawCircle(screen, start_pos, 
                          int(math.sqrt((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2)), 
                          radius, mode, True)
            elif shape_mode == 'square':
                drawSquare(screen, start_pos, end_pos, radius, mode, True)
            elif shape_mode == 'right_triangle':
                drawRightTriangle(screen, start_pos, end_pos, radius, mode, True)
            elif shape_mode == 'equilateral_triangle':
                drawEquilateralTriangle(screen, start_pos, end_pos, radius, mode, True)
            elif shape_mode == 'rhombus':
                drawRhombus(screen, start_pos, end_pos, radius, mode, True)
        
        # Draw buttons
        # Color buttons
        for color, btn in color_buttons.items():
            btn_color = button_colors[color]
            if mode == color:
                btn_color = (min(255, btn_color[0]+50), min(255, btn_color[1]+50), min(255, btn_color[2]+50))
            pygame.draw.rect(screen, btn_color, btn)
            text = button_font.render(color.capitalize(), True, (0, 0, 0))
            screen.blit(text, (btn.x + 5, btn.y + 5))
        
        # Shape buttons
        for shape, btn in shape_buttons.items():
            btn_color = (200, 200, 200) if shape != 'clear' else (220, 150, 150)
            if shape_mode == shape:
                btn_color = min(255, btn_color[0]+50), min(255, btn_color[1]+50), min(255, btn_color[2]+50)
            pygame.draw.rect(screen, btn_color, btn)
            
            # Format shape names for display
            display_name = shape.replace('_', ' ').title()
            if shape == 'right_triangle':
                display_name = "R.Triangle"
            elif shape == 'equilateral_triangle':
                display_name = "Eq.Triangle"
            
            text = button_font.render(display_name if shape != 'clear' else "Clear", True, (0, 0, 0))
            screen.blit(text, (btn.x + 5, btn.y + 5))

        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    color = getColor(color_mode)
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    iterations = int(iterations)
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def drawRectangle(screen, start, end, width, color_mode, preview=False):
    color = getColor(color_mode)
    rect = pygame.Rect(min(start[0], end[0]), min(start[1], end[1]), 
                      abs(end[0] - start[0]), abs(end[1] - start[1]))
    
    if preview:
        pygame.draw.rect(screen, color, rect, width)
    else:
        # For final rectangle, we'll draw it with circles for consistent line width
        points = [
            (rect.left, rect.top),
            (rect.right, rect.top),
            (rect.right, rect.bottom),
            (rect.left, rect.bottom)
        ]
        
        for i in range(4):
            p1 = points[i]
            p2 = points[(i+1)%4]
            drawLineBetween(screen, i, p1, p2, width, color_mode)

def drawCircle(screen, center, radius, width, color_mode, preview=False):
    color = getColor(color_mode)
    if preview:
        pygame.draw.circle(screen, color, center, radius, width)
    else:
        # For better looking circles with consistent width, we'll draw multiple points
        for angle in range(0, 360, 5):
            rad = math.radians(angle)
            x = int(center[0] + radius * math.cos(rad))
            y = int(center[1] + radius * math.sin(rad))
            pygame.draw.circle(screen, color, (x, y), width)

def drawSquare(screen, start, end, width, color_mode, preview=False):
    color = getColor(color_mode)
    size = max(abs(end[0] - start[0]), abs(end[1] - start[1]))
    rect = pygame.Rect(start[0], start[1], size, size)
    
    if end[0] < start[0]:
        rect.x = start[0] - size
    if end[1] < start[1]:
        rect.y = start[1] - size
    
    if preview:
        pygame.draw.rect(screen, color, rect, width)
    else:
        points = [
            (rect.left, rect.top),
            (rect.right, rect.top),
            (rect.right, rect.bottom),
            (rect.left, rect.bottom)
        ]
        
        for i in range(4):
            p1 = points[i]
            p2 = points[(i+1)%4]
            drawLineBetween(screen, i, p1, p2, width, color_mode)

def drawRightTriangle(screen, start, end, width, color_mode, preview=False):
    color = getColor(color_mode)
    points = [
        start,
        (start[0], end[1]),
        end
    ]
    
    if preview:
        pygame.draw.polygon(screen, color, points, width)
    else:
        for i in range(3):
            p1 = points[i]
            p2 = points[(i+1)%3]
            drawLineBetween(screen, i, p1, p2, width, color_mode)

def drawEquilateralTriangle(screen, start, end, width, color_mode, preview=False):
    color = getColor(color_mode)
    side_length = math.sqrt((end[0]-start[0])**2 + (end[1]-start[1])**2)
    height = side_length * math.sqrt(3)/2
    
    # Calculate the third point to make an equilateral triangle
    angle = math.atan2(end[1]-start[1], end[0]-start[0])
    p3 = (
        start[0] + side_length * math.cos(angle + math.pi/3),
        start[1] + side_length * math.sin(angle + math.pi/3)
    )
    
    points = [start, end, p3]
    
    if preview:
        pygame.draw.polygon(screen, color, points, width)
    else:
        for i in range(3):
            p1 = points[i]
            p2 = points[(i+1)%3]
            drawLineBetween(screen, i, p1, p2, width, color_mode)

def drawRhombus(screen, start, end, width, color_mode, preview=False):
    color = getColor(color_mode)
    center = ((start[0] + end[0])/2, (start[1] + end[1])/2)
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    
    # The other two points are perpendicular to the main diagonal
    p1 = (center[0] - dy/2, center[1] + dx/2)
    p2 = (center[0] + dy/2, center[1] - dx/2)
    
    points = [start, p1, end, p2]
    
    if preview:
        pygame.draw.polygon(screen, color, points, width)
    else:
        for i in range(4):
            p1 = points[i]
            p2 = points[(i+1)%4]
            drawLineBetween(screen, i, p1, p2, width, color_mode)

def getColor(color_mode):
    if color_mode == 'blue':
        return (0, 0, 255)
    elif color_mode == 'red':
        return (255, 0, 0)
    elif color_mode == 'green':
        return (0, 255, 0)
    elif color_mode == 'eraser':
        return (255, 255, 255)
    return (0, 0, 0)

main()