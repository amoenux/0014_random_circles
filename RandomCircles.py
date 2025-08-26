import cairo
from math import pi,tau,cos,sin
import random

def draw_random_circle_through_center(ctx:cairo.Context,AVERAGE_RADIUS=1):
    # Pick radius and center location at random
    radius=random.expovariate(1/AVERAGE_RADIUS)
    theta=random.random()*pi
    
    # Find the (x,y) coordinates of the center
    xaux=0.5+cos(theta)*radius
    yaux=sin(theta)*radius
    if random.random()<0.5:
        yaux*=-1
    yaux=0.5+yaux
    
    #Draw circle
    ctx.arc(xaux,yaux,radius,0,tau)
    ctx.stroke()


def draw_random_circle(ctx:cairo.Context,AVERAGE_RADIUS=1):
    # Pick radius and center location at random
    radius=random.expovariate(1/AVERAGE_RADIUS)
    theta=random.random()*pi
    
    # Find the (x,y) coordinates of the center
    # And add deviation from the center of the image
    xaux=random.random()+cos(theta)*radius
    yaux=sin(theta)*radius
    if random.random()<0.5:
        yaux*=-1
    yaux=random.random()+yaux
    
    # Draw circle
    ctx.arc(xaux,yaux,radius,0,tau)
    ctx.stroke()
        
        
def draw_circles(n,file_format='png',file_name="output",line_width=0.1):
    
    # Set up the image surface (width, height)
    if file_format == 'svg':
        # SVG surface for SVG output
        width, height = 256,256
        surface = cairo.SVGSurface(file_name+".svg", width, height)
    else:
        # PNG surface for PNG output (default)
        width, height = 2048,2048
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    
    ctx = cairo.Context(surface)
    
    # Fill background
    ctx.set_source_rgb(1,1,1)  # RGB for white
    ctx.rectangle(0, 0, width, height)  # Full canvas
    ctx.fill()
    
    # Prepare to draw circles
    ctx.scale(width,height)
    ctx.set_line_width(line_width)
    ctx.set_source_rgb(0,0,0)  # Set color for the circles (black)
    
    for i in range(n):
        draw_random_circle(ctx)

    # Save the output based on the chosen file format
    if file_format == 'svg':
        print(f"SVG saved as '{file_name}.svg'")
    else:
        surface.write_to_png(file_name+".png")
        print(f"PNG saved as '{file_name}.png'")


def random_drawings(n,min_lines=5,max_lines=100,line_width=0.0025,file_format='svg'):
    for i in range(n):
        draw_circles(random.randint(min_lines,max_lines),line_width=line_width,file_format=file_format,file_name=f"CircleDrawingBOW_{i:03}")


#random.seed(0)
#draw_circles(100, line_width=0.0025, file_format='svg',file_name="test1")
random_drawings(24)