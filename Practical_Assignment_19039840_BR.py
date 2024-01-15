import csv
import random
import math
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

border_margin =  2
border_strength = 10
border_size = 100

class Boid():

    def __init__(self, id, x, y, sim):
        self.sim = sim
        self.id = id
        self.x = x
        self.y = y
        flt = round(random.random(), 1)
        self.xv = random.choice(range(-(1), (1))) + flt
        flt = round(random.random(), 1)
        self.yv = random.choice(range(-(1), (1))) + flt
        self.alignment = [0,0]
        self.inner_boids = list()
        self.outer_boids = list()

    def reset_neighbors(self):
        self.inner_boids.clear()
        self.outer_boids.clear()

    def find_neighbors(self, list_of_boids, inner_radius, outer_radius):
        self.inner_boids.clear()
        self.outer_boids.clear()
        for i in list_of_boids:
            if i != self:
                distance = math.sqrt((self.x - i.x)**2 + (self.y - i.y)**2)

                if 0 < distance <= inner_radius:
                    self.inner_boids.append(i)
                elif inner_radius < distance <= outer_radius:
                    self.outer_boids.append(i)
    def calculate_next_separation_vector(self):
        x = 0
        y = 0
        for i in self.inner_boids:
            differenceY = (self.y - i.y)
            y += differenceY
            differenceX = (self.x - i.x)
            x += differenceX

        if len(self.inner_boids) > 0:
            x /= len(self.inner_boids)
            y /= len(self.inner_boids)
        else: return (0,0)

        return ((x * self.sim.separation_strength)+(self.sim.randomness_strength * random.uniform(-1, 1)), ((y * self.sim.separation_strength)+(self.sim.randomness_strength * random.uniform(-1, 1))))

    def calculate_next_cohesion_vector(self):
        x = 0
        y = 0
        for i in self.outer_boids:
            differenceY = (i.y - self.y)
            y += differenceY
            differenceX = (i.x - self.x)
            x += differenceX

        if len(self.outer_boids) > 0:
            pass
            x /= len(self.outer_boids)
            y /= len(self.outer_boids)
        else: return(0,0)
        return (((x * self.sim.cohesion_strength)+(self.sim.randomness_strength * random.uniform(-1, 1))), ((y * self.sim.cohesion_strength)+(self.sim.randomness_strength * random.uniform(-1, 1))))

    def calculate_next_alignment_vector(self):
        x = 0
        y = 0

        for i in self.inner_boids:
            x += i.xv
            y += i.yv

        if len(self.inner_boids) > 0:
            x /= len(self.inner_boids)
            y /= len(self.inner_boids)

        return ((x * self.sim.alignment_strength), (y * self.sim.alignment_strength))

#########################################################################################################
#########################################################################################################
#########################################################################################################    

class SimulationGUI:
    def __init__(self, master):
        self.master = master
        master.title("Boids Simulation")

        self.label = tk.Label(master, text="Select an option:")
        self.label.pack()

        self.button_frame = tk.Frame(master)
        self.button_frame.pack()

        options = [
            "Run Default Simulation",
            "Plot the start and end positions of 10 boids",
            "Plot the start and end positions of 100 boids",
            "Run a simulation with 10 boids",
            "Run a simulation with 100 boids",
            "Run simulation with 10 boids and save data",
            "Run simulation with 100 boids and save to data",
            "Run simulation using only separation and cohesion",
            "Run simulation using only separation and alignment",
            "Run simulation using only cohesion and alignment",
            "Run simulation with Wind",
            "Run simulation with Reduced vision"
        ]

        self.buttons = []

        for i, option in enumerate(options, start=1):
            button = tk.Button(self.button_frame, text=f"{i}. {option}", command=lambda i=i: self.run_option(i))
            button.pack(side=tk.TOP)
            self.buttons.append(button)

    def run_option(self, choice):
        try:
            if 1 <= choice <= 12:
                if choice == 1:
                    sim = Simulation()
                    sim.assign_Parameters(inrad = 5, outrad = 20, boidcount = 50, frames = 200, maxvel = 2, randstr = 0,cohstr = 0.03 ,sepstr = 0.25, alistr = 0.13)
                    sim.create_boids()
    
                    for frame in range(sim.frames):
                        sim.update()
                        sim.plot_boids_simulation()
        
                elif choice == 2:
                    sim = Simulation()
                    sim.assign_Parameters(inrad = 5, outrad = 20, boidcount = 10, frames = 200, maxvel = 2, randstr = 0,cohstr = 0.03 ,sepstr = 0.25, alistr = 0.13)
                    sim.create_boids()
                    for frame in range(sim.frames):
                        sim.update()
                        sim.plot_boids_start_end(sim.frames,frame)
                elif choice == 3:
                    sim = Simulation()
                    sim.assign_Parameters(inrad = 5, outrad = 20, boidcount = 100, frames = 200, maxvel = 2, randstr = 0,cohstr = 0.03 ,sepstr = 0.25, alistr = 0.13)
                    sim.create_boids()
                    for frame in range(sim.frames):
                        sim.update()
                        sim.plot_boids_start_end(sim.frames,frame)
                elif choice == 4:
                    sim = Simulation()
                    sim.assign_Parameters(inrad = 5, outrad = 20, boidcount = 10, frames = 200, maxvel = 2, randstr = 0,cohstr = 0.03 ,sepstr = 0.25, alistr = 0.13)
                    sim.create_boids()
                    for frame in range(sim.frames):
                        sim.update()
                        sim.plot_boids_simulation()
        
                elif choice == 5:
                    sim = Simulation()
                    sim.assign_Parameters(inrad = 5, outrad = 20, boidcount = 100, frames = 200, maxvel = 2, randstr = 0,cohstr = 0.03 ,sepstr = 0.25, alistr = 0.13)
                    sim.create_boids()
                    for frame in range(sim.frames):
                        sim.update()
                        sim.plot_boids_simulation()
        
                elif choice == 6:
                    sim = Simulation()
                    sim.assign_Parameters(inrad = 5, outrad = 20, boidcount = 10, frames = 200, maxvel = 2, randstr = 0,cohstr = 0.03 ,sepstr = 0.25, alistr = 0.13)
                    sim.create_boids()
                    for frame in range(sim.frames):
                        sim.update()
                        sim.plot_boids_simulation()
                        sim.save_data(frame, '10_boid_simulation.csv')
        
                    messagebox.showinfo("Info", "Data has been saved to 10_boid_simulation.csv")
                elif choice == 7:
                    sim = Simulation()
                    sim.assign_Parameters(inrad = 5, outrad = 20, boidcount = 100, frames = 200, maxvel = 2, randstr = 0,cohstr = 0.03 ,sepstr = 0.25, alistr = 0.13)
                    sim.create_boids()
                    for frame in range(sim.frames):
                        sim.update()
                        sim.plot_boids_simulation()
                        sim.save_data(frame, '100_boid_simulation.csv')
        
                    messagebox.showinfo("Info", "Data has been saved to 100_boid_simulation.csv")
                elif choice == 8: # Cohesion + Seperation Model
                    sim = Simulation()
                    sim.assign_Parameters(inrad = 5, outrad = 20, boidcount = 100, frames = 200, maxvel = 2, randstr = 0,cohstr = 0.03 ,sepstr = 0.25, alistr = 0)
                    sim.create_boids()
                    for frame in range(sim.frames):
                        sim.update()
                        sim.plot_boids_simulation()
                        sim.save_data(frame, 'Coh_Sep_Model_Breaking.csv')
        
                elif choice == 9:   # Alignment + Seperation Model
                    sim = Simulation()
                    sim.assign_Parameters(inrad = 5, outrad = 20, boidcount = 100, frames = 200, maxvel = 2, randstr = 0,cohstr = 0.00 ,sepstr = 0.25, alistr = 0.13)
                    sim.create_boids()
                    for frame in range(sim.frames):
                        sim.update()
                        sim.plot_boids_simulation()
                        sim.save_data(frame, 'Ali_Sep_Model_Breaking.csv')
        
                elif choice == 10:  # Cohesion + Alignment Model
                    sim = Simulation()
                    sim.assign_Parameters(inrad = 5, outrad = 20, boidcount = 100, frames = 200, maxvel = 2, randstr = 0,cohstr = 0.03 ,sepstr = 0, alistr = 0.13)
                    sim.create_boids()
                    for frame in range(sim.frames):
                        sim.update()
                        sim.plot_boids_simulation()
                        sim.save_data(frame, 'Coh_Ali_Model_Breaking.csv')
        
                elif choice == 11:
                    sim = Simulation()
                    sim.assign_Parameters(inrad = 5, outrad = 20, boidcount = 100, frames = 200, maxvel = 2, randstr = 0,cohstr = 0.03 ,sepstr = 0.25, alistr = 0.13)
                    sim.create_boids()
                    for frame in range(sim.frames):
                        sim.update_with_wind(0.75)
                        sim.plot_boids_simulation()
                        sim.save_data(frame, 'With_Wind_Modifier.csv')
        

                elif choice == 12:
                    sim = Simulation()
                    sim.assign_Parameters(inrad = 3, outrad = 9, boidcount = 100, frames = 200, maxvel = 2, randstr = 0,cohstr = 0.03 ,sepstr = 0.25, alistr = 0.13)
                    sim.create_boids()
                    for frame in range(sim.frames):
                        sim.update()
                        sim.plot_boids_simulation()
                        sim.save_data(frame, 'Reduced_Vision_Modifier.csv')
        
            else:
                messagebox.showerror("Error", "Invalid choice")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def view_example():
        sim = Simulation()
        sim.assign_Parameters(inrad = 5, outrad = 20, boidcount = 50, frames = 2000, maxvel = 2, randstr = 0,cohstr = 0.03 ,sepstr = 0.25, alistr = 0.13)
        sim.create_boids()
    
        for frame in range(sim.frames):
            sim.update()
            sim.plot_boids_simulation()

#########################################################################################################
#########################################################################################################
#########################################################################################################

class Simulation:

    def __init__(self):
        self.inner_radius = 0 # 5
        self.outer_radius = 0 # 20
        self.amount_of_boids = 0 # 50
        self.frames = 0 # 2000
        self.max_velocity = 0 # 2
        self.randomness_strength = 0 # 0
        self.cohesion_strength = 0 # 0.03
        self.separation_strength = 0  # 0.25
        self.alignment_strength = 0 #0.12
        self.list_of_boids = list()

    def assign_Parameters(self, inrad, outrad, boidcount, frames, maxvel, randstr,cohstr,sepstr, alistr):
    
        self.inner_radius = inrad # 5
        self.outer_radius = outrad # 20
        self.amount_of_boids = boidcount # 50
        self.frames = frames # 2000
        self.max_velocity = maxvel # 2
        self.randomness_strength = randstr # 0
        self.cohesion_strength = cohstr # 0.03
        self.separation_strength = sepstr  # 0.25
        self.alignment_strength = alistr #0.12
    
    def create_boids(self):
        for i in range(1, self.amount_of_boids+1):
            flt = round(random.random(), 1)
            posx = random.choice(range(-(border_size), (border_size))) + flt
            flt = round(random.random(), 1)
            posy = random.choice(range(-(border_size), (border_size))) + flt
            self.list_of_boids.append(Boid(i, posx, posy, self))

    def get_boid_info(self):
        for i in self.list_of_boids:
            print(f"\nBoid: {i.id} \nx position: {i.x} \ny position: {i.y} \nboids in inner radius: {len(i.inner_boids)} \nboids in outer radius: {len(i.outer_boids)}")
            print(f"\nBoid x-Velocity: {i.xv} \n y-Velocity: {i.yv}")
            print(f"Separation Vector: {i.calculate_next_separation_vector()}")
            print(f"Cohesion Vector: {i.calculate_next_cohesion_vector()}")
            print(f"Alignment Vector: {i.calculate_next_alignment_vector()}\n")

    def plot_boids_start_end(self, frames, frame):
        boids = self.list_of_boids
        x_positions = [boid.x for boid in boids]
        y_positions = [boid.y for boid in boids]
        if frame == 1:
            plt.scatter(x_positions, y_positions, color="green", marker='o')
        if frame == frames -1:
            plt.scatter(x_positions, y_positions, color="red", marker='o')
        plt.xlim(-(border_size+5), (border_size+5))
        plt.ylim(-(border_size+5), (border_size+5))
        plt.title("Start/End")
        plt.pause(0.05)


    def save_data(self, frame, filename): 
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['frame', 'Boid', 'x', 'y', 'xy', 'yv'])
            for boidnumber, boid in enumerate(self.list_of_boids):
                writer.writerow([frame + 1, boidnumber + 1, boid.x, boid.y,
                                boid.xv, boid.yv])
                writer.writerow([])


    def plot_boids_simulation(self):
        plt.clf()
        boids = self.list_of_boids
        x_positions = [boid.x for boid in boids]
        y_positions = [boid.y for boid in boids]
        plt.scatter(x_positions, y_positions, color="green", marker='o')
        plt.xlim(-(border_size+5), (border_size+5))
        plt.ylim(-(border_size+5), (border_size+5))
        plt.title("Boids Simulation")
        plt.pause(0.05)

    def update_with_wind(self, windstr):
        for boid in self.list_of_boids:
            boid.reset_neighbors()
            boid.find_neighbors(self.list_of_boids, self.inner_radius, self.outer_radius)
            separation_vector = boid.calculate_next_separation_vector()
            cohesion_vector = boid.calculate_next_cohesion_vector()
            alignment_vector = boid.calculate_next_alignment_vector()

            boid.alignment = (alignment_vector[0], alignment_vector[1])
            #boid.resetVel()
            boid.xv += (cohesion_vector[0] + separation_vector[0] + alignment_vector[0])
            boid.yv += (cohesion_vector[1] + separation_vector[1] + alignment_vector[1])

            magnitude = math.sqrt(boid.xv**2 + boid.yv**2)
            if magnitude > self.max_velocity:
                scaling_factor = self.max_velocity / magnitude
                boid.xv *= scaling_factor
                boid.yv *= scaling_factor

            boid.x += boid.xv+windstr
            boid.y += boid.yv+windstr

            border_margin = 2.0
            if boid.x < -border_size + border_margin or boid.x > border_size - border_margin:
                boid.xv *= -border_strength
            if boid.y < -border_size + border_margin or boid.y > border_size - border_margin:
                boid.yv *= -border_strength




    def update(self):
        for boid in self.list_of_boids:
            boid.reset_neighbors()
            boid.find_neighbors(self.list_of_boids, self.inner_radius, self.outer_radius)
            separation_vector = boid.calculate_next_separation_vector()
            cohesion_vector = boid.calculate_next_cohesion_vector()
            alignment_vector = boid.calculate_next_alignment_vector()

            boid.alignment = (alignment_vector[0], alignment_vector[1])
            #boid.resetVel()
            boid.xv += (cohesion_vector[0] + separation_vector[0] + alignment_vector[0])
            boid.yv += (cohesion_vector[1] + separation_vector[1] + alignment_vector[1])

            magnitude = math.sqrt(boid.xv**2 + boid.yv**2)
            if magnitude > self.max_velocity:
                scaling_factor = self.max_velocity / magnitude
                boid.xv *= scaling_factor
                boid.yv *= scaling_factor

            boid.x += boid.xv
            boid.y += boid.yv

            border_margin = 2.0
            if boid.x < -border_size + border_margin or boid.x > border_size - border_margin:
                boid.xv *= -border_strength
            if boid.y < -border_size + border_margin or boid.y > border_size - border_margin:
                boid.yv *= -border_strength


def runTest():
    sim = Simulation()
    sim.assign_Parameters(inrad = 5, outrad = 20, boidcount = 50, frames = 2000, maxvel = 2, randstr = 0,cohstr = 0.03 ,sepstr = 0.25, alistr = 0.13)
    sim.create_boids()
    
    for frame in range(sim.frames):
        sim.update()
        sim.plot_boids_simulation()
    plt.close()


def main():
    runTest()


if __name__ == "__main__":
    #main()
    root = tk.Tk()
    app = SimulationGUI(root)
    root.mainloop()



