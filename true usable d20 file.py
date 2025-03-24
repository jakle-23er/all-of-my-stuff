import matplotlib.pyplot as plt #to be able to referrence the program i am using to animate
from mpl_toolkits.mplot3d.art3d import Poly3DCollection #needed for 3d shapes
import numpy as np
from matplotlib.animation import FuncAnimation #allows for animation
import customtkinter #to make gui
#---------------------------------------------------------------------

# function to generate a random rotation
def random_rotation():
    # random face for rotation
    axis = np.random.randn(3)
    axis /= np.linalg.norm(axis)
    
    #random angle for rotation between 0 and 360 degrees
    angle = np.random.uniform(0, 2 * np.pi)
    
    #rotation of dice formula
    cos_angle = np.cos(angle)
    sin_angle = np.sin(angle)
    ux, uy, uz = axis
    
    rotation_function = np.array([
        [cos_angle + ux**2 * (1 - cos_angle), ux * uy * (1 - cos_angle) - uz * sin_angle, ux * uz * (1 - cos_angle) + uy * sin_angle],
        [uy * ux * (1 - cos_angle) + uz * sin_angle, cos_angle + uy**2 * (1 - cos_angle), uy * uz * (1 - cos_angle) - ux * sin_angle],
        [uz * ux * (1 - cos_angle) - uy * sin_angle, uz * uy * (1 - cos_angle) + ux * sin_angle, cos_angle + uz**2 * (1 - cos_angle)]
    ])
    
    return rotation_function

# function to plot and animate a 3D dice
def plot_rolling_dice():
    # best ratio for figure
    phi = (1 + np.sqrt(5)) / 2
    
    # sides of a regular 20 sided polygon (aka an icosohedron)
    vertices = np.array([
        [-1,  phi,  0],
        [ 1,  phi,  0],
        [-1, -phi,  0],
        [ 1, -phi,  0],
        [ 0, -1,  phi],
        [ 0,  1,  phi],
        [ 0, -1, -phi],
        [ 0,  1, -phi],
        [ phi,  0, -1],
        [ phi,  0,  1],
        [-phi,  0, -1],
        [-phi,  0,  1],
        [ 1,  0,  phi],
        [-1,  0,  phi],
        [ 1,  0, -phi],
        [-1,  0, -phi],
        [ phi,  1,  0],
        [ phi, -1,  0],
        [-phi,  1,  0],
        [-phi, -1,  0]
    ])
    
    # faces of the icosahedron
    faces = [
        [0, 11, 5], [0, 5, 1], [0, 1, 7], [0, 7, 10], [0, 10, 11],
        [1, 5, 9], [5, 11, 4], [11, 10, 2], [10, 7, 6], [7, 1, 8],
        [3, 9, 4], [3, 4, 2], [3, 2, 6], [3, 6, 8], [3, 8, 9],
        [4, 9, 5], [2, 4, 11], [6, 2, 10], [8, 6, 7], [9, 8, 1]
    ]
    
    # plotting the dice
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # create faces using poly3dCollection
    poly3d = Poly3DCollection([vertices[face] for face in faces], color='skyblue', edgecolors='black', linewidths=1, alpha=0.5)
    ax.add_collection3d(poly3d)
    
    # label each face with its corresponding number
    for i, face in enumerate(faces):
        # find the center of each triangle
        x_central = np.mean(vertices[face, 0])
        y_central = np.mean(vertices[face, 1])
        z_central = np.mean(vertices[face, 2])
        
        # place the label (number) at the central
        ax.text(x_central, y_central, z_central, str(i+1), color='black', fontsize=12, weight='bold')

    # set aspect ratio to be equal
    ax.set_box_aspect([1, 1, 1])  # Equal scaling for all axes
    
    # hide axes
    ax.set_axis_off()
    
    # randomize the number of frames for the animation
    frames = inputed_frames
    rotation_angle = np.pi / 18  # degree of rotation per framed (yes this is partially manditory, it wont function right without it)
    
    # function to update the plot for animation
    def update(frame):
        #nonlocal is a keyword that allows for a function to work with variables inside nested functions where the variable should not belong to the inner function (yes I stole the definition, also part of this code, however I cant remember who from)
        nonlocal vertices
        
        # generate a random rotation matrix
        rotation_function = random_rotation()
        
        # rotate the sides
        vertices = np.dot(vertices, rotation_function.T)
        
        # clear the previous plot
        ax.clear()
        
        # recreate the dice faces
        poly3d = Poly3DCollection([vertices[face] for face in faces], color='skyblue', edgecolors='black', linewidths=1, alpha=0.5)
        ax.add_collection3d(poly3d)
        
        # label the faces
        for i, face in enumerate(faces):
            x_centroid = np.mean(vertices[face, 0])
            y_centroid = np.mean(vertices[face, 1])
            z_centroid = np.mean(vertices[face, 2])
            ax.text(x_centroid, y_centroid, z_centroid, str(i+1), color='black', fontsize=12, weight='bold')
        
        ax.set_box_aspect([1, 1, 1])  # equal size for all sides
        ax.set_axis_off() 
    
    # create the animation
    ani = FuncAnimation(fig, update, frames=frames, interval=100, repeat=False)
    
    # Show the plot
    plt.show()

# call the function to animate the rolling icosahedron
#plot_rolling_icosahedron() :This was for testing purposes: 
#The reason i used icosahedron was because i could and thought it would be funny. it was until i had to start using it and now i dont want to go back and edit my code to change it

def process_action():
    global inputint
    global inputed_frames
    try:
        inputint=int(input.get()) #integer changer
        trycheck = True #for checking that the try command came out with no exception
        print("success")
        textbox.configure(state='normal')  # configure textbox to be read-write
        textbox.delete('0.0', 'end')  # delete all text
        textbox.insert('0.0', 'using your input for rolling') # insert at line 0 character 0 to replace the old text
        textbox.configure(state='disabled')  # configure textbox to be read-only
    except:
        textbox.configure(state='normal')  # configure textbox to be read-write
        textbox.delete('0.0', 'end')  # delete all text
        textbox.insert('0.0', 'impossible input: try again with an inputable whole integer number with no - . or /') # insert at line 0 character 0 place holder text
        textbox.configure(state='disabled')  # configure textbox to be read-only
        trycheck = False #for checking that the try command came out with no exception
        print("error")
    if trycheck == True: #for checking that the try command came out with no exception
        inputed_frames=inputint
        plot_rolling_dice()


# ********** END OF FUNCTION DEFINITIONS

# Sets up GUI global specs
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

#the root window that shows for the title and buttons
root = customtkinter.CTk() # root window object
root.title="roll the die"
root.geometry("600x500")

# Add a framed under a the root window
framed = customtkinter.CTkFrame( # creates a framed where the master of this element is root
    master=root,
    border_width=3
) 

# This calls the pack() geometry manager which places objects into blocks
# and then places them into the framed
framed.pack(padx=20, pady=60, fill="both", expand = True) 

#custom font setup
fontTitle = customtkinter.CTkFont(
    family = "Arial",
    size=44,
    weight="normal",
    underline=False
)

#title setup
lblTitle = customtkinter.CTkLabel(
    master=framed, 
    text="Roll The Die",
    padx=10,
    pady=12,
    font=fontTitle 
)
lblTitle.pack(padx=10,pady=12,fill="both",expand="True")

#entryfield
input = customtkinter.CTkEntry(
    master=framed,
    placeholder_text="input your time"
)
input.pack(padx=10,pady=12)

#allows the function to run
btnRUN=customtkinter.CTkButton(
    master=framed, #the parent for the button
    text="roll", # the text in the buttom
    command=process_action # The function to be executed when the button is clicked
)
btnRUN.pack(padx=10,pady=12)

#quit button
btnQuit=customtkinter.CTkButton(
    master=framed,
    text="Quit",
    command=root.destroy #closes program
    )
btnQuit.pack(padx=10,pady=10)



#general use textbox for all outputs that i need to tell the user
textbox = customtkinter.CTkTextbox(master=framed, width=250, height=150)

textbox.place(x=10, y=10)

textbox.insert('0.0', 'nothing here yet') # insert at line 0 character 0 place holder text

textbox.configure(state='disabled')  # configure textbox to be read-only

textbox.pack(padx=10,pady=11)


# ********* Program Starts Here *******************

# start the TKinter main loop
root.mainloop()
print(f"Program Ends...")