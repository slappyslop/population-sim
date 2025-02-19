package Simulation;

import java.util.ArrayList;

class Blob {
    // beings in the program
    World world;
    int age, nourishment;
    boolean canReproduce, isHungry, willDie, hasmoved;
    int location[] = new int[2];
    ArrayList<int[]> movable = new ArrayList<>();

    Blob(int age, int[] locations, World world) {
        this.world = world;
        this.age = age;
        nourishment = 8;
        this.location = locations;
        hasmoved = true;


    }

    //updates eating and reproduction thresholds
    boolean willDie() {

       return willDie = nourishment == 0 || age > 2;
    }

    void build_posArr() { // Fills a 2 dimensional array where true is a place that the blob can move, and the middle element is the current positon of the blob
        movable.ensureCapacity(9);
        for (int x = -1; x < 2; x++) {
            for (int y = -1; y < 2; y++) {
                try {
                    if (!world.places[location[0] + x][location[1] + y].isOccupied)
                        movable.add(world.places[location[0] + x][location[1] + y].position);
                } catch (
                        IndexOutOfBoundsException e) { //empty catch block as if a blob is on an edge/corner and surrounding place is out of bounds, then it won't get added to movable and no interaction occurs
                    continue;
                }

            }
        }


    }

    void feed() {
        isHungry = nourishment < 10;
        if (world.places[location[0]][location[1]].food > 0 && isHungry) {
            world.places[location[0]][location[1]].food -= 1;
            nourishment = 10;
        }
    }

    void reproduce() {
        /* Adds a new blob to the blobs list, who neighbours the reproducing blob, by picking a random place around the blob

         */
        canReproduce = nourishment > 7;
        if (canReproduce && !movable.isEmpty()) {
            nourishment -= 5;
            Blob baby = new Blob(0, movable.get(world.rand.nextInt(movable.size())), world);
            world.blobs.add(baby);
            baby.canReproduce = false;
            world.places[baby.location[0]][baby.location[1]].isOccupied = true;
            baby.nourishment = 5;
        }
    }

    void move() {
        if (!movable.isEmpty()) {
            int i = world.rand.nextInt(movable.size()+1);
            if (i< movable.size()) location = movable.get(i);
        }
    }
}
