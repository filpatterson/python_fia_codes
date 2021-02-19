import math
from AnotherSimulation import VectorsMath, PointMath, BoidBehavior, Ship, Sprite

"""
    Class for arithmetic operations over the vector
"""
class VectorsMath:

    #   get vector with sum of dimension elements
    @staticmethod
    def sum_of_vectors(first_vector, second_vector):
        resulting_vector = [0] * len(first_vector)

        #   iterate through each vector dimension
        for i in range(len(first_vector)):
            resulting_vector[i] = first_vector[i] + second_vector[i]

        return resulting_vector

    #   get vector with negation of dimension elements
    @staticmethod
    def negation_of_vectors(first_vector, second_vector):
        resulting_vector = [0] * len(first_vector)
        for i in range(len(first_vector)):
            resulting_vector[i] = first_vector[i] - second_vector[i]

        return resulting_vector

    #   get vector with multiplication of dimension elements
    @staticmethod
    def multiplication_of_vectors(first_vector, second_vector):
        resulting_vector = [0] * len(first_vector)
        for i in range(len(first_vector)):
            resulting_vector[i] = first_vector[i] * second_vector[i]

        return resulting_vector

    #   get vector with division of dimension elements by value
    @staticmethod
    def dividing_vector_by_value(vector, value):
        if value == 0:
            return vector

        resulting_vector = [0] * len(vector)
        for i in range(len(vector)):
            resulting_vector[i] = vector[i] / value

        return resulting_vector

    #   get vector with multiplication of dimension elements by value
    @staticmethod
    def multiply_vector_by_value(vector, value):
        resulting_vector = [0] * len(vector)
        for i in range(len(vector)):
            resulting_vector[i] = vector[i] * value

        return resulting_vector


"""
    Class for arithmetic operations
"""
class PointMath:

    #   transform angle to the vector
    @staticmethod
    def angle_to_vector(ang):
        return [math.cos(ang), math.sin(ang)]

    #   get distance between two points
    @staticmethod
    def distance(first_point, second_point):
        return math.sqrt((first_point[0] - second_point[0]) ** 2 + (first_point[1] - second_point[1]) ** 2)


class BoidBehavior:
    #   define center of mass for all boids and move boid to this center
    @staticmethod
    def cohesion(boid: Sprite, boids_group: set[Sprite]):
        #   if there is less than two boids then do not work
        if len(boids_group) < 2:
            return 0

        #   init array for center of mass
        center_of_mass = [0] * len(boid.pos)
        total = 0

        #   iterate through all boids
        for anotherBoid in boids_group:
            #   accumulate positions to find center of mass and count boids
            center_of_mass = VectorsMath.sum_of_vectors(center_of_mass, anotherBoid.pos)
            total += 1

        #   if amount of boids is bigger than one boid
        if total > 1:
            #   find arithmetical average of all positions
            center_of_mass = VectorsMath.dividing_vector_by_value(center_of_mass, total)

            #   find difference of coordinates between center of mass and current boid
            differential_coordinate = VectorsMath.negation_of_vectors(center_of_mass, boid.pos)

            #   transform difference of coordinates into velocity vector
            differential_coordinate = VectorsMath.dividing_vector_by_value(
                differential_coordinate, PointMath.distance(center_of_mass, boid.pos)
            )

            #   normalize values of the vector to be applicable
            differential_coordinate = BoidBehavior.normalize_velocity_vector(differential_coordinate)
            return differential_coordinate
        #   if there is only one boid or none, then there is nothing to change
        else:
            return 0

    #   return vector for chasing ship
    @staticmethod
    def chase(boid: Sprite, ship_to_be_chased: Ship):
        #   define difference of coordinates between boid and ship
        differential_coordinate = VectorsMath.negation_of_vectors(ship_to_be_chased.pos, boid.pos)

        #   transform difference of coordinates into velocity vector
        differential_coordinate = VectorsMath.dividing_vector_by_value(
            differential_coordinate, PointMath.distance(ship_to_be_chased.pos, boid.pos) / 1.5
        )

        #   normalize velocity vector to be applicable
        differential_coordinate = BoidBehavior.normalize_velocity_vector(differential_coordinate)
        return differential_coordinate

    #   return vector for pushing away from boids (keeping minimal possible distance)
    @staticmethod
    def separation(boid: Sprite, boids_group: set[Sprite]):
        #   if there is less than two boids then do not make calculation
        if len(boids_group) < 2:
            return 0

        #   init vector for movement
        avg_counter_movement = [0] * len(boid.pos)
        total = 0

        #   iterate through all boids
        for another_boid in boids_group:
            #   find distance between boid and boid for list of all boids
            distance = PointMath.distance(boid.pos, another_boid.pos)

            #   if distance is less than 3 radii
            if distance < boid.get_radius() * 3:
                #   algorithm is similar to the "chase" principle
                differential_coordinate = VectorsMath.negation_of_vectors(boid.pos, another_boid.pos)
                differential_coordinate = VectorsMath.dividing_vector_by_value(differential_coordinate, distance / 6)
                avg_counter_movement = VectorsMath.sum_of_vectors(avg_counter_movement, differential_coordinate)
                total += 1

        if total > 1:
            avg_counter_movement = VectorsMath.dividing_vector_by_value(avg_counter_movement, total)
            return avg_counter_movement
        else:
            return 0

    #   return average velocity vector of all movement vectors of all boids
    @staticmethod
    def align(boid: Sprite, boids_group: set[Sprite]):
        if len(boids_group) < 2:
            return 0
        avg_movement = [0] * len(boid.pos)
        total = 0

        for another_boid in boids_group:
            #   accumulate all velocity vectors
            avg_movement = VectorsMath.sum_of_vectors(avg_movement, another_boid.vel)
            total += 1

        if total > 1:
            avg_movement = VectorsMath.dividing_vector_by_value(avg_movement, total)
            return avg_movement
        else:
            return 0

    #   normalize velocity vector to be applicable to the simulation
    @staticmethod
    def normalize_velocity_vector(vector: set[int]):
        for i in range(len(vector)):
            if vector[i] > 1:
                vector[i] = 1
            elif vector[i] < -1:
                vector[i] = -1

        return vector

    #   define all vectors for alignment, separation, cohesion, chase, then apply them to the velocity
    @staticmethod
    def apply_all_flock_laws(boid: Sprite, boids_group: set[Sprite], ship_to_be_chased: Ship):
        #   initialize vector for accumulating flock changes
        applied_velocity = [0] * len(boid.vel)

        #   calculate all flock movement vectors
        cohesion_velocity = BoidBehavior.cohesion(boid, boids_group)
        separation_velocity = BoidBehavior.separation(boid, boids_group)
        align_velocity = BoidBehavior.align(boid, boids_group)

        #   accumulate all flock movement vectors
        if cohesion_velocity != 0:
            applied_velocity = VectorsMath.sum_of_vectors(applied_velocity, cohesion_velocity)
        if separation_velocity != 0:
            applied_velocity = VectorsMath.sum_of_vectors(applied_velocity, separation_velocity)
        if align_velocity != 0:
            applied_velocity = VectorsMath.sum_of_vectors(applied_velocity, align_velocity)
        if ship_to_be_chased.is_chased:
            chasing_velocity = BoidBehavior.chase(boid, ship_to_be_chased)
            if chasing_velocity != 0:
                applied_velocity = VectorsMath.sum_of_vectors(applied_velocity, chasing_velocity)

        #   apply flock movement vectors to the movement vector
        boid.vel = VectorsMath.sum_of_vectors(boid.vel, applied_velocity)

        #   normalize velocity and round it to the least possible step
        boid.vel = BoidBehavior.normalize_velocity_vector(boid.vel)
        for i in range(len(boid.vel)):
            boid.vel[i] = round(boid.vel[i], 3)

        return boid.vel

"""
   The only method that must be changed in original simulation:
   we replace original fire() method with this one and append it
   to the 'space' button. If 'space' is pressed, then boids will
   chase the ship.
"""
def start_being_chased(self, shoot):
    if shoot > 0:
        if self.is_chased:
            self.is_chased = False
        elif not self.is_chased:
            self.is_chased = True

        print(self.is_chased)

