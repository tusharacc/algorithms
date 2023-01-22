from turtle import *
import math
import seaborn as sns

class Draw:
    def __init__(self,graph):
        self.line_coordinates = []
        self.nodes = {}
        pal = sns.color_palette(n_colors=len(graph.nodes.keys())).as_hex()
        counter = 0
        for node in graph.nodes:
            self.nodes[node] = {'object': graph.nodes[node], 'x': 0, 'y': 0, 'edges':graph.G[node], 'color': pal[counter]}
            counter += 1
        self.user_input = textinput("Continue","Do you want to continue?")
    
    def __pen(self,ind):
        if ind == 'up':
            pu()
        elif ind == 'down':
            pd()

    def __write_at_pos(self,text):
        self.__pen('up')
        write(text,align='center',font=('Arial', 12, 'normal'))
        #self.__pen('up')

    def __set_position(self,x,y):
        self.__pen('up')
        setpos(x,y)

    def __draw_circle(self,radius,colorstring,node = None):
        self.__pen('down')
        color(colorstring)
        begin_fill()
        circle(radius=radius)
        end_fill()
        if node != None:
            x,y = position()

            self.__set_position(x+100,y)
            self.__write_at_pos(f"Node Name: {node.symbol}")
            self.__set_position(x+100,y-20)
            self.__write_at_pos(f"Next Node: {node.next}")
            self.__set_position(x+100,y-40)
            self.__write_at_pos(f"Node Capacity: {node.input_capacity}")
        

    def __turn_pointer(self,ind,radians):
        # if ind == 'right':
        #     rt(radians)
        # elif ind == 'left':
        rt(radians)

    def __draw_line(self,distance):
        pd()
        fd(distance)

    def __calculate_distance(self,from_pos,to_pos):
        x,y = from_pos
        x1,y1 = to_pos
        vertical = 0
        horizontal = 0
        if y1 < y:
            vertical = -50
        elif y > y1:
            vertical = 50
        
        return round(math.sqrt(math.pow(y1-y,2)+ math.pow(x1-x,2)) + vertical,2)

    def __draw_arrow(self,from_pos,to_pos):
        radians()
        #print (from_pos, to_pos)
        x,y = from_pos
        x1,y1 = to_pos
        denominator = x1 - x
        if denominator == 0.0:
            #print ("this is true")
            if y1 > y:
                slope_radians = math.radians(-90)
            else:
                #print ("I am in false")
                slope_radians = math.radians(90)
        else:
            if x1 < x:
                slope_radians = math.pi - math.atan(((y1-y)/(x1-x)))
            else:
                slope_radians = math.atan(((y1-y)/(x1-x))*-1)
        #print (math.degrees(slope_radians))
        self.__set_position(x,y)
        self.__turn_pointer('right',slope_radians)
        distance = self.__calculate_distance(from_pos,to_pos)
        self.__draw_line(distance)
        #fd(distance)
        curr_x,curr_y = position()
        self.__turn_pointer('right',math.radians(135))
        self.__draw_line(distance=20)
        #fd(distance=10)
        self.__set_position(curr_x,curr_y)
        self.__turn_pointer('right', math.radians(-270))      
        self.__draw_line(distance=20) 
        self.__turn_pointer('right', math.radians(135))   
        self.__turn_pointer('right',-1*slope_radians)
        self.__set_position(0,0)

    def __set_pencolor(self,hexstring):
        pencolor(hexstring)

    def __default_pencolor(self):
        pencolor('black')

    def __get_slope_of_line_radian(self,from_pos,to_pos):
        x,y = from_pos
        x1,y1 = to_pos

        if math.isclose(x,x1):
            return round(math.radians(90),2)
        else:
            return round(math.atan(abs(y1-y)/abs(x1-x)),2)


    def __get_line_coordinates(self,from_pos, to_pos):
        x,y = from_pos
        x1,y1 = to_pos
        #print ("Original coordinates",x,y,x1,y1)
        counter = 1.0
        increment = 10.0
        while True:
            found = False
            for line in self.line_coordinates:
                x_temp, y_temp, x1_temp, y1_temp = line
                
                slope_of_existing_line = self.__get_slope_of_line_radian(( x_temp, y_temp),(x1_temp, y1_temp))

                if slope_of_existing_line == float('inf'):
                    import sys
                    sys.exit(-2)
                slope_of_tentative_line = self.__get_slope_of_line_radian((x,y),(x1,y1))
                slope_of_existing_tentative = self.__get_slope_of_line_radian((x,y),(x_temp, y_temp))

                if slope_of_existing_line == slope_of_tentative_line and slope_of_tentative_line == slope_of_existing_tentative:
                    found = True
                    break
                # print ("Coordinates already drawn",x_temp, y_temp, x1_temp, y1_temp)
                # print ("Comparision",x_temp == x,y_temp==y,x1_temp==x1,y1_temp==y1)
                # print ("Is Close",math.isclose(x_temp,x),math.isclose(y_temp,y),math.isclose(x1_temp,x1),math.isclose(y1_temp,y1))
                # if math.isclose(x_temp,x) and math.isclose(y_temp,y) and math.isclose(x1_temp,x1) and  math.isclose(y1_temp,y1):
                #     found = True
                #     break
            if found:
                #print ("Corodinates-1",x,y,increment)
                x,y = x+increment,y+increment
                #print ("Corodinates-2",x1,y1,increment)
                x1,y1 = x1+increment,y1+increment
                counter += 1
                increment= increment*counter 
            else:
                break
        self.line_coordinates.append([x,y,x1,y1])
        return (x,y,x1,y1)
    
    def __write_edge_weights(self,edge_name,edge_weight,colorstring,position):
        x,y = position
        self.__set_position(x,y)
        self.__set_pencolor(colorstring)
        self.__write_at_pos(f"{edge_name:<10} : {edge_weight:<3}")
        x,y = position
        return (x,y-20)
    def draw(self):
        number_of_nodes = len(self.nodes.keys())
        width, height = window_height(), window_width()
        THETA = 360/number_of_nodes
        x,y = 300,0
        counter = 1
        for k,v in self.nodes.items():
            angle = counter*THETA
            x = round(300*math.sin(math.radians(angle)),2)
            y = round(300*math.cos(math.radians(angle)),2)
            self.__set_position(x,y)
            self.nodes[k]['x'] = x
            self.nodes[k]['y'] = y
            #print (k,x,y)
            self.__set_pencolor(v['color'])
            self.__draw_circle(25,v['color'],v['object'])
            self.__default_pencolor()
            self.__set_position(0,0)
            counter += 1

        start_text_pos = (-400,-100)
        for k,v in self.nodes.items():
            self.__set_pencolor(v['color'])
            for edge in v['edges']:
                x = v['x']
                y = v['y']
                x1,y1 = self.nodes[edge.destination]['x'],self.nodes[edge.destination]['y']
                x,y,x1,y1 = self.__get_line_coordinates((x,y),(x1,y1))
                self.__draw_arrow((x,y),(x1,y1))
                #Write Edge weights
                start_text_pos = self.__write_edge_weights(f"{edge.start:<4} --> {edge.destination:<4}", edge.weight,v['color'],start_text_pos)
            self.__default_pencolor()
        done()
